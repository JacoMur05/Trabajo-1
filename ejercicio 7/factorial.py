# Error de sintaxis, falta ":" al final de la línea

def factorial(n):  

# Se corrigió el operador de igualdad, de "=" a "=="

    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))

# Se añadió el argumento "numero" a la función factorial

print(f"El factorial de {numero} es {factorial(numero)}")