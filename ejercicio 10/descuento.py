# Se añadió ":" al final de la línea
def calcular_precio_con_descuento(precio_base, porcentaje_descuento):  
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento

# Se corrigió "retunr" por "return"


    return precio_final 
 
# Corregido el uso de "float" en lugar de "input" para la entrada del precio_base

precio_base = float(input("Ingrese el precio base del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
