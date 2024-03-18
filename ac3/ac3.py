
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
        a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
        b = float(input("Digite o comprimento do segundo lado do triângulo: "))
        c = float(input("Digite o comprimento do terceiro lado do triângulo: "))
        print(determina_tipo_triangulo(a, b, c))
        break

testa_triangulo()


#Exercicio 2


def dia_semana(numero):
    dias_da_semana = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado"
    }
    
    if 1 <= numero <= 7:
        return dias_da_semana[numero]
    else:
        return "Número inválida"

def testa_dia_semana():
  
    
    numero = int(input("Digite o número correspondente ao dia da semana (1 a 7): "))
    print(dia_semana(numero))


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

calculadora()

