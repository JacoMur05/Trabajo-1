# Error de sintaxis, falta ":" al final de la línea

def celsius_a_fahrenheit(celsius):  

# Error matemático, falta el operador "+" entre (9/5) y 32

    return (celsius * 9/5) + 32 

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))  # Se cambió "float("Ingrese la temperatura en Celsius: ")" por "float(input("Ingrese la temperatura en Celsius: "))" para solicitar la entrada al usuario
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
