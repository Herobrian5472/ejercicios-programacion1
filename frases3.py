'''
Importamos os y luego usamos la funcion remove para eliminar el archivo completo
'''



import time # Para jugar con tiempos de espera ficticios
import os

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
        
def eliminar():
    try:
        os.remove(ruta)
        print(ruta, " removido.\n")
        
    except FileNotFoundError:
        print("No hay archivos para eliminar.")

# Menu con opciones
def main():
    while True:
        print(f"\n¿Qué desea hacer?\n"
        f"1. Mostrar frases\n"
        f"2. Agregar una frase\n"
        f"3. Leer última frase\n"
        f"4. Borrar todas las frases\n"
        f"5. Borrar solo la última\n"
        f"6. Eliminar archivo de frases\n"
        f"7. Salir\n")
        
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
            eliminar()

        elif opcion == 7:
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