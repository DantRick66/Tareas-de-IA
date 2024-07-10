#Daniel Javier De Leon Thomas (2023-1087)
#PARTE 1
#Dados los siguientes algoritmos de ordenamiento en forma de pseudocodigo,
#realice el programa correspondiente de UNO de ellos.

#4. Selection sort.
def selection_sort(A):
    # Recorremos toda la lista excepto el último elemento
    for j in range(len(A) - 1):
        # Asumimos que el elemento actual es el mínimo
        i_min = j
        
        # Buscamos el elemento más pequeño en el resto de la lista
        for i in range(j + 1, len(A)):
            if A[i] < A[i_min]:
                # Si encontramos un elemento más pequeño, actualizamos i_min
                i_min = i
        
        # Si el elemento mínimo no es el actual, hacemos el intercambio
        if i_min != j:
            A[j], A[i_min] = A[i_min], A[j]
    
    # La lista A ha sido ordenada in-place (sin crear una nueva lista)

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una lista de ejemplo
    lista = [64, 34, 25, 12, 22, 11, 90]
  
    # Llamamos a la función de ordenamiento
    selection_sort(lista)
    
    print("Lista ordenada( Selection sort):", lista)



