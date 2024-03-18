def determina_tipo_triangulo(a, b, c):  
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é um triângulo"
    elif a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"
    elif a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def testa_triangulo():
    while True:
        a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
        b = float(input("Digite o comprimento do segundo lado do triângulo: "))
        c = float(input("Digite o comprimento do terceiro lado do triângulo: "))
        print(determina_tipo_triangulo(a, b, c))

testa_triangulo()