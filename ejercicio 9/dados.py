import random  # Corregido el error tipográfico en la importación

3# Se añadió ":" al final de la línea

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado): 
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados  # Se corrigió "retunr" por "return"

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))

# Se añadieron los argumentos correctos

lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado)  
print(f"Resultados del lanzamiento: {lanzamientos}")

