# RECURSAO 

def fatorial(numero):
    if numero == 0:
        return 1
    
    return numero * fatorial(numero-1)

print(fatorial(4))

# FIBONACCI DE 8 = 0, 1, 1, 2, 3, 5, 8, 13...

# OITAVO NUMERO DE FIBONACCI 21
# SEXTO NUMERO DE FIBONACCI 8

# CALCULAR O N-ÉSIMO NUMERO DE FIBONACCI
def fibonacci(numero):
    
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 2) + fibonacci(numero - 1)
    
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
    