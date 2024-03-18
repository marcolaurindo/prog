
#Exercicio 1


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
        try:
            a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
            b = float(input("Digite o comprimento do segundo lado do triângulo: "))
            c = float(input("Digite o comprimento do terceiro lado do triângulo: "))
            print(determina_tipo_triangulo(a, b, c))
            break
        except ValueError:
            print("Por favor, insira um número válido para o comprimento do lado.")

testa_triangulo()



#Exercicio 2

def dia_semana(numero):
    dias_semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
    
    if 1 <= numero <= 7:
        return dias_semana[numero - 1]
    else:
        return ""

def testa_dia_semana():
    num_dia = int(input("Digite o número do dia da semana (1 a 7): "))
    nome_dia = dia_semana(num_dia)
    
    if nome_dia:
        print("O dia da semana correspondente é:", nome_dia)
    else:
        print("Número de dia inválido.")

testa_dia_semana()



#Exercicio 3

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calculadora():
    print("Bem-vindo à calculadora!")
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = soma(num1, num2)
            elif operacao == '-':
                resultado = subtracao(num1, num2)
            elif operacao == '*':
                resultado = multiplicacao(num1, num2)
            elif operacao == '/':
                resultado = divisao(num1, num2)
            else:
                print("Operação inválida.")
                continue

            print("O resultado é:", resultado)
            break

        except ValueError:
            print("Por favor, insira números válidos.")

calculadora()

