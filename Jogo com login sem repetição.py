import random

# ======== CADASTRO ========
print('CADASTRE-SE aqui!')
while True:
    usuario = input('Crie um nome de usuário: ').strip()
    senha = input('Crie uma senha: ').strip()
    confirmacao = input('Confirme a senha: ').strip()

    if confirmacao == senha:
        break
    else:
        print('-' * 30)
        print('Senhas diferentes! Tente novamente!')

print('Parabéns! Agora você tem uma conta!')
print('-' * 35)
print('Login abaixo')

# ======== LOGIN ========
tentativas = 0

while True:
    usuario2 = input('Nome de usuário: ').strip()
    senha2 = input('Digite a senha: ').strip()
    tentativas += 1

    if usuario2 == usuario and senha2 == senha:
        print('Login realizado com sucesso!')
        break
    elif tentativas == 3:
        print('Conta bloqueada!')
        print('Motivo: Atingiu o limite de tentativas!')
        exit()
    else:
        print('-' * 30)
        print('Senha ou usuário incorreto! Tente novamente!')
        print(f'Você fez {tentativas} tentativa(s) de 3')

# ======== MENU PRINCIPAL ========
while True:
    print('\n' + '=' * 30)
    print('MENU PRINCIPAL')
    print('1 - Jogar')
    print('2 - Sair')
    print('=' * 30)

    menu = input('Escolha uma opção: ').strip()

    if menu == '1':
        # ======== REPETIR O JOGO ========
        while True:
            print('\n🎮 Jogo de Adivinhação 🎯')

            t = 0

            # ======== ESCOLHA DA DIFICULDADE ========
            while True:
                print('1️⃣ Fácil   2️⃣ Médio   3️⃣ Difícil')
                d = input('Qual dificuldade você deseja: ').strip()

                if d == '1':
                    f = random.randint(1, 10)
                    limite = 10
                    break
                elif d == '2':
                    f = random.randint(1, 50)
                    limite = 50
                    break
                elif d == '3':
                    f = random.randint(1, 100)
                    limite = 100
                    break
                else:
                    print('Escolha somente essas opções!')

            # ======== FUNCIONAMENTO DO JOGO ========
            while True:
                try:
                    p = int(input(f'🕵️ Descubra o número secreto entre 1 e {limite}: '))
                    t += 1

                    if p == f:
                        print('🏆 Você acertou! Parabéns!!! 🎉')
                        break
                    elif p > f:
                        print('⬇️ Tente um número menor!')
                    else:
                        print('⬆️ Tente um número maior!')
                except ValueError:
                    print('Digite apenas números!')

            # ======== CLASSIFICAÇÃO ========
            if t == 1:
                c = 'Excelente'
            elif t <= 5:
                c = 'Ótimo'
            elif t <= 10:
                c = 'Bom'
            else:
                c = 'Ruim'

            print(f'🎯 Você conseguiu em {t} tentativas!')
            print(f'⭐ Classificação: {c}')

            # ======== JOGAR NOVAMENTE ========
            novamente = input('Quer jogar novamente? (s/n): ').strip().lower()

            if novamente != 's':
                break

    elif menu == '2':
        print('Programa encerrado!')
        break

    else:
        print('Escolha uma opção válida!')


    
