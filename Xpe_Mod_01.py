# define o valor do limiar

limiar = 3

menores = []  # cria lista menores
maiores = []  # cria lista maiores

# divide o snúmeros de 1 a 18 em maiores e menores

for i in range(10):
    if i < limiar:
        menores.append(i)
    elif i > limiar:
        maiores.append(i)

# imprime na tela os valores das listas

print('Resultado final')
print('menores:', menores)
print('maiores:', maiores)
