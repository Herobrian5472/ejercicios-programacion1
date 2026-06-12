'''
Ejercitacion para trabajar sobre txt p linea por linea

Programa en bucle con funciones que:

1. Muestre las frases (lineas) existentes

2. Agregue una frase (linea al final)

3. Elimine la ultima frase (ultima linea)

4. Borrar todo


'''

print(f"================================\n"
      f"Bienvenido a su diario de frases\n"
      f"================================\n")

while True:

    
    print(f"\n¿Qué desea hacer?\n"
      f"1. Mostrar frases\n"
      f"2. Agregar una frase\n"
      f"3. Leer última frase\n"
      f"4. Borrar todas las frases\n"
      f"5. Borrar solo la última\n"
      f"6. Salir\n")

    opcion = int(input("\nElija una opción: "))

    if opcion == 1:
        with open(r'C:\Users\Brian\Downloads\Archivos\frases.txt', 'r') as archivo_de_texto: # 'r' lee
            print("\n")
            for linea in archivo_de_texto.readlines():
                print(linea.strip())
                # no hace falta continue (el for al terminar continua con el bucle)
                    
    elif opcion == 2:
        frase = input("Escribe una frase: ")

        with open(r'C:\Users\Brian\Downloads\Archivos\frases.txt', 'a') as archivo_de_texto: # 'a' es de append (agrega como en listas)
            
            archivo_de_texto.write(frase + '\n')

    elif opcion == 3:
        with open(r'C:\Users\Brian\Downloads\Archivos\frases.txt', 'r') as archivo_de_texto:
        
            lineas = archivo_de_texto.readlines()
            print(lineas[-1].strip()) # imprime solo la última (-1)

    elif opcion == 4:
        with open(r'C:\Users\Brian\Downloads\Archivos\frases.txt', 'w') as archivo_de_texto: # 'w' sobreescribe sobre todo el txt
            pass # sale sin hacer más nada, deja el txt en blanco

    elif opcion == 5:
        with open(r'C:\Users\Brian\Downloads\Archivos\frases.txt', 'r') as archivo_de_texto:
        
            lineas = archivo_de_texto.readlines()

        lineas.pop() # esto explota si no hay más lineas, usar if len(lineas) > 0:

        with open(r'C:\Users\Brian\Downloads\Archivos\frases.txt', 'w') as archivo_de_texto:
            
            archivo_de_texto.writelines(lineas)
            print("última frase eliminada.\n")

    elif opcion == 6:
        print("¡Adiós!")
        break

    else:
        print("Opción no válida.\n")
        continue



'''

-----------------------------------------------------------------------------------

OK, ahora crear funciones, una para cada opcion y luego un menú

'''