import os

pessoas = ['Maria', 'Pedro', 'André', 'Camila']

nome_pessoa = input('Qual seu nome? ')

if nome_pessoa == 'Maria':
    cor_1 = input('Qual sua cor favorita Maria? ')
    print(f'Cor favorita da Maria: {cor_1}')
elif nome_pessoa == 'Pedro':
    cor_2 = input('Qual sua cor favorita? ')
    print(f'Cor favorita do Pedro: {cor_2}')
elif nome_pessoa == 'André':
    cor_3 = input('Qual sua cor favorita? ')
    print(f'Cor favorita do André: {cor_3}')
elif nome_pessoa == 'Camila':
    cor_4 = input('Qual sua cor favorita? ')
    print(f'Cor favorita da Camila: {cor_4}')

# VARIÁVEL = str / True/ int/ float/ complex 
# LISTA = []
# MATRIZ = [ [], [] ]
# TUPLA = ()
# DICIONÁRIO = {}

cor1 = input('\nDigite sua cor favorita: ')
cor2 = input('Digite sua cor favorita: ')
cor3 = input('Digite sua cor favorita: ')
cor4 = input('Digite sua cor favorita: ')

print('A cor da Maria foi: ' + cor1)
print('A cor do Pedro foi: ' + cor2)
print('A cor do André foi: ' + cor3)
print('A cor da Camila foi: ' + cor4)

os.system('cls')
lista_nomes = ['indice_0', 'indice_1', 'indice_2']
lista_cores = []

# lista_cores[0] = input('Digite sua cor preferida: ')
# lista_cores[1] = input('Digite sua cor preferida: ')
# lista_cores[2] = input('Digite sua cor preferida: ')
# lista_cores[3] = input('Digite sua cor preferida: ')

# append - adiciona um item smepre no final
# range - n-1 (4-1)
for i in range(5):
    #lista_cores[i] = input("Digite uma cor: ")
    lista_cores.append(input('Digite sua cor favorita: '))
print(lista_cores)

# print('LISTA ATUAL: ', lista_nomes)
# nome_temp = input("Digite um nome: ")
# indice_lista = int(input("Digite qual indice vai ser alterado: "))
# lista_nomes[indice_lista] = nome_temp
# print("LISTA MODIFICADA: ",lista_nomes)