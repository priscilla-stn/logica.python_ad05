num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")


if operador == "+":
    resultado = num1 + num2
    resultado = round(resultado, 2)
    print(int(resultado) if resultado.is_integer() else resultado)

elif operador == "-":
    resultado = num1 - num2
    resultado = round(resultado, 2)
    print(int(resultado) if resultado.is_integer() else resultado)

elif operador == "*":
    resultado = num1 * num2
    resultado = round(resultado, 2)
    print(int(resultado) if resultado.is_integer() else resultado)

elif operador == "/":
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = num1 / num2
        resultado = round(resultado, 2)
        print(int(resultado) if resultado.is_integer() else resultado)

else:
    print("Operador inválido")