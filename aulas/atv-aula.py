nota_1 = float(input('Digite sua nota P1: '))
nota_2 = float(input('Digite sua nota P2: '))

print(f'Nota da P1: {nota_1}')
print(f'Nota da P2: {nota_2}')

mediaNotas = (nota_1 + nota_2)/2
print(f'Média: {mediaNotas}')

if mediaNotas >= 5.0: 
    print('Aprovado. Sua média foi igual a ' + str(mediaNotas))
elif mediaNotas >= 2.0:
    print(f'Está de Recuperação. Sua média foi igual a {mediaNotas}')
else:
    print(f'Reprovado. Sua média foi igual a {mediaNotas:.2f}')