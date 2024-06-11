from CINEMA import Funcoes

filmes = []
cadeiras = []
lanches = []
recibo = []
administrador = {'admin': '12345'}
users = {}
usuarios_registrados = 0

while True:
    print('\n\t\033[35m---=== NORDESTE EM CINEMA ===---\033[0m')
    print('\033[32m1. Registrar')
    print('2. Login')
    print('3. Sair\033[0m')

    opcao = input('\033[36mEscolha uma opção: \033[0m')

    if opcao == '1':
        user = input('\033[36mDigite um login: ')
        senha = input('Digite sua senha: \033[0m')
        if user in users:
            print('\033[3m\033[31mUsuário já existe. Por favor, escolha um nome de usuário diferente.\033[0m')
        elif len(senha) >= 4 and len(user) >= 4:
            if Funcoes.validar_input(user) and Funcoes.validar_input(senha):
                users[user] = senha
                usuarios_registrados += 1
                print('\033[3m\033[33m(Usuário registrado com sucesso!)\033[0m')
            else:
                print('\033[3m\033[31mPor favor, coloque caracteres válidos para o usuário e senha.\033[0m')
        else:
            print('\033[3m\033[31mO usuário e a senha devem ter 4 caracteres ou mais.\033[0m')

    elif opcao == '2':
        user = input('\033[36mDigite o login: ')
        senha = input('Digite a senha: \033[0m')

        # CASO O LOGIN SEJA IGUAL AO DO ADM, VAI PARA O MENU DO ADM, MAS SE O ADM QUISER ELE PODE ADICIONAR UM NOVO ADM
        if user in administrador and administrador[user] == senha:
            print('\033[3m\033[33m(Seja Bem Vindo ADM.)\033[0m')
            while True:
                print('\n\t\033[35m---=== MENU ADM ===---\033[0m')
                print('\033[32m1. Cadastrar Filme')
                print('2. Listar Filmes')
                print('3. Atualizar Filme')
                print('4. Remover Filme')
                print('5. Cadastrar Lanche')
                print('6. Cadastrar Novo ADM')
                print('7. Visualizar Perfil')
                print('8. Sair\033[0m')

                operacao_admin = input('\033[36mQual operação realizar?: \033[0m')

                if operacao_admin == '1':
                    while True:
                        print('\n\033[35mFilmes já cadastrados:\033[0m')
                        if not filmes:
                            print('\033[31mNão há filmes disponíveis no momento.\033[0m\n')
                        else:
                            for filme in filmes:
                                print(f"\033[1m\033[34mTítulo: {filme['titulo']}, Sala: {filme['sala']}, Horário: {filme['horario']}, Capacidade: {filme['capacidade']}, Valor: R${filme['valor']}\033[0m\n")
                        print('\033[33m(Caso queira sair, escreva "Sair" em qualquer campo.)\033[0m')
                        titulo = input('\033[36mDigite o título do filme: \033[0m').capitalize()
                        if titulo in ['sair', 'Sair']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        genero = input('\033[36mDigite o genêro do filme: \033[0m').capitalize()
                        if genero in ['sair', 'Sair']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        sala = input('\033[36mDigite a sala: \033[0m')
                        if sala in ['sair', 'Sair']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        horario = input('\033[36mDigite o horário separando por ":", por favor: \033[0m')
                        if horario in ['sair', 'Sair']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        capacidade = input('\033[36mDigite a capacidade da sala: \033[0m')
                        if capacidade in ['sair', 'Sair']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        valor = input('\033[36mDigite o valor do ingresso: \033[0m')
                        if valor in ['sair', 'Sair']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        if not Funcoes.validar_texto(titulo):
                            print('\033[3m\033[31mPor favor, coloque um título válido.\033[0m')
                        elif not Funcoes.validar_texto(genero):
                            print('\033[3m\033[31mPor favor, coloque um genero válido.\033[0m')
                        elif not Funcoes.validar_numeros_positivos(sala):
                            print('\033[3m\033[31mPor favor, coloque uma sala válida.\033[0m')
                        elif not Funcoes.validar_numeros_positivos(capacidade):
                            print('\033[3m\033[31mPor favor, coloque um valor de capacidade válida.\033[0m')
                        elif not Funcoes.validar_float_positivo(valor):
                            print('\033[3m\033[31mPor favor, coloque um valor válido.\033[0m')
                        elif horario.count(':') != 1:
                            print('\033[3m\033[31mPor favor, coloque um formato de horário válido.\033[0m')
                        else:
                            hora, minuto = horario.split(':')
                            if not (hora.isdigit() and minuto.isdigit()):
                                print('\033[3m\033[31mEsse horário é inválido, por favor, colocar horário válido.\033[0m')
                            else:
                                hora = int(hora)
                                minuto = int(minuto)

                                if hora < 0 or hora >= 24 or minuto < 0 or minuto >= 60:
                                    print('\033[3m\033[31mEsse horário é inválido, por favor, colocar um horário válido.\033[0m')
                                else:
                                    if Funcoes.validar_sala_ocupada(sala, filmes):
                                        print(f'\033[3m\033[31mA sala {sala} já está sendo usada. Por favor, escolha outra sala.\033[0m')
                                    else:
                                        novo_filme = {'titulo': titulo, 'genero': genero, 'sala': sala, 'horario': horario, 'capacidade': int(capacidade), 'valor': float(valor), 'cadeiras': Funcoes.cadastro_de_cadeiras({'capacidade': int(capacidade)})}
                                        filmes.append(novo_filme)
                                        cadeira = {'titulo': titulo, 'Cadeira': capacidade}
                                        cadeiras.append(cadeira)
                                        print('\033[3m\033[33m(Filme cadastrado com sucesso.)\033[0m')
                                        break

                elif operacao_admin == '2':
                    print('\n\033[35mFilmes cadastrados:\033[0m')
                    for filme in filmes:
                        print(f"\033[1m\033[34mTítulo: {filme['titulo']}, Genêro: {filme['genero']}, Sala: {filme['sala']}, Horário: {filme['horario']}, Capacidade: {filme['capacidade']}, Valor: R${filme['valor']}\033[0m\033[0m")

                elif operacao_admin == '3':
                    titulo_busca = input('\033[36mDigite o título do filme que deseja atualizar: \033[0m').capitalize()
                    filme_encontrado = next((filme for filme in filmes if filme['titulo'] == titulo_busca), None)

                    if filme_encontrado:
                        print('\033[35mO que deseja alterar?\033[0m')
                        print('\033[32m1. Título')
                        print('2. Sala')
                        print('3. Horário')
                        print('4. Capacidade')
                        print('5. Valor')
                        print('6. Genero\033[0m')

                        opcao_atualizacao = input('\033[36mDigite a opção desejada: \033[0m')

                        if opcao_atualizacao == '1':
                            novo_titulo = input('\033[36mDigite o novo título: \033[0m').capitalize()
                            if not Funcoes.validar_texto(novo_titulo):
                                print('\033[3m\033[31mPor favor, coloque um título válido.\033[0m')
                            else:
                                filme_encontrado['titulo'] = novo_titulo
                                print('\033[3m\033[33m(Título atualizado com sucesso.)\033[0m')
                        elif opcao_atualizacao == '2':
                            nova_sala = input('\033[36mDigite a nova sala: \033[0m')
                            if Funcoes.validar_sala_ocupada(nova_sala, filmes):
                                print(f'\033[3m\033[31mA sala {nova_sala} já está sendo usada. Por favor, escolha outra sala.\033[31m')
                            else:
                                filme_encontrado['sala'] = nova_sala
                                print('\033[3m\033[33m(Sala atualizada com sucesso.)\033[33m')
                        elif opcao_atualizacao == '3':
                            novo_horario = input('\033[36mDigite o novo horário: \033[0m')
                            if novo_horario.count(':') != 1:
                                print('\033[3m\033[31mPor favor, coloque um formato de horário válido.\033[0m')
                            else:
                                hora, minuto = novo_horario.split(':')
                                if not (hora.isdigit() and minuto.isdigit()):
                                    print('\033[3m\033[31mEsse horário é inválido, por favor, colocar horário válido.\033[0m')
                                else:
                                    hora = int(hora)
                                    minuto = int(minuto)

                                    if hora < 0 or hora >= 24 or minuto < 0 or minuto >= 60:
                                        print('\033[3m\033[31mEsse horário é inválido, por favor, colocar um horário válido.\033[0m')
                                    else:
                                        filme_encontrado['horario'] = novo_horario
                                        print('\033[3m\033[33m(Horário atualizado com sucesso.)\033[0m')
                        elif opcao_atualizacao == '4':
                            nova_capacidade = input('\033[36mDigite a nova capacidade: \033[0m')
                            if not Funcoes.validar_numeros_positivos(nova_capacidade):
                                print('\033[3m\033[31mPor favor, coloque um valor de capacidade válida.\033[0m')
                            else:
                                filme_encontrado['capacidade'] = int(nova_capacidade)
                                for item in cadeiras:
                                    if item['titulo'] == filme_encontrado['sala']:
                                        item['Cadeira'] = nova_capacidade
                                        break
                                print('\033[3m\033[33m(Capacidade atualizada com sucesso.)\033[0m')
                        elif opcao_atualizacao == '5':
                            novo_valor = input('\033[36mDigite o novo valor do ingresso: \033[0m')
                            if not Funcoes.validar_float_positivo(novo_valor):
                                print('\033[3m\033[31mPor favor, coloque um valor válido.\033[0m')
                            else:
                                filme_encontrado['valor'] = float(novo_valor)
                                print('\033[3m\033[33m(Valor atualizado com sucesso.)\033[0m')

                        elif opcao_atualizacao == '6':
                            novo_genero = input('\033[36mDigite o novo gênero: \033[0m').capitalize()
                            if Funcoes.validar_texto(novo_genero):
                                print('\033[3m\033[31mPor favor, coloque um genêro válido.\033[0m')
                            else:
                                filme_encontrado['genero'] = novo_genero
                                print('\033[3m\033[33m(Genêro atualizado com sucesso.)\033[0m')
                        else:
                            print('\033[3m\033[31mOpção inválida.\033[0m')
                    else:
                        print('\033[3m\033[31mFilme não encontrado.\033[0m')

                elif operacao_admin == '4':
                    while True:
                        for filme in filmes:
                            print(f"\033[1m\033[34mTítulo: {filme['titulo']}\033[0m")
                        titulo_remover = input('\033[36mDigite o título do filme que deseja remover: \033[0m').capitalize()
                        if titulo_remover in ['sair', 'Sair']:
                            break
                        filme_encontrado = next((filme for filme in filmes if filme['titulo'] == titulo_remover), None)

                        if filme_encontrado:
                            filmes.remove(filme_encontrado)
                            print('\033[3m\033[33m(Filme removido com sucesso.)\033[0m')
                        else:
                            print('\033[3m\033[31mFilme não encontrado.\033[0m')

                elif operacao_admin == '5':
                    while True:
                        print('\n\033[35mCadastrar Lanches:\033[0m')
                        if not lanches:
                            print('\033[3m\033[31m(Não há lanches disponíveis no momento.)\033[0m')
                        for lanche in lanches:
                            print(f"\033[1m\033[34mNome: {lanche['nome']}, Disponíveis: {lanche['disponiveis']}, Preço: R${lanche['preco']:.2f}\033[0m\033[0m")

                        print('\n\033[3m\033[33m(Caso queira sair, escreva "Sair" em qualquer campo.)\033[0m')
                        nome_lanche = input('\033[36mDigite o nome do produto: \033[0m').capitalize()
                        if nome_lanche.lower() == 'sair':
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break

                        lanches_disponiveis = input('\033[36mDigite a quantidade: \033[0m')
                        if lanches_disponiveis.lower() == 'sair':
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break

                        preco_lanche = input('\033[36mDigite o preço do produto: \033[0m')
                        if preco_lanche.lower() == 'sair':
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break

                        if not Funcoes.validar_texto(nome_lanche):
                            print('\033[3m\033[31mPor favor, coloque um nome válido para o lanche.\033[0m')
                        elif not Funcoes.validar_float_positivo(preco_lanche):
                            print('\033[3m\033[31mPor favor, coloque um preço válido.\033[0m')
                        elif not Funcoes.validar_numeros_positivos(lanches_disponiveis):
                            print('\033[3m\033[31mPor favor, coloque uma quantidade válida.\033[0m')
                        else:
                            novo_lanche = {'nome': nome_lanche, 'disponiveis': int(lanches_disponiveis), 'preco': float(preco_lanche)}
                            lanches.append(novo_lanche)
                            print('\033[3m\033[33m(Lanche cadastrado com sucesso.)\033[0m')

                elif operacao_admin == '6':
                    controlador = True
                    while controlador:
                        print('\n\033[35mUsuários registrados:\033[0m')
                        if not users:
                            print('\033[3m\033[31mNão há usuários registrados ainda.\033[0m')
                            break
                        else:
                            while True:
                                for usuarios, senha in users.items():
                                    print(f'\033[1m\033[34mUsuário: {usuarios}, Senha: {senha}\033[0m\033[0m')
                                print('\n\033[3m\033[33m(Caso queira sair, escreva "Sair" em qualquer campo.)\033[0m')
                                novo_adm = input('\033[36mDigite o login do novo ADM: \033[0m')
                                if novo_adm in ['sair', 'Sair']:
                                    print('\033[3m\033[31mSaindo...\033[0m')
                                    controlador = False
                                    break
                                nova_senha_adm = input('\033[36mDigite a senha do novo ADM: \033[0m')
                                if nova_senha_adm in ['sair', 'Sair']:
                                    print('\033[3m\033[31mSaindo...\033[0m')
                                    controlador = False
                                    break

                                if novo_adm in administrador:
                                    print('\033[3m\033[31mADM já existe. Por favor, escolha um nome de usuário diferente.\033[0m')
                                elif len(nova_senha_adm) >= 4 and len(novo_adm) >= 4:
                                    if novo_adm in users:
                                        administrador[novo_adm] = users.pop(novo_adm)
                                        print('\033[3m\033[33m(Usuário promovido a ADM com sucesso!)\033[0m')
                                    elif Funcoes.validar_input(novo_adm) and Funcoes.validar_input(nova_senha_adm):
                                        administrador[novo_adm] = nova_senha_adm
                                        print('\033[3m\033[33m(Novo ADM registrado com sucesso!)\033[0m')
                                        controlador = False
                                        break
                                    else:
                                        print('\033[3m\033[31mPor favor, coloque caracteres válidos para o usuário e senha.\033[0m')
                                else:
                                    print('\033[3m\033[31mO usuário e a senha devem ter 4 caracteres ou mais.\033[0m')

                elif operacao_admin == '7':
                    while True:
                        print('\n\033[35mPerfil ADM:\033[0m\n')
                        print(f'\033[34mLogin: {user}')
                        relatorio = input('Deseja ver o relatório? (sim/nao): \033[0m').strip().lower()
                        if relatorio in ['sim', 's']:
                            Funcoes.relatorio_admin(filmes, lanches, users, recibo)
                            pedir_relatorio_adm = input('\n\033[32mDeseja Exportar o Relatório? (sim/não): \033[0m').lower()
                            if pedir_relatorio_adm in ['sim', 's']:
                                Funcoes.exportar_relatorio_admin(filmes, lanches, users, recibo, 'relatorio_cinema.txt')
                                print('\033[3m\033[31mSaindo...\033[0m')
                                break
                            elif pedir_relatorio_adm in ['não', 'n', 'nao']:
                                print('\033[3m\033[31mSaindo...\033[0m')
                                break
                        elif relatorio in ['nao', 'não', 'n']:
                            print('\033[3m\033[31mSaindo...\033[0m')
                            break
                        else:
                            print("\033[3m\033[31mPor favor, digite (Sim) ou (Não).\033[0m")

                elif operacao_admin == '8':
                    print('\033[3m\033[31mSaindo...\033[0m')
                    break
                else:
                    print('\033[3m\033[31mOpção inválida.\033[0m')

        elif user in users and users[user] == senha:
            print('\033[3m\033[33m(Seja Bem Vindo.)\033[0m')
            operador = True
            while operador:
                print('\n\t\033[35m---=== MENU USUÁRIO ===---\033[0m')
                print('\033[32m1. Listar Filmes')
                print('2. Comprar Ingressos')
                print('3. Refeitório')
                print('4. Visualizar Recibo')
                print('5. Exportar Recibo')
                print('6. Perfil')
                print('7. Sair\033[0m')

                operacao_user = input('\033[36mQual operação realizar?: \033[36m')

                if operacao_user == '1':
                    print('\n\033[35mFilmes disponíveis:\033[0m')
                    if not filmes:
                        print('\033[3m\033[31m(Não há filmes disponíveis no momento.)\033[0m')
                    else:
                        for idx, filme in enumerate(filmes, start=1):
                            print(f"\033[1m\033[34m{idx}. Título: {filme['titulo']}, Genêro: {filme['genero']}, Sala: {filme['sala']}, Horário: {filme['horario']}, Capacidade: {filme['capacidade']}, Valor: R${filme['valor']}\033[0m\033[0m")

                elif operacao_user == '2':
                    while True:
                        if not filmes:
                            print('\033[3m\033[31m(Não há filmes disponíveis no momento.)\033[0m')
                            break
                        else:
                            print('\n\033[35mFilmes disponíveis:\033[0m')
                            for idx, filme in enumerate(filmes, start=1):
                                print(f"\033[1m\033[34m{idx}. Título: {filme['titulo']}, Genêro: {filme['genero']}, Sala: {filme['sala']}, Horário: {filme['horario']}, Ingressos restantes: {filme['capacidade']}, Valor: R${filme['valor']}\033[0m\033[0m")
                            print('\033[33m(Escreva "Sair" para sair.)\033[0m')
                            filme_numero = input('\n\033[36mDigite o número do filme que deseja: \033[0m')
                            if filme_numero in ['Sair', 'sair']:
                                print('\033[3m\033[31mSaindo...\033[0m')
                                break

                            if not Funcoes.validar_numeros_positivos(filme_numero) or int(filme_numero) > len(filmes):
                                print('\033[3m\033[31mPor favor, insira um número de filme válido.\033[0m')
                            else:
                                filme_escolhido = filmes[int(filme_numero) - 1]
                                ingressos_comprados = Funcoes.comprar_ingressos(filme_escolhido, user)
                                if ingressos_comprados:
                                    recibo.append([filme_escolhido['titulo'], filme_escolhido['valor'], ingressos_comprados, user])
                                    print('\033[3m\033[33m(Ingressos comprados com sucesso.)\033[0m')
                                    break

                elif operacao_user == '3':
                    if not lanches:
                        print('\033[3m\033[31m(Não há lanches disponíveis no momento.)\033[0m')

                    else:
                        print('\n\033[35mLanches disponíveis:\033[0m')
                        for idx, lanche in enumerate(lanches, start=1):
                            print(f'\033[1m\033[34m{idx}. Nome: {lanche['nome']}, Disponíveis: {lanche['disponiveis']}, Preço: R${lanche['preco']:.2f}\033[0m')

                        lanche_numero = input('\033[36mDigite o número do lanche que deseja comprar: \033[0m')

                        if not Funcoes.validar_numeros_positivos(lanche_numero) or int(lanche_numero) > len(lanches):
                            print('\033[3m\033[31mPor favor, insira um número de lanche válido.\033[0m')

                        else:
                            lanche_escolhido = lanches[int(lanche_numero) - 1]
                            quantidade_lanche = input(f'\033[36mQuantas {lanche_escolhido["nome"]} deseja comprar?: \033[0m')

                            if not Funcoes.validar_numeros_positivos(quantidade_lanche):
                                print('\033[3m\033[31mPor favor, insira uma quantidade válida.\033[0m')

                            else:
                                quantidade_lanche = int(quantidade_lanche)

                                if quantidade_lanche > lanche_escolhido['disponiveis']:
                                    print('\033[3m\033[31mQuantidade indisponível. Por favor, escolha uma quantidade menor.\033[0m')

                                else:
                                    lanche_escolhido['disponiveis'] -= quantidade_lanche
                                    lanche_comprado = {

                                        'tipo': 'lanche',

                                        'nome': lanche_escolhido['nome'],

                                        'preco_total': lanche_escolhido['preco'] * quantidade_lanche,

                                        'quantidade': quantidade_lanche,

                                        'cliente': user

                                    }

                                    recibo.append([lanche_escolhido['nome'], lanche_escolhido['preco'], lanche_comprado, user])
                                    print('\033[3m\033[33m(Lanche comprado com sucesso.)\033[0m')

                elif operacao_user == '4':
                    if not recibo:
                        print('\033[3m\033[31m(Nenhuma compra realizada.)\033[0m')

                    else:
                        print('\033[36mRecibo\033[0m')
                        Funcoes.recibo_cliente(user, recibo)

                elif operacao_user == '5':
                    if not recibo:
                        print('\033[3m\033[31m(Nenhuma compra realizada.)\033[0m')
                    else:
                        nome_arquivo = f"recibo_{user}.txt"
                        Funcoes.exportar_recibo(user, recibo, nome_arquivo)
                        print('\033[3m\033[33m(Recibo exportado com sucesso.)\033[0m')

                elif operacao_user == '6':
                    while True:
                        print('\n\t\033[35m---=== Cliente ===---\033[0m\n')
                        print(f'\033[34mUsuário: {user}\033[0m')
                        print('\n\033[32m1 - Filmes Assistidos')
                        print('2 - Excluir Conta')
                        print('3 - Sair\033[0m')

                        opcao3 = input('\033[36mQual operação deseja executar?: \033[0m')

                        if opcao3 == '1':
                            print('\n\033[35mFilmes assistidos:\033[0m')
                            filmes_vistos = set()
                            filmes_assistidos = {filme['titulo'] for filme in filmes}
                            for item in recibo:
                                if item[3] == user and item[0] in filmes_assistidos:
                                    filmes_vistos.add(item[0])
                            if filmes_vistos:
                                for filme_visto in filmes_vistos:
                                    print(f"\033[3m\033[34m- {filme_visto}\033[0m")
                            else:
                                print('\033[3m\033[31mVocê não viu nenhum filme ainda\033[0m')

                        elif opcao3 == '2':
                            confirmacao = input('\033[36mTem certeza que deseja excluir sua conta? (sim ou não): \033[36m').lower()
                            if confirmacao in ['sim', 's']:
                                del users[user]
                                print('\033[3m\033[33m(Conta excluída com sucesso.)\033[0m')
                                usuarios_registrados -= 1
                                operador = False
                                break
                            elif confirmacao in ['não', 'n', 'nao']:
                                break
                            else:
                                print('\033[3m\033[31mPor favor, digite "Sim" ou "Não"!\033[0m')

                        elif opcao3 == '3':
                            break

                        else:
                            print('Opcão inválida')

                elif operacao_user == '7':
                    break
                else:
                    print('\033[3m\033[31mOpção inválida.\033[0m')

        else:
            print('\033[3m\033[31mUsuário ou senha inválidos. Tente novamente.\033[0m')

    elif opcao == '3':
        print('\033[3m\033[31mSaindo...\033[0m')
        break
    else:
        print('\033[3m\033[31mOpção inválida.\033[0m')
