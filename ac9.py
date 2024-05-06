distancia = int(input())  # Lendo a distância em quilômetros
velocidade_relativa = 90 - 60  # Calculando a velocidade relativa em km/h
tempo_em_horas = distancia / velocidade_relativa  # Calculando o tempo em horas
tempo_em_minutos = tempo_em_horas * 60  # Convertendo o tempo para minutos
print(f'{int(tempo_em_minutos)} minutos')  # Imprimindo o tempo necessário em minutos




def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

# Lendo o valor de N
n = int(input())

# Verificando se N está dentro do intervalo especificado
if 0 < n < 13:
    resultado = calcular_fatorial(n)
    print(resultado)
else:
    print("O valor de N está fora do intervalo permitido.")





    # Função para calcular o valor total da compra
def calcular_valor_compra(produtos, lista_compras):
    valor_total = 0
    for item in lista_compras:
        produto, quantidade = item
        if produto in produtos:
            preco_unitario = produtos[produto]
            valor_total += preco_unitario * quantidade
    return valor_total

# Número de casos de teste
num_casos_teste = int(input())

# Loop sobre os casos de teste
for _ in range(num_casos_teste):
    # Leitura dos produtos disponíveis na feira e seus preços
    num_produtos_disponiveis = int(input())
    produtos = {}
    for _ in range(num_produtos_disponiveis):
        produto, preco = input().split()
        produtos[produto] = float(preco)
    
    # Leitura dos produtos que Dona Parcinova deseja comprar
    num_produtos_compra = int(input())
    lista_compras = []
    for _ in range(num_produtos_compra):
        produto, quantidade = input().split()
        lista_compras.append((produto, int(quantidade)))
    
    # Cálculo do valor total da compra
    valor_total = calcular_valor_compra(produtos, lista_compras)
    
    # Impressão do valor total formatado
    print(f'R$ {valor_total:.2f}')







 # Lendo o tipo de chá real
tipo_cha_real = int(input())

# Lendo as respostas dos competidores
respostas = list(map(int, input().split()))

# Contando o número de competidores que acertaram
num_acertos = respostas.count(tipo_cha_real)

# Imprimindo o número de competidores que acertaram
print(num_acertos)






# Lendo os valores de entrada
competidores, folhas_compradas, folhas_por_competidor = map(int, input().split())

# Calculando o total de folhas necessárias
folhas_necessarias = competidores * folhas_por_competidor

# Verificando se a quantidade de folhas compradas é suficiente
if folhas_necessarias <= folhas_compradas:
    print('S')
else:
    print('N')







# Lendo a quantidade de intervalos de tempo
N = int(input())

# Inicializando a distância total como zero
distancia_total = 0

# Loop sobre os intervalos de tempo
for _ in range(N):
    # Lendo o tempo decorrido e a velocidade média do intervalo
    tempo, velocidade_media = map(int, input().split())
    
    # Calculando a distância percorrida no intervalo e somando à distância total
    distancia_total += tempo * velocidade_media

# Imprimindo a distância total percorrida
print(distancia_total)












# Lendo o número de pessoas que clicaram no terceiro link
t = int(input())

# Calculando o número de pessoas que clicaram no primeiro link
primeiro_link = 4 * t

# Imprimindo o resultado
print(primeiro_link)













# Lendo o tamanho da sequência
N = int(input())

# Lendo a sequência de números
sequencia = [int(input()) for _ in range(N)]

# Encontrando a primeira e última ocorrência do número 2 na sequência
primeiro_2 = sequencia.index(2)
ultimo_2 = N - 1 - sequencia[::-1].index(2)

# Contando os números 1 entre o primeiro e último 2
numeros_1 = sequencia.count(1, primeiro_2, ultimo_2 + 1)

# Imprimindo a quantidade máxima de números que podem ser marcados
print(numeros_1)







