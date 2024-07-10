#Programación ORIENTADA A OBJETOS
#Dados los siguientes problemas de programación orientada a objetos
#seleccione uno e implemente una clase que cumpla lo que se pide

#3.- Diseñe una clase que represente a un empleado con nombre, apellido, cédula,
#fecha de nacimiento y salario, y que permita obtener su nombre completo, sus
#iniciales, su edad y su ganancia anual.
from datetime import datetime

class Empleado:
    def __init__(self, nombres, apellidos, cedula, fecha_nacimiento, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        self.salario = salario

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def iniciales(self):
        return f"{self.nombres[0]}.{self.apellidos.split()[0][0]}."

    def edad(self):
        hoy = datetime.now()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def ganancia_anual(self):
        return self.salario * 12
    
# Solicitar datos al usuario
nombres = input("Introduce tus nombres: ")
apellidos = input("Introduce tus apellidos: ")
cedula = input("Introduce tu número de cédula: ")
fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd-mm-aaaa): ")
salario = float(input("Introduce tu salario mensual: "))

# Crear instancia de Empleado con los datos ingresados
empleado = Empleado(nombres, apellidos, cedula, fecha_nacimiento, salario)

# Mostrar la información
print(f"\nNombre completo: {empleado.nombre_completo()}")
print(f"Iniciales: {empleado.iniciales()}")
print(f"Edad: {empleado.edad()} años")
print(f"Ganancia anual: RD${empleado.ganancia_anual():,}")
