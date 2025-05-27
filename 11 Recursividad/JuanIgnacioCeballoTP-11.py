def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
def valida_entero(mensaje, min = float("-Inf"), max = float("Inf")):
    num = int(input(f"{mensaje}"))
    while num < min or num > max:
        num = int(input(f"Por favor, {mensaje}"))
    return num

def potencia(b,e):
    if e == 1:
        return b
    elif e == 0:
        return 1
    else:
        return b * potencia(b, e-1)
    
def decimalABinario(num):
    if num == 0:
        return "0"
    else:
        return decimalABinario(num // 2) + str(num % 2)
    
def es_palindromo(palabra):
    if len(palabra) == 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
def palabra_simple(palabra):
    tildes = "áÁéÉíÍóÓúÚ"
    for i in palabra:
        if i in tildes or i == " ":
            return False
    return True

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return suma_digitos(num//10) + int(num % 10)
    
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return contar_bloques(n-1) + int(n)
    
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    resto = numero % 10
    if resto == digito:
        return contar_digito(numero // 10, digito) + 1
    else:
        return contar_digito(numero // 10 , digito)
    


# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

num_fact = valida_entero("Ingrese un número entero positivo: ", 0)

for i in range(0, num_fact+1):
    print(f"El factorial de {i} es {factorial(i)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

fibo = valida_entero("Ingrese la posición de la serie Fibonacci: ", 0)

for i in range(0, fibo+1):
    print(fibonacci(i))

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente.

base = valida_entero("Ingrese la base de la potencia: ")
exponente = valida_entero("Ingrese el exponente de la potencia: ", 0)

print(f"{base} elevado a {exponente} es {potencia(base,exponente)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
## En este caso tuve que buscar la solución porque no sabía como resolverlo

decimal = valida_entero("Ingrese el número decimal que desea convertir a binario: ")

print(f"{decimal} base 10 es igual a {decimalABinario(decimal)} base 2")


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

palabra = input("Ingrese una palabra sin tildes ni espacios: ")

while palabra_simple(palabra) == False :
    palabra = input("Por favor, ingrese una palabra sin tildes ni espacios: ")

if es_palindromo(palabra):
    print(f"{palabra} si es un palindromo")
else:
    print(f"{palabra} no es un palindromo")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.


num_dig = valida_entero("Ingrese un número entero positivo: ", 0)

print(f"La suma de los dígitos de {num_dig} es: {suma_digitos(num_dig)}")


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.


bloques = valida_entero("Ingrese la cantidad de bloques que utilizara para la base de la pirámide: ")

print(f"Para una pirámide con {bloques} bloques de base, se necesitan {contar_bloques(bloques)} bloques para su construcción")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

num = valida_entero("Ingrese un número entero positivo: ", 0)
digit = valida_entero("Ingrese el dígito del cual desea saber las veces que se repite en le número: ", 0)

print(f"{contar_digito(num, digit)}")



