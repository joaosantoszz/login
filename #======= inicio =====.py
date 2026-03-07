#======= inicio =====
print('CADASTRE-SE aqui!')
tentativas = 0
#========Pegando o usuário e a senha=======
while True:
    usuario = input('Crie um nome de usuário: ').strip()
    senha = input('Crie uma senha: ').strip()
    confirmaçao = input('Confirme a senha: ').strip()
    if confirmaçao == senha:
        break
    elif senha != confirmaçao:
        print('-' * 30)
        print('Senhas diferente! Tente novamente!')




#mensagem
print('Parabéns! Agora você tem uma conta!')
print('-' *  35)
print('Login abaixo')


#=======usando o while=======
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
#=========Fim=======
if tentativas < 4:
    print('Conta bloqueada!')
    print('Motivo: Atingiu o limite de tentativas!')
else:
    print('Login realizada com sucesso!')