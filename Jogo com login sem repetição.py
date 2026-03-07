#======= inicio =====
print('CADASTRE-SE aqui!')
tentativas = 0
#======== Pegando o usuário e a senha =======
while True:
    usuario = input('Crie um nome de usuário: ').strip()
    senha = input('Crie uma senha: ').strip()
    confirmaçao = input('Confirme a senha: ').strip()
    if confirmaçao == senha:
        break
    elif senha != confirmaçao:
        print('-' * 30)
        print('Senhas diferente! Tente novamente!')
        
#======= Mensagem de boas-vindas =======
print('Parabéns! Agora você tem uma conta!')
print('-' *  35)
print('Login abaixo')


#=======Sistema de login=======
while True:
    usuario2 = input('Nome de usuário: ').strip()
    senha2 = input('Digite a senha: ').strip()
    tentativas += 1
    if usuario2 == usuario and senha2 == senha:
        break
    elif tentativas == 3:
        mensagem_bloqueada = "conta bloaqueada"
        break
    else:
        print('-' * 30)
        print('Senha ou Usuário incorreto! Tente novamente!')
        print(f'Você fez {tentativas} tentativas de 3')

#========= Fim do programa de login =======

if tentativas == 3:
    print('Conta bloqueada!')
    print('Motivo: Atingiu o limite de tentativas!')
else:
    cert = print('Login realizada com sucesso!')

#======= Fim do código de Login =======

#======= inicio do jogo de advinhação =======
if cert == print('Login realizada com sucesso!'):
    print(" ")
    print('-' * 30)
    print(" ")
    print('Agora você tem acesso ao jogo de advinhação!')


#===== Biblioteca de random=====
import random


#========= Nome do jogo =========

print('🎮 Jogo de Adivinhação\U0001F3AF!')

#====== Pegando dificuldade =======

print('1️⃣ Fácil 2️⃣ Médio 3️⃣ Difícil ')
d = str(input('Qual dificuldade você deseja: ').strip())



#===== Variavel para tentativas =====
t = 0

#===== Sobre as dificuldades =====

if d == '1':
    f = random.randint(1, 10)

elif d == '2':
    f = random.randint(1, 50)

elif d == '3':
    f = random.randint(1, 100)

#======= Guardando a dificuldade ========

if d == '1':
    limite = '10'
elif d == '2':
    limite = '50'
elif d == '3':
    limite = '100'


#===== Funcionamento do jogo =====

while True:
    p = int(input("🕵️ Descubra o número secreto entre 1 e {}: ".format(limite)))
    t += 1 #calculando dificuldade
    if f == p:
         print('🏆 Você acertou! Parabéns!!! 🎉')
         break
    
    elif p > f:
        print('⬇️ Tente um número menor!')

    elif p < f:
        print('⬆️ Tente um número maior!')

    else:
         print('Você errou! Tente novamente!')

#===== Guardando a classificação ======

if t == 1:
    c = 'Excelente'

elif t <= 5:
    c = 'Ótimo'

elif t <= 10:
    c = 'Bom'

else:
    c = 'Ruim'


#===== Fim do jogo =====

print('🎯Você conseguiu em {} tentativas!'.format(t))
print("⭐ Classificação: {}".format(c))

    
