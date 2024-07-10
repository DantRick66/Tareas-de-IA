#Programación estructurada
#Dados los siguientes problemas de programación estructurada seleccione uno

#1.- Diseñe una solución que convierte cualquier número romano a decimal.
def roman_to_decimal(roman_num):
    # Diccionario que mapea los símbolos romanos a sus valores decimales
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    decimal = 0  # Variable para almacenar el resultado decimal
    prev_value = 0  # Variable para almacenar el valor del símbolo anterior
    
    # Iteramos sobre el número romano de derecha a izquierda
    for char in reversed(roman_num):
        current_value = roman_values[char]  # Obtenemos el valor del símbolo actual
        
        # Si el valor actual es mayor o igual al anterior, se suma
        if current_value >= prev_value:
            decimal += current_value
        # Si es menor, se resta (para casos como IV, IX, etc.)
        else:
            decimal -= current_value
        
        prev_value = current_value  # Actualizamos el valor previo para la siguiente iteración
    
    return decimal  # Devolvemos el resultado decimal

# Ejemplo de uso
roman_number = input("Ingrese un número romano: ")  # Solicitamos al usuario que ingrese un número romano
result = roman_to_decimal(roman_number)  # Llamamos a la función para convertir
print(f"El número decimal equivalente es: {result}")  # Imprimimos el resultado


