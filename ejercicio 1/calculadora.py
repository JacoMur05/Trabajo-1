def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

#LA VARIABLE ESTA MAL DECLARADA 
    
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 != 0:

#LA VARIABLE ESTA MAL DECLARADA 

            resultado = num1 / num2
        else:
            resultado = "No se puede dividir por cero"
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)

calculadora()

#Se cambió el nombre de la variable de num a num1 en la operación de suma.
#Se agregó una verificación de división por cero en caso de que 
#el usuario elija la operación de división.
