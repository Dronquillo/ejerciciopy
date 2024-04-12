import math
# 1 Escribe un programa en Python que imprima tu nombre en la pantalla.
def imprimir_nombre():
    print("Dario Ronquillo")
    # Aquí se imprime el nombre en la pantalla

if __name__ == "__main__":
    imprimir_nombre()
#     # Se llama a la función imprimir_nombre() para ejecutarla

# # # 2 Escribe un programa que calcule la suma de los números del 1 al 10.
def suma_1_al_10():
    suma = sum(range(1, 11))  
    #return suma
    print ("La suma es ",suma)
    

if __name__ == "__main__":
    resultado = suma_1_al_10()  
#     # Se imprime el resultado de la suma

# 3 Crea variables para almacenar tu edad, nombre y estatura, e imprímelas en pantalla.
def imprimir_datos_personales(nombre, edad, estatura):
    
    print(f"Nombre: {nombre}\nEdad: {edad}\nEstatura: {estatura}")
    # Se imprimen en pantalla los datos personales recibidos como argumentos

if __name__ == "__main__":

    nombre = "Dario Ronquillo"
    edad = 45
    estatura = 1.65
    imprimir_datos_personales(nombre, edad, estatura)
    
    # Se llama a la función imprimir_datos_personales() para mostrar los datos

# 4 Escribe un programa que determine si un número ingresado por el usuario es par o impar.
def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"


if __name__ == "__main__":
   num = int(input("Ingrese un número: "))  
   print(par_o_impar(num))  

# 5 Crea una función que calcule el área de un círculo dado su radio.
# import math

def area_circulo(radio):
    area = math.pi * radio ** 2  
    return area
    
    # Se devuelve el área calculada

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  
    # Se imprime el área calculada del círculo
    print(area_circulo(radio)) 

#6 Define una función que reciba dos números como argumentos y devuelva su suma.
def suma(a, b):
    return a + b
    # Se devuelve la suma de los dos números recibidos como argumentos

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))  
    # Se solicita al usuario que ingrese el segundo número
    print("La suma es:", suma(num1, num2))  

# 7 Modifica la función que calcula el área del círculo para que reciba el radio como parámetro.

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area
    # Se devuelve el área calculada

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  
    print("El área del círculo es:", area_circulo(radio)) 

# 8 Diseña un programa que convierta grados Celsius a Fahrenheit y viceversa, utilizando funciones para realizar los cálculos.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Se aplica la fórmula de conversión de Celsius a Fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
#     # Se aplica la fórmula de conversión de Fahrenheit a Celsius

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius)) 
    
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    print("Temperatura en Celsius:", fahrenheit_a_celsius(fahrenheit))
    



