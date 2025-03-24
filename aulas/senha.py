from getpass import getpass

minha_senha = '12345'

def VerificarSenha(nova_senha):
    if nova_senha == minha_senha:
        print('senha valida')
    else:
        print('senha invalida')

# senha_1 = input("digite sua senha: ")
senha_1 = getpass("digite sua senha: ")
print(senha_1)

import senha
print(senha.minha_senha)

var_senha = input("digite sua nova senha: ")
senha.VerificarSenha(var_senha)