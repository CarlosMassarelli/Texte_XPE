# Define o valor de PI
PI = 3.141592


# Calcula a área do quadrado
def quadrado(l):
    return l ** 2


# calcula a área de um triângulo
def triangulo(b, h):
    return (b * h) / 2


# calcula a área de um círculo
def circulo(r):
    return PI * (r ** 2)


# calcula a área de uma elipse
def elipse(a, b):
    return PI * a * b


# calcula a área de um trapézio
def trapezio(a, b, h):
    return (a + b) * h / 2
