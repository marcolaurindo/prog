#Vamos começar com a equação de segundo grau

#Primeiro calculamos o delta
def calcular_o_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

delta = calcular_o_delta

#Depois pedimos os valores de a, b, c
a = float(input("Informe o parâmetro a da equação "))
b = float(input("Informe o parâmetro b da equação "))
c = float(input("Informe o parâmetro c da equação "))

#Achando o resultado da primeira raiz
raiz1_x = (-b + delta(a, b, c)**0.5) / (2*a)

#Mostrando o resultado da primeira raiz
print("A primeira raiz da equação é: ", raiz1_x)

#Achando a segunda raiz
raiz2_x = (-b - delta(a, b, c)**0.5) / (2*a)

#Mostrando o resultado da segunda raiz
print("A segunda raiz da equação é ", raiz2_x)



#Agora vamos descobrir se o ano é bissexto ou nao

#Primeiro pedimos ao usuário informar um ano
ano = int(input("Informe um ano: "))

#Aqui achamos a resposta com essa formula. Se for bissexto será TRUE e se não for será FALSE
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

#Resposta aqui
print(bissexto)




#Professor, so uma observação que gostaria de fazer, fiz todos esse comentários no meu vscode mas não veio pra cá. Tive que escrever todos aqui no github.

