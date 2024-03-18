
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
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

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
        return None

def calculadora():
    operacoes = {'soma': soma, 'subtracao': subtracao, 'multiplicacao': multiplicacao, 'divisao': divisao}
    operacao = input("Digite a operação (soma, subtracao, multiplicacao ou divisao): ").lower()
    
    if operacao in operacoes:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)

            if operacao == 'divisao' and num2 == 0:
                print("Erro: divisão por zero")
            else:
                resultado = operacoes[operacao](num1, num2)
                print(f"Resultado: {resultado}")
        else:
            print("Erro: Insira números válidos.")
    else:
        print("Operação inválida")

# Teste da função calculadora
calculadora()
