'''

#############-README-################

Ejercitacion para trabajar sobre txt linea por linea
**Programa en bucle con funciones que:

1. Muestre las frases (lineas) existentes
2. Agregue una frase (linea al final)
3. Lea la ultima frase
4. Elimine la ultima frase (ultima linea)
5. Borrar todo
6. Salir

_______________________________________________________________________________________________________________________________________________________________________________________________________________________

-Todo lo anterior está encapsulado en funciones y un menú que tambien es una función.

-Jugué con time para hacer una espera visual al crear un nuevo txt.

-Aprendí a usar try y except para controlar errores, descubrí que cuando no encontraba la ruta me devolvía el error FileNotFoundError, así que lo usé para crear un nuevo archivo cuando no encontrara frases.txt

_______________________________________________________________________________________________________________________________________________________________________________________________________________________

Entonces, para que quede claro el tema de abrir un .txt para trabajar sobre él:
    también pueden ser archivos .csv .json .py .html (porque todos son texto)

with open() sirve para trabajar con un archivo
    dentro de sus paréntesis van la ruta y el modo de lectura ('a', 'r', 'w')
        'a' = append (agregar al final)
        'r' = read (leer)
        'w' = write (escribir, esto borra lo que existe dentro, es decir, sobreescribe)

as es como decir "nombralo como variable"

entonces cuando decimos:
    with open(ruta, 'r') as archivo:
    # estamos diciendo: abre el archivo ubicado en ruta con modo lectura y nombralo como variable archivo.
    
luego usamos .readlines() para que lea todo el archivo, linea por linea
    lineas = archivo.readlines()
    # creamos una variable a la que llamamos "lineas" y guardamos en ella todas las líneas del archivo
        linea.strip() elimina los saltos de linea, para que el print en la consola quede más limpio (funciona igual si no se usa)

y si usamos .write estamos escribiendo dentro del archivo, pero tener en cuenta de usar 'a' para agregar y 'w' para sobreescribir todo
    with open(ruta, 'w') as archivo: # lo abre en modo escritura y borra lo que había dentro
        pass # dejamos el archivo vacío (pass mantiene válido el bloque aunque no haga nada)
        
    with open(ruta, 'a') as archivo: # lo abre en modo append
        archivo.write("Si el programa funciona no lo toques") # esto agrega la linea escrita dentro del () al final del archivo sin borrar lo anterior
                
_______________________________________________________________________________________________________________________________________________________________________________________________________________________

'''

import time # Para jugar con tiempos de espera ficticios

ruta = r'C:\Users\brian\Escritorio\Github\ejercicios-programacion1\frases.txt' # Puedo usar solo ruta = 'frases.txt' y el programa buscará el archivo en la misma carpeta del .py

# Funcion para mostrar las frases existentes en el txt
def mostrar():
    try:
        with open(ruta, 'r') as archivo_de_texto: # 'r' lee
            print("\n")

            lineas = archivo_de_texto.readlines()

            if len(lineas) > 0:
                for linea in lineas:
                    print(linea.strip())
                    # no hace falta continue (el for al terminar continua con el bucle)

            else:
                print("No hay frases guardadas.\n")
                
    except FileNotFoundError:
        print("No existe un cuaderno de frases.\n")
        print("Creando un nuevo cuaderno de frases, espere un momento...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("3...")
        with open(ruta, 'w') as archivo_de_texto:
            pass # sale sin hacer más nada, deja el txt en blanco
        print("\nSe acaba de crear un cuarderno de frases en blanco.\n")

# Funcion para agregar una nueva frase al final de las existentes
def agregar():
    frase = input("Escribe una frase: ")
    with open(ruta, 'a') as archivo_de_texto: # 'a' es de append (agrega como en listas)
        archivo_de_texto.write(frase + '\n')

# Funcion que lee la última frase existente en el txt
def leer_ultima():
    with open(ruta, 'r') as archivo_de_texto:
        lineas = archivo_de_texto.readlines()
        if len(lineas) > 0:
            print(lineas[-1].strip()) # imprime solo la última (-1)

        else:
            print("No hay frases guardadas.\n")

# Funcion que borra todo dentro del txt
def limpiar():
    with open(ruta, 'w') as archivo_de_texto: # 'w' sobreescribe sobre todo el txt
        pass # sale sin hacer más nada, deja el txt en blanco

# Funcion que borra solo la ultima frase (linea)
def borrar_ultima():
    with open(ruta, 'r') as archivo_de_texto:
        lineas = archivo_de_texto.readlines() # creamos la variable donde guardamos las lineas del archivo

    if len(lineas) > 0: # verificamos que existan líneas antes de usar pop()
        lineas.pop() # elimina la ultima linea de la variable lineas
        with open(ruta, 'w') as archivo_de_texto: # recordar que 'w' sobreescribe, borra lo que habia y escribe lo siguiente:
            archivo_de_texto.writelines(lineas) # escribe todas las lineas que hay en la variable lineas (menos la ultima que borró)
            print("última frase eliminada.\n")

    else:
        print("No hay frases guardadas.\n")

# Menu con opciones
def main():
    while True:
        print(f"\n¿Qué desea hacer?\n"
        f"1. Mostrar frases\n"
        f"2. Agregar una frase\n"
        f"3. Leer última frase\n"
        f"4. Borrar todas las frases\n"
        f"5. Borrar solo la última\n"
        f"6. Salir\n")
        
        while True:
            try:    # por si escribe string
                opcion = int(input("\nElija una opción: "))
                break
            except ValueError:
                print("Debe ingresar una opción numérica.\n")
                continue

        if opcion == 1:
            mostrar()
            
        elif opcion == 2:
            agregar()
            
        elif opcion == 3:
            leer_ultima()

        elif opcion == 4:
            limpiar()

        elif opcion == 5:
            borrar_ultima()

        elif opcion == 6:
            print("¡Adiós!")
            break

        else:
            print("Opción no válida.\n")
            continue

print(f"================================\n"
      f"Bienvenido a su diario de frases\n"
      f"================================\n")

main()

print("Vuelva pronto ♥")
