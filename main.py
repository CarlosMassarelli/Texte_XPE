# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# utilizando um módulo

import areas as ar

print(ar.triangulo(5, 8))
print(ar.quadrado(5))
print(ar.PI)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# importando novos módulos
# modulo com funções matemáticas para cálculos mais complexos
import math

print('Função cosseno:', math.cos(100))
print('Função log:', math.log(10))

# modulo para construção de sequências elaboradas
import itertools

print(list(
    itertools.combinations('ABCD', 3)))  # combinação a cada 3 print(list(itertools.permutations(['a', 'b', 'c'], 2)))
# permutação a cada 2


# modulo para manipulação de timestamps (datas, horários, deltas etc.)
from datetime import datetime, timedelta

print('Datetime atual:', datetime.now())
print('Datetime após 7 dias:', datetime.now() + timedelta(days=7))

# modulo para criação de números e sequências randômicas
import random

print('Numero aleatório entre 0 e 1:', random.random())
print('Inteiro aleatório entre 50 e 100:', random.randint(50, 100))

# modulo para funcionalidades que dependem do sistema operacional
import os

# os.mkdir('pasta')  # cria um diretório chamado pasta
print('Caminho completo:', os.path.join('/home/antonio', 'pasta', 'arquivo.txt'))

# manipulação de arquivos
# abrindo e lendo arquivo txt
arquivo = open('cidades.txt', 'r')
linhas = arquivo.read()
arquivo.close()
print('somente lendo arquivo')
print(linhas)

# leitura com readlines
arquivo = open('cidades.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()
print(linhas)
type(linhas)

# iterando a variável e retirando '/n'
novas_linhas = []
for linha in linhas:
    novas_linhas.append(linha.rstrip())
print(novas_linhas)

# escrevendo no arquivo
arquivo = open('cidades.txt', 'a')
arquivo.write('RJ; São Gonçalo; 1021903\n')
arquivo.close()

# inserindo novas linhas
linhas = [
    'AL; Maceió; 1005319\n',
    'RJ; Duque de Caxias; 878402\n',
    'RN; Natal; 862044\n',
    'MS; Campo Grande; 843120\n'
]
arquivo = open('cidades.txt', 'a')
arquivo.writelines(linhas)
arquivo.close()
print(linhas)

# compreensão de LISTAS
# CODIGO EXTENSO
potencias = []
for item in range(1, 11):
    potencias.append(item ** 2)
print(potencias)

# lista compreesiva
potencias = [item ** 2 for item in range(1, 11)]
print(potencias)

# outras listas comprimidas
print([n * 10 for n in range(1, 16)])  # multiplica por 10 numero de 1 a 15
print([c.upper() for c in 'antonio'])  # cria lista com os caracteres da palavra
print([(n % 2 == 0) for n in range(0, 10)])  # indica se n é par ou não

# para uma condição na iteração temos
# ele elevará a 2 para itens de 1 a 10 SE O RESTO DA DIVISÃO POR 2 DO ITEM FOR DIFERENTE DE ZERO
potencias=[item**2 for item in range(1, 11) if item % 2 !=0]
print(potencias)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
