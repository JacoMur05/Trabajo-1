# Error de sintaxis, falta un ":" al final de la línea.

def contar_palabra(texto, palabra):
    return texto.lower().split().count(palabra.lower())

# Error de sintaxis en la llamada a la función. Falta un paréntesis de cierre ")" 
# después de "palabra_buscada".

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

# Se corrigió la llamada a la función y el f-string.
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.")
