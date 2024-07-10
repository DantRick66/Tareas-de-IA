#Daniel Javier De Leon Thomas (2023-1087)
#PARTE 2
#Dados los siguientes algoritmos de búsqueda en forma de pseudocódigo, realice
#el programa correspondiente de UNO de ellos.

#1. Binary Search.
import math

def binary_search(A, T):
    # Inicializamos los índices de inicio y fin
    L = 0
    R = len(A) - 1
    
    while L <= R:
        # Calculamos el índice medio
        m = math.floor((L + R) / 2)
        
        # Si el elemento en la posición media es menor que T
        if A[m] < T:
            L = m + 1  # Ajustamos la búsqueda a la mitad derecha
        # Si el elemento en la posición media es mayor que T
        elif A[m] > T:
            R = m - 1  # Ajustamos la búsqueda a la mitad izquierda
        else:
            return m  # Hemos encontrado T, retornamos su posición
    
    # Si salimos del bucle sin encontrar T, la búsqueda no tuvo éxito
    return "unsuccessful"

# Ejemplo de uso
if __name__ == "__main__":
    # Lista ordenada de ejemplo
    A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Elemento a buscar
    T = 7
    
    resultado = binary_search(A, T)
    if resultado != "unsuccessful":
        print(f"El elemento {T} se encuentra en la posición {resultado}")
    else:
        print(f"El elemento {T} no se encuentra en la lista")
    
    # Probamos con un elemento que no está en la lista
    T = 8
    resultado = binary_search(A, T)
    if resultado != "unsuccessful":
        print(f"El elemento {T} se encuentra en la posición {resultado}")
    else:
        print(f"El elemento {T} no se encuentra en la lista")


