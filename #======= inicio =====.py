#======= inicio =====
print('CADASTRE-SE aqui!')

#========Pegando o usuário e a senha=======
usuario = input('Crie um nome de usuário: ').strip()
senha = input('Crie uma senha: ').strip()

#mensagem
print('Parabéns! Agora você tem uma conta!')
print('-' *  35)
print('Login abaixo')


#=======usando o while=======
while True:
    usuario2 = input('Nome de usuário: ').strip()
    senha2 = input('Digite a senha: ').strip()
    if usuario2 == usuario and senha2 == senha:
        break
    else:
        print('Senha ou Usuário incorreto!')
        print('Tente novamente!')

#=========Fim=======
print('Login realizado com sucesso!')