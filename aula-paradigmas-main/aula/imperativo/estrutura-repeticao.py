
#somar numero ate um limite
# limite = 100
# soma = 0
# numero = 1

# while soma < limite:
#     soma += numero
#     numero += 1
#     print(soma)
#     print(numero)


#encontrar o primeiro numero divisivel por 7 em um intervalo
# 1 -> 99
# for numero in range(1, 100):
#     if numero % 7 == 0:
#         print(numero)
#         break

#verificar se todos os itens de uma lista sao positivos
numeros = [1,2,3,8,9, -11]
todos_positivos = True

for numero in numeros:
    if numero < 0:
        todos_positivos = False

if todos_positivos == True:
    print("todos positivos")
else:
    print("existe negativo")
