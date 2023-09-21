import math
GRAVIDADE = 10

def velocidadeInicial(forca, massa):
    v0 = forca/massa
    return v0
def velocidadeInicialHorizontal(forca, massa, angulo):
    v0 = velocidadeInicial(forca, massa)
    v0x = v0 * math.cos(math.radians(angulo))
    return v0x
def velocidadeInicialVertical(forca, massa, angulo):
    v0 = velocidadeInicial(forca, massa)
    v0y = v0 * math.sin(math.radians(angulo))
    return v0y
def velocidadeHorizontal(forca, massa, angulo, tempo):
    if(tempo >= tempoDeVoo(forca, massa, angulo)): return 0
    v0x = velocidadeInicialHorizontal(forca, massa, angulo)
    vx = v0x
    return v0x
def velocidadeVertical(forca, massa, angulo, tempo):
    if(tempo >= tempoDeVoo(forca, massa, angulo)): return 0
    v0y = velocidadeInicialVertical(forca, massa, angulo)
    vy = v0y - (GRAVIDADE * tempo)
    return vy
def tempoDeVoo(forca, massa, angulo):
    v0y = velocidadeInicialVertical(forca, massa, angulo)
    t_max = 2 * v0y / GRAVIDADE
    return t_max
def alcance(forca, massa, angulo):
    t_max = tempoDeVoo(forca, massa, angulo)
    v0x = velocidadeInicialHorizontal(forca, massa, angulo)
    x_max =  v0x * t_max 
    return x_max
def localDaQueda(forca, massa, angulo, x0, y0):
    x1 = x0 + alcance(forca, massa, angulo) + (y0 / velocidadeHorizontal(forca, massa, angulo, 1))
    y1 = y0
    return (x1,y1)

print("----------------------------------------")
print("------Bem vindo ao canhão calc 3000-----")
print("----------------------------------------")

forca = float(input("Digite a força inicial (N): "))
angulo = float(input("Digite o ângulo de inclinação em graus(º): "))
x0 = float(input("Digite a coordenada x do canhão (m): "))
y0 = float(input("Digite a coordenada y do canhão (m): "))

massa = 0.5
print(f"A nossa bala pesa {massa}Kg, bem levinha...")

print(f"velocidade inicial absoluta = {velocidadeInicial(forca, massa):.2f}m/s")
print(f"velocidade horizontal inicial = {velocidadeInicialHorizontal(forca, massa, angulo):.2f}m/s")
print(f"velocidade vertical inicial = {velocidadeInicialVertical(forca, massa, angulo):.2f}m/s")

print(f"tempo total de voo = {tempoDeVoo(forca, massa, angulo):.2f}s")

x,y = localDaQueda(forca, massa, angulo, x0, y0)
d = alcance(forca, massa, angulo)
print(f"local da queda foi nas coordenadas ({x:.2f},{y:.2f}), a {d:.2f}m do local horiginal")

print("----------------------------------------")
print("velocidades de voo ao longo da trajetória:")
print("----------------------------------------")
for i in range(10):
    j = i/10
    t = tempoDeVoo(forca, massa, angulo) * j
    vx = velocidadeHorizontal(forca, massa, angulo, t)
    vy = velocidadeVertical(forca, massa, angulo, t)
    print(f"a velocidade no instante {t:.2f} foi")
    print(f"\thorizontal: {vx:.2f} m/s")
    print(f"\tvertical: {vy:.2f} m/s")
print("----------------------------------------")