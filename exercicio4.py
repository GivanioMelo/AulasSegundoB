#podemos recuperar informações do usuário pedindo para que ele digite valores
#utilizando a função Input, por exemplo

# a = input("digite um numero")
# print(f"o numero que você digitou foi: {a}")

#escreva um código que receba 10 numeros, e escreva
#   o primeiro mais o segundo
#   o produto do terceiro e do quarto
#   a divisão do quinto pelo sexto
#   o sétimo elevado ao oitavo
#   o nono menos o décimo

x1 = float(input("digite um numero..."))
x2 = float(input("digite um numero..."))
x3 = float(input("digite um numero..."))
x4 = float(input("digite um numero..."))
x5 = float(input("digite um numero..."))
x6 = float(input("digite um numero..."))
x7 = float(input("digite um numero..."))
x8 = float(input("digite um numero..."))
x9 = float(input("digite um numero..."))
x10 = float(input("digite um numero..."))


soma = x1+x2
print(f"a soma do primeiro mais o segundo é: {soma}")

produto = x3*x4
print(f"o produto do terceiro pelo quarto é: {produto}")

divisao = x5/x6
print(f"o quociente da divisão do quinto pelo sexto é: {divisao}")

potencia = x7 ** x8
print(f"a potencia do sétimo pelo oitavo é: {potencia}")

subtracao = x9 - x10
print(f"o resultado da subtração do nono pelo décimo é: {subtracao}")

input("digite enter para continuar...")