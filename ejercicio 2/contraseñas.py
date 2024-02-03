# Error de importación, debería ser "import random

import random 
import string

# Error de sintaxis en la definición de la función. Faltan los dos puntos (:) al final.
# Además, hay un error en el nombre de la función. Debería ser "generar_contraseña".

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
# Debería ser "return contraseña"

print(generar_contraseña())

# Error de llamada a la función.