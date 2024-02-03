def es_palindromo(texto):  # Error de sintaxis, falta ":" al final de la línea
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra_frase):  # Se añadió el argumento "palabra_frase" a la función es_palindromo
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
