# funcao pura
def soma(a,b):
    return a + b 

print(soma(3,4))
print(soma(3,4))

#funcao de alta ordem - recebe funcao como parametro
def aplicar_duas_vezes(func, valor):
    return func(func(valor))


def incrementar(x):
    return x + 1

def elevar_ao_quadrado(x):
    return x ** 2

def dividir_por_dois(x):
    return x / 2

print(incrementar(6))

print(aplicar_duas_vezes(incrementar,6))

print(elevar_ao_quadrado(6))

print(aplicar_duas_vezes(elevar_ao_quadrado,6))


#aplicar transformacao em cada item da lista
numeros = [1,2,3,4,5,6]

def aplicar_transformacao(funcao, lista):
    return [funcao(x) for x in lista] # mesmo efeito de fazer um for em uma lista- list comprehension

numeros_quadrado = aplicar_transformacao(elevar_ao_quadrado, numeros)
numeros_quadrado_dividido_dois = aplicar_transformacao(dividir_por_dois, numeros_quadrado)

print(numeros_quadrado)
print(numeros_quadrado_dividido_dois)