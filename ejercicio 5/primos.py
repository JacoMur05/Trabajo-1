# Error de sintaxis, falta ":" al final de la línea

def es_primo(numero):  

# Se añadió ":" al final de la línea

    if numero < 2: 
        return False
    for i in range(2, int(numero**0.5) + 1):  # Se añadió ":" al final de la línea
        if numero % i == 0:
            return False
        
# Se corrigió "retrun" por "return"

    return True  # Se corrigió "retrun" por "return"

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(num)]  # Se corrigió "es_primo()" por "es_primo(num)"
print("Números primos:", primos)
