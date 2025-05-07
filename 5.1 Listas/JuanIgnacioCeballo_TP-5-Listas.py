# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

mult_4 = list(range(4, 101, 4))

print(mult_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

list_5 = ["hola", 96.25, True, -47.25, ["Raul", "juan"]]

print(list_5[3])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

noneList = []

noneList.append("Hola")
noneList.append("cómo")
noneList.append("va?")

print(noneList)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"];

print(animales);

animales[1] = "loro";
animales[3] = "oso";

print(animales);

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# La primera linea establece un array con número naturales como elementos
numeros = [8, 15, 3, 22, 7];

# La siguiente linea accede el método remove y a su vez a la función max que devuelve el número mayor dentro del array, en este caso 22
numeros.remove(max(numeros));

# Luego se imprime el resutlado
print(numeros);

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

list_5 = list(range(10, 31, 5));

print(list_5[0], list_5[1]);

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"];

print(autos);

autos[1] = "bora";
autos[2] = "passat";

print(autos);

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles = [];

for i in range(5, 16, 5):
    dobles.append(i*2);

print(dobles);

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: a) Agregar "jugo" a la lista del tercer cliente usando append. b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. c) Eliminar "pan" de la lista del primer cliente. d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]];

compras[2].append("jugo");
compras[1][1] = "tallarines";
compras[0].remove("pan");

print(compras);

# 10) Lista anidada

lista_anidada = [];

lista_anidada.append(15);
lista_anidada.append(True);
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False);

print(lista_anidada);





















