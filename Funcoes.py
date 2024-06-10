import random


def validar_input(input_digitado):
    return not any(caractere.isspace() for caractere in input_digitado) and len(input_digitado) > 0


def validar_float_positivo(valor2):
    if '.' in valor2:
        validacao_float = valor2.split('.')
        if len(validacao_float) == 2 and validacao_float[0].isdigit() and validacao_float[1].isdigit():
            return float(valor2) > 0
    elif valor2.isdigit():
        return float(valor2) > 0
    return False


def validar_texto(texto):
    return texto.strip() != ''


def validar_numeros_positivos(valor1):
    return valor1.isdigit() and int(valor1) > 0


def validar_sala_ocupada(sala, filmes):
    for filme in filmes:
        if filme['sala'] == sala:
            return True
    return False


def cadastro_de_cadeiras(filme):
    return ['Livre' for cadeira in range(filme['capacidade'])]


def reservar_cadeiras(filme, quantidade):
    cadeiras_disponiveis = [i for i, estado in enumerate(filme['cadeiras']) if estado == 'Livre']
    cadeiras_reservadas = []
    while len(cadeiras_reservadas) < quantidade:
        cadeira = input(f'\033[36mDigite o número da cadeira que deseja reservar (1-{filme["capacidade"]}): \033[0m').lower()
        if cadeira.isdigit():
            cadeira = int(cadeira) - 1
            if cadeira in cadeiras_disponiveis:
                cadeiras_reservadas.append(cadeira)
                cadeiras_disponiveis.remove(cadeira)
            else:
                print('\033[3m\033[31mEssa cadeira já está ocupada ou não existe. Escolha outra.\033[0m')
        else:
            print('\033[3m\033[31mNúmero de cadeira inválido. Tente novamente.\033[0m')

    return cadeiras_reservadas


def cadeiras_random(filme, quantidade):
    cadeiras_disponiveis = [i for i, estado in enumerate(filme['cadeiras']) if estado == 'Livre']
    if quantidade > len(cadeiras_disponiveis):
        raise ValueError("Quantidade de cadeiras solicitadas é maior do que as disponíveis.")
    cadeiras_reservadas = random.sample(cadeiras_disponiveis, quantidade)
    return cadeiras_reservadas


def comprar_ingressos(filme, user):
    quantidade = input('\033[36mQuantos ingressos deseja comprar: \033[0m')
    if not validar_numeros_positivos(quantidade):
        print('\033[3m\033[31mPor favor, insira uma quantidade válida de ingressos.\033[0m')
        return False
    quantidade = int(quantidade)
    if quantidade > filme['capacidade']:
        print('\033[3m\033[31mPerdão, mas a quantidade que você quer comprar é maior que a quantidade de cadeira da sala.\033[0m')
        return False

    cadeiras_disponiveis = len([estado for estado in filme['cadeiras'] if estado == 'Livre'])
    if quantidade > cadeiras_disponiveis:
        print('\033[3m\033[31mPerdão, mas a quantidade de cadeiras disponíveis é menor do que a quantidade desejada.\033[0m')
        return False

    opcao_reserva = input('\033[36mDeseja reservar uma cadeira? (sim/nao): \033[0m').strip().lower()
    valor_total = filme['valor'] * quantidade
    reserva = False
    cadeiras = []

    if opcao_reserva in ['sim', 's']:
        reserva = True
        cadeiras = reservar_cadeiras(filme, quantidade)
        print('\033[3m\033[33m(Reserva realizada, valor atualizado.)\033[0m')
        valor_total += 30 * quantidade
    elif opcao_reserva in ['nao', 'n', 'não']:
        cadeiras = cadeiras_random(filme, quantidade)
        if cadeiras is None:
            print('\033[3m\033[31mErro: Não foi possível atribuir cadeiras automaticamente.\033[0m')
            return False
        print('\033[3m\033[33m(Cadeiras atribuídas automaticamente.)\033[0m')
    else:
        print('\033[3m\033[31mOpção inválida.\033[0m')
        return False

    for cadeira in cadeiras:
        filme['cadeiras'][cadeira] = 'Reservado'

    filme_comprado = {
        'filme': filme['titulo'],
        'quantidade': quantidade,
        'valor_total': valor_total,
        'reserva': reserva,
        'cadeiras': cadeiras,
        'cliente': user,
        'tipo': 'filme'
    }

    filme['capacidade'] -= quantidade
    return filme_comprado


def exportar_recibo(usuario, recibo, nome_arquivo):
    total_usuario = 0
    primeiro_item = True
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        for item in recibo:
            if item[3] == usuario:
                if isinstance(item[2], dict):
                    tipo_item = item[2].get('tipo', 'filme')
                    if tipo_item == 'filme':
                        filme_comprado = item[2]
                        preco_total = filme_comprado['valor_total']
                        quantidade = filme_comprado['quantidade']
                        reserva = filme_comprado['reserva']
                        cadeiras = ', '.join(str(cadeira + 1) for cadeira in filme_comprado.get('cadeiras', []))
                        subtotal = preco_total
                        if primeiro_item:
                            file.write(f'Usuário: {usuario}\n')
                            primeiro_item = False
                        if reserva:
                            file.write(f'{item[0]} x{quantidade}: R${subtotal:.2f} (Reserva de cadeira: {cadeiras})\n')
                        else:
                            file.write(f'{item[0]} x{quantidade}: R${subtotal:.2f} (Cadeiras: {cadeiras})\n')
                        total_usuario += subtotal
                    elif tipo_item == 'lanche':
                        lanche_comprado = item[2]
                        preco_unitario = lanche_comprado['preco_total'] / lanche_comprado['quantidade']
                        quantidade = lanche_comprado['quantidade']
                        subtotal = preco_unitario * quantidade
                        if primeiro_item:
                            file.write(f'Usuário: {usuario}\n')
                            primeiro_item = False
                        file.write(f'{item[0]} x{quantidade}: R${subtotal:.2f}\n')
                        total_usuario += subtotal
                    else:
                        file.write("Tipo de item desconhecido.\n")
                else:
                    file.write(f"{item[0]} x{item[2]}: R${item[1]:.2f}\n")
                    total_usuario += item[1]
        file.write(f'Total: R${total_usuario:.2f}\n')


def criar_txt_relatorio_admin(filmes, lanches, users, recibo):
    relatorio = []
    relatorio.append('\n---=== RELATÓRIO DO CINEMA ===---\n')
    relatorio.append(f'Usuários registrados: {len(users)}')
    relatorio.append(f'Filmes cadastrados: {len(filmes)}')
    relatorio.append(f'Lanches no refeitório: {len(lanches)}')

    total_faturado = 0

    for item in recibo:
        if isinstance(item[2], dict):
            tipo_item = item[2].get('tipo')
            if tipo_item == 'filme':
                total_faturado += item[2].get('valor_total', 0)
            elif tipo_item == 'lanche':
                total_faturado += item[2].get('preco_total', 0)

    relatorio.append(f'\nO cinema faturou: R${total_faturado:.2f}')

    relatorio.append('\nVendas por Filme:')
    for filme in filmes:
        vendas_filme = [item for item in recibo if item[0] == filme['titulo']]
        total_ingressos = sum(item[2]['quantidade'] for item in vendas_filme if isinstance(item[2], dict))
        relatorio.append(f"Filme: {filme['titulo']}, Ingressos Vendidos: {total_ingressos}")
        for venda in vendas_filme:
            relatorio.append(f"Cliente: {venda[3]}, Quantidade: {venda[2]['quantidade']}")
            if venda[2].get('reserva', False):
                relatorio.append('(Reserva de cadeira: R$30.00)')

    relatorio.append('\nVendas de Lanches:')
    for lanche in lanches:
        vendas_lanche = [item for item in recibo if item[0] == lanche['nome']]
        total_lanches = sum(item[2]['quantidade'] for item in vendas_lanche if isinstance(item[2], dict))
        relatorio.append(f"Lanche: {lanche['nome']}, Quantidade Vendida: {total_lanches}, Disponíveis: {lanche['disponiveis']}")
        for venda in vendas_lanche:
            relatorio.append(f"Comprador: {venda[3]}, Quantidade: {venda[2]['quantidade']}")

    relatorio.append('\nHistórico dos Usuários:')
    for user in users:
        atividades_usuario = [item for item in recibo if item[3] == user]
        if atividades_usuario:
            relatorio.append(f'Usuário: {user}')
            total_usuario = 0
            for atividade in atividades_usuario:
                if isinstance(atividade[2], dict):
                    tipo_item = atividade[2].get('tipo', 'filme')
                    if tipo_item == 'filme':
                        filme_comprado = atividade[2]
                        preco_total = filme_comprado['valor_total']
                        quantidade = filme_comprado['quantidade']
                        reserva = filme_comprado['reserva']
                        cadeiras = ', '.join(str(cadeira + 1) for cadeira in filme_comprado.get('cadeiras', []))
                        subtotal = preco_total
                        if reserva:
                            relatorio.append(f'{atividade[0]} x{quantidade}: R${subtotal:.2f} (Reserva de cadeira: {cadeiras})')
                        else:
                            relatorio.append(f'{atividade[0]} x{quantidade}: R${subtotal:.2f} (Cadeiras: {cadeiras})')
                        total_usuario += subtotal
                    elif tipo_item == 'lanche':
                        lanche_comprado = atividade[2]
                        preco_unitario = lanche_comprado['preco_total'] / lanche_comprado['quantidade']
                        quantidade = lanche_comprado['quantidade']
                        subtotal = preco_unitario * quantidade
                        relatorio.append(f'{atividade[0]} x{quantidade}: R${subtotal:.2f}')
                        total_usuario += subtotal
                    else:
                        relatorio.append("Tipo de item desconhecido.")
                else:
                    relatorio.append(f'{atividade[0]} x{atividade[2]}: R${atividade[1]:.2f}')
                    total_usuario += atividade[1]
            relatorio.append(f'Total: R${total_usuario:.2f}\n')

    return '\n'.join(relatorio)


def exportar_relatorio_admin(filmes, lanches, users, recibo, nome_arquivo):
    relatorio = criar_txt_relatorio_admin(filmes, lanches, users, recibo)
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(relatorio)


def recibo_cliente(usuario, recibo):
    total_usuario = 0
    primeiro_item = True
    for item in recibo:
        if item[3] == usuario:
            if isinstance(item[2], dict):
                tipo_item = item[2].get('tipo', 'filme')
                if tipo_item == 'filme':
                    filme_comprado = item[2]
                    preco_total = filme_comprado['valor_total']
                    quantidade = filme_comprado['quantidade']
                    reserva = filme_comprado['reserva']
                    cadeiras = ', '.join(str(cadeira + 1) for cadeira in filme_comprado.get('cadeiras', []))
                    subtotal = preco_total
                    if primeiro_item:
                        print(f'\033[1m\033[34mUsuário: {usuario}\033[0m')
                        primeiro_item = False
                    if reserva:
                        print(f'\033[1m\033[34m{item[0]} x{quantidade}: R${subtotal:.2f} \033[3m\033[33m(Reserva de cadeira: {cadeiras})\033[0m')
                    else:
                        print(f'\033[1m\033[34m{item[0]} x{quantidade}: R${subtotal:.2f} \033[3m\033[33m(Cadeiras: {cadeiras})\033[0m')
                    total_usuario += subtotal
                elif tipo_item == 'lanche':
                    lanche_comprado = item[2]
                    preco_unitario = lanche_comprado['preco_total'] / lanche_comprado['quantidade']
                    quantidade = lanche_comprado['quantidade']
                    subtotal = preco_unitario * quantidade
                    if primeiro_item:
                        print(f'\033[1m\033[34mUsuário: {usuario}\033[0m')
                        primeiro_item = False
                    print(f'\033[1m\033[34m{item[0]} x{quantidade}: R${subtotal:.2f}\033[0m')
                    total_usuario += subtotal
                else:
                    print('\033[3m\033[31mNada foi encontrado.\033[0m')
            else:
                print(f"\033[1m\033[34m{item[0]} x{item[2]}: R${item[1]:.2f}\033[0m")
                total_usuario += item[1]
    print(f'\033[1m\033[33mTotal: R${total_usuario:.2f}\033[0m\n')


def relatorio_admin(filmes, lanches, users, recibo):
    print('\n\033[35m---=== RELATÓRIO DO CINEMA ===---\033[0m\n')
    print(f'\033[34mUsuários registrados: {len(users)}')
    print(f'Filmes cadastrados: {len(filmes)}')
    print(f'Lanches no refeitório: {len(lanches)}\033[0m')

    total_faturado = 0

    for item in recibo:
        if isinstance(item[2], dict):
            tipo_item = item[2].get('tipo')
            if tipo_item == 'filme':
                total_faturado += item[2].get('valor_total', 0)
            elif tipo_item == 'lanche':
                total_faturado += item[2].get('preco_total', 0)

    print(f'\n\033[1m\033[33mO cinema faturou: R${total_faturado:.2f}\033[0m')

    print('\n\033[35mVendas por Filme:\033[0m')
    for filme in filmes:
        vendas_filme = [item for item in recibo if item[0] == filme['titulo']]
        total_ingressos = sum(item[2]['quantidade'] for item in vendas_filme if isinstance(item[2], dict))
        print(f"\n\033[34mFilme: {filme['titulo']}, Ingressos Vendidos: {total_ingressos}\033[0m")
        for venda in vendas_filme:
            print(f"\033[95mCliente: {venda[3]}, Quantidade: {venda[2]['quantidade']}\033[0m")
            if venda[2].get('reserva', False):
                print('\033[3m\033[33m(Reserva de cadeira: R$30.00)\033[0m')

    print('\n\033[35mVendas de Lanches:\033[0m')
    for lanche in lanches:
        vendas_lanche = [item for item in recibo if item[0] == lanche['nome']]
        total_lanches = sum(item[2]['quantidade'] for item in vendas_lanche if isinstance(item[2], dict))
        print(f"\033[34mLanche: {lanche['nome']}, Quantidade Vendida: {total_lanches}, Disponíveis: {lanche['disponiveis']}\033[0m")
        for venda in vendas_lanche:
            print(f"\033[95mComprador: {venda[3]}, Quantidade: {venda[2]['quantidade']}\033[0m")

    print('\n\033[35mHistórico dos Usuários:\033[0m')
    for user in users:
        atividades_usuario = [item for item in recibo if item[3] == user]
        if atividades_usuario:
            print(f'\n\033[34mUsuário: {user}\033[0m')
            total_usuario = 0
            for atividade in atividades_usuario:
                if isinstance(atividade[2], dict):
                    tipo_item = atividade[2].get('tipo', 'filme')
                    if tipo_item == 'filme':
                        filme_comprado = atividade[2]
                        preco_total = filme_comprado['valor_total']
                        quantidade = filme_comprado['quantidade']
                        reserva = filme_comprado['reserva']
                        cadeiras = ', '.join(str(cadeira + 1) for cadeira in filme_comprado.get('cadeiras', []))
                        subtotal = preco_total
                        if reserva:
                            print(f'\033[34m{atividade[0]} x{quantidade}: R${subtotal:.2f} (Reserva de cadeira: {cadeiras})\033[0m')
                        else:
                            print(f'\033[34m{atividade[0]} x{quantidade}: R${subtotal:.2f} (Cadeiras: {cadeiras})\033[0m')
                        total_usuario += subtotal
                    elif tipo_item == 'lanche':
                        lanche_comprado = atividade[2]
                        preco_unitario = lanche_comprado['preco_total'] / lanche_comprado['quantidade']
                        quantidade = lanche_comprado['quantidade']
                        subtotal = preco_unitario * quantidade
                        print(f'\033[34m{atividade[0]} x{quantidade}: R${subtotal:.2f}\033[0m')
                        total_usuario += subtotal
                    else:
                        print('\033[3m\033[31mTipo de item desconhecido.\033[0m')
                else:
                    print(f'\033[34m{atividade[0]} x{atividade[2]}: R${atividade[1]:.2f}\033[0m')
                    total_usuario += atividade[1]
            print(f'\033[1m\033[33mTotal: R${total_usuario:.2f}\033[0m\n')
