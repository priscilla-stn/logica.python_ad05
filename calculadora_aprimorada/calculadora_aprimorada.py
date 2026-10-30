def somarmultiplosnumeros(lista) :
    soma = 0

    for numero in lista:
     soma = soma + numero

    return soma

def multiplicarmultiplosnumeros(lista) :
    resultado = 1

    for numero in lista:
     resultado = resultado * numero

    return resultado

lista1 = [5, 10, 15]
lista2 = [-1, 3, 2.5]

print("Soma da lista 1:", somarmultiplosnumeros(lista1))
print("Multiplicação da lista 1:", multiplicarmultiplosnumeros(lista1))

print("Soma da lista 2:", somarmultiplosnumeros(lista2))
print("Multiplicação da lista 2:", multiplicarmultiplosnumeros(lista2))


def ehpar(numero):
    return ehinteiro(numero) and numero % 2 == 0

def ehinteiro(numero):
    return numero % 1 == 0
   
numero1 = 8
numero2 = 4.2

print("O número", numero1, "é par?", ehpar(numero1))
print("O número", numero1, "é inteiro?", ehinteiro(numero1))

print("O número", numero2, "é par?", ehpar(numero2))
print("O número", numero2, "é inteiro?", ehinteiro(numero2))
