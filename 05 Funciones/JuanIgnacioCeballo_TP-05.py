import math

def hola_mundo():
    saludo = "Hola Mundo"
    return saludo

def nombre(mensaje):
    nombre = input(mensaje)
    return f"Hola {nombre}!"


def personal_inf(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

def valida_entero(mensaje, min = float("-Inf"), max = float("Inf")):
    num = int(input(f"{mensaje}"))
    while num < min or num > max:
        num = int(input(f"Por favor, {mensaje}"))
    return num

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area 

def calcular_perimetro_circulo(radio):
    perimetro = math.pi * radio * 2
    return perimetro

def segundos_a_horas(segundos):
    return segundos / 3600


def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{numero} x {i} = {numero*i} \n")

def operaciones_basicas(a, b):
    suma = f"Suma entre {a} y {b} es igual a {a + b}"
    resta = f"Resta entre {a} y {b} es igual a {a - b}"
    mult = f"Multiplicacion entre {a} y {b} es igual a {a * b}"
    if b == 0:
        division = "No se puede hacer division por 0"
    else:
        division = f"División entre {a} y {b} es igual a {a / b}"

    resultado = (suma, resta, mult, division)
    return resultado

def calcular_imc(peso, altura):
    return peso / (altura**2)

def celsius_a_fahrenheit(celsius):
    fahr = (celsius * 9/5) + 32
    return fahr


def calcular_promedio(a, b, c):
    return (a + b + c)/3



# Main 

# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

print(hola_mundo())

# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.

print(nombre("Ingrese su nombre: "))

# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.

nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
edad = valida_entero("Ingrese su edad: ", 0)
res = input("Ingrese su lugar de residencia: ")

print(personal_inf(nom, ape, edad, res))

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

radio = float(input("Ingrese el radio del círculo: "))

print(f"El área del círculo es de {calcular_area_circulo(radio)} y su perimetro es de {calcular_perimetro_circulo(radio)}")

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

sec = valida_entero("Ingrese la canitdad de segundos para devolver su equivalente en horas: ", 0)

print(f"{sec} segundos equivale a {segundos_a_horas(sec)} horas") 

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.

num_tabla = int(input("Ingrese un número para saber su tabla de multiplicar: "))

tabla_multiplicar(num_tabla)


# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

a = float(input("Ingrese el primer número a operar: "))
b = float(input("Ingrese el segundo número a operar: "))

operaciones = operaciones_basicas(a, b)

for operacion in operaciones:
    print(operacion)


# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("INgrese su altura en métros: "))

print(f"Su indice de masa corporal es de {calcular_imc(peso, altura)}")


# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.

cel = float(input("Ingrese la temperatura en grados celcius: "))

fahr = celsius_a_fahrenheit(cel)

print(f"{cel}º celsius equivalen a {fahr}º fahrenheit")


# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.

nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

print(f"El promedio de las notas ingresadas es: {calcular_promedio(nota1, nota2, nota3)}")




