# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "));

if edad > 18:
    print("Es mayor de edad");

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Por favor, ingrese su nota: "));

if nota >= 6:
    print("Aprobado");
else:
    print("Desaprobado");

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = float(input("Ingrese un número: "));

if num % 2 == 0:
    print("Ha ingresado un número par");
else:
    print("Por favor, ingrese un número par");

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "));

if edad >= 0 and edad < 12:
    print("Niño/a");
elif edad >= 12 and edad < 18:
    print("Adolescente");
elif edad >= 18 and edad < 30:
    print("Adulto/a joven");
elif edad >= 30:
    print("Adulto");
else:
    print("Por favor, ingrese una edad correcta");

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

password = str(input("Ingrese contraseña: "));

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta");
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres");

# 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random 
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)];

for i in numeros_aleatorios:
    print(i);

moda = mode(numeros_aleatorios);
mediana = median(numeros_aleatorios);
media_aritmetica = mean(numeros_aleatorios);

print(f"Moda del conjunto: {moda}");
print(f"Mediana del conjunto: {mediana}");
print(f"Media aritmética del conjunto: {media_aritmetica}");

if media_aritmetica == moda == mediana:
    print("El conjunto de números no tiene sesgo");
elif media_aritmetica > mediana > moda:
    print("el conjunto de números posee Sesgo positivo");
elif media_aritmetica < mediana < moda:
    print("el conjunto de números posee Sesgo negativo");
else:
    print("No se puede definir el sesgo");

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

vowels = ["a", "e", "i", "o", "u"];

palabra = str(input("Ingrese un palabra o frase: "));

palabra = list(palabra);

ult = len(palabra);

if palabra[ult-1] in vowels:
    palabra.append("!");

palabra = "".join(palabra);

print(palabra); 

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingrese su nómbre: "));
opt = int(input("Elija una opción:\n 1. Si quiere su nombre en mayúsculas\n 2. Si quiere su nombre en minúsculas\n 3. Si quiere su nombre con la primera letra mayúscula."));

if opt == 1:
    nombre = nombre.upper();
elif opt == 2:
    nombre = nombre.lower();
elif opt == 3:
    nombre = nombre.title();
else:
    print("Por favor, ingrese una opción correcta");

print(nombre);


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: Menor que 3: "Muy leve" (imperceptible). Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

richter = float(input("Ingrese la magnitud del terremoto: "));

if richter < 3 and richter > 0:
    print('"Muy leve" (imperceptible)');
elif richter >= 3 and richter < 4:
    print('"Leve" (ligeramente perceptible)');
elif richter >= 4 and richter < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)');
elif richter >= 5 and richter < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)');
elif richter >= 6 and richter < 7:
    print('"Muy Fuerte" (puede causar daños significativos)');
elif richter >= 7 and richter < 10:
    print('"Extremo" (puede causar graves daños a gran escala)');
else:
    print("Error: Fuera de rango");

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

h = ["N", "S"];

hemisferio = str((input("Ingrese el hemisferio en el que se encuentra (N/S): "))).upper();

if not hemisferio in h:
    print("Por favor, ingrese el hemisferio correcto (N/S)");

mes = int(input("Ingrese el mes (valor numérico): "));
dia = int(input("Ingrese el día: "));

m30 = [4, 6, 9, 11];

m31= [1, 3, 5, 7, 8, 10, 12];

m31Verdadero = False;
m30Verdadero = False;
febrero = False;


if (mes in m31 and (dia > 0 and dia <=31 )):
    m31Verdadero = True;

if (mes in m30 and (dia > 0 and dia <= 30)):
    m30Verdadero = True;

if (mes == 2 and (dia > 0 and dia <=28)):
    febrero = True;



if ((m31Verdadero or m30Verdadero) or febrero) and ((mes == 12 and dia >= 21) or (mes in[1, 2]) or (mes == 3 and dia <= 20)):
    if hemisferio == "N":
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Invierno");
    else:
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Verano");
elif (m31Verdadero or m30Verdadero) and ((mes == 3 and dia >= 21) or (mes in[4, 5]) or (mes == 6 and dia <=20)):
    if hemisferio == "N":
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Primavera");
    else:
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Otoño");
elif (m31Verdadero or m30Verdadero) and ((mes == 6 and dia >= 21) or (mes in[7, 8]) or (mes == 9 and dia <= 20)):
    if hemisferio == "N":
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Verano");
    else:
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Invierno");
elif (m31Verdadero or m30Verdadero) and ((mes == 9 and dia >= 21) or (mes in[10, 11]) or (mes == 12 and dia <= 20)):
    if hemisferio == "N":
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Otoño");
    else:
        print(f"{dia} del {mes} en el hemisferio {hemisferio}, la estación es Primavera");
else:
    print("Error fecha erronea");