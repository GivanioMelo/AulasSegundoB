# Implemente um programa em python, 
# que receba dois valores e imprima 
# a média entre eles, defina uma função 
# customizada para calcular a média.

def media(a,b):
    s = a + b
    m = s / 2
    return m

a = float(input("Insira um numero: "))
b = float(input("Insira outro mnumero: "))
print(f"A média de {a} e {b} é: {media(a,b):.4f}")