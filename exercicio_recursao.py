import time
def contagemRegressiva(i:int):
    if(i <= 0): print(0)
    else:
        time.sleep(1)
        print(i)
        contagemRegressiva(i-1)

print("contagem regressiva de 10:")
contagemRegressiva(10)

def somaRecursiva(i: int):
    if( i <= 1): return 1
    else:
        return i + somaRecursiva(i-1)

print("soma recursiva")
print(f"de 1: {somaRecursiva(1)}")
print(f"de 2: {somaRecursiva(2)}")
print(f"de 3: {somaRecursiva(3)}")
print(f"de 4: {somaRecursiva(4)}")
print(f"de 5: {somaRecursiva(5)}")
print(f"de 6: {somaRecursiva(6)}")
print(f"de 7: {somaRecursiva(7)}")

#Exercício 1: Potência Recursiva
def potencia(base, expoente):
    if expoente == 0: return 1
    else: return base * potencia(base, expoente - 1)

print(f"2 elevado a 3: {potencia(2, 3)}")
print(f"3 elevado a 2: {potencia(3, 2)}")
print(f"2 elevado a 2: {potencia(2, 2)}")
print(f"3 elevado a 3: {potencia(3, 3)}")

#Exercício 3: Inversão de String
def inverter_string(s):
    if len(s) == 0: return ""
    else: return s[-1] + inverter_string(s[:-1])

print("inverter strings")
print(f'recursividade : {inverter_string("recursividade")}')
print(f'inconstitucionalissimamente : {inverter_string("inconstitucionalissimamente")}')
print(f'paralelepipedo : {inverter_string("paralelepipedo")}')
print(f'osso : {inverter_string("osso")}')
print(f'salas : {inverter_string("salas")}')
print(f'socos : {inverter_string("socos")}')