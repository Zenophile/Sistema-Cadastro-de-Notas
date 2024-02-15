import os
while True:
    print('\nBem vindo ao sistema de notas de Alunos\n')
    print('Digite 1 cadastrar um aluno\n')
    print('Digite 2 para mostrar a lista de alunos cadastrados\n')
    print('Digite 3 para escolher um aluno específico\n')
    print('Digite 4 para cadastrar as notas de um aluno')
    print('Digite 5 para Sair\n')
    escolha = int(input())
    if escolha == 5:
        print('Fechando o programa')
        print('...')
        break
    while True:
        if escolha == 1:
            nome_arquivo = input('Digite o nome do Aluno: ')
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write('Esse aluno foi Adicionado:')
            print(f'Arquivo {nome_arquivo} foi adicionado')
            print('\nDigite 1 para adicionar outro aluno ou 2 para voltar ao menu inicial\n')
            escolha2 = int(input())
            if escolha2 == 1:
                continue
            else:
                break
        elif escolha == 2:
            os.listdir()
            files = [f for f in os.listdir() if os.path.isfile(f)]
            print(files)
            break
        elif escolha == 3:
            nome_aluno = input('Digite o nome do aluno que você deseja escolher')
            try:
                with open(nome_aluno, 'r') as arquivo:
                    notas = arquivo.read()
                    print(f"\nVocê escolheu o aluno: '{nome_aluno}'")
                    print(notas)
                    soma_notas = 0
                    numero_notas = 0
                    arquivo.seek(0)
                    for nota in arquivo:
                        numero_notas += 1
                        soma = [int(x) for x in nota.split()]
                        soma_notas += sum(soma)

                    print("A soma de todas as notas é igual a", soma_notas)
                    print("Para se passar de ano é necessário ter uma média mínima de 70")
                    media = soma_notas / numero_notas
                    print(f"\nA media de '{nome_aluno}' é ", media)
                    if media >= 70:
                        print(f"{nome_aluno} passou de ano")
                    else:
                        print(f"{nome_aluno} esta de recuperação")

                    print('\nDeseja digitar o nome de outro aluno? se sim digite 1, se não digite 2 para retornar ao menu')
                    n = int(input())
                    if n == 1:
                        continue
                    elif n == 2:
                        print('Retornando ao menu')
                        break

            except FileNotFoundError:
                print(f"Esse aluno não está cadastrado no sistema.")
        elif escolha == 4:
            nome_aluno_notas = input('Digite o nome do aluno que você deseja cadastrar as notas')

            notas_input = input('Digite as notas do aluno separadas por um espaço, sendo elas respectivamente\n Mat, Geo, Hist, PT, QUI')

            try:
                notas = [int(x) for x in notas_input.split()]
            except ValueError:
                print('Nota inválida, a nota do Aluno deve ser composta por um valor número inteiro, ex: 7')
                exit()
            try:
                with open(nome_aluno_notas, 'w') as arquivo2:
                    for nota in notas:
                        arquivo2.write(str(nota))
                        arquivo2.write('\n')
                print('Notas inseridas')
                print('Retornando ao menu')
                break
            except FileNotFoundError:
                print('Esse aluno não se encontra cadastrado em nosso sistema.')




        else:
            print('Opção inválida')
            break

#ajustes finais

