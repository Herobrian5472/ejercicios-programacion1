# Archivo del profesor que contiene [legajo, precio de venta]
ruta = 'archivo.txt'

lista_ventas = []
vendedores = []
precios_ventas = []

try:
    # abrir el archivo .txt
    with open(ruta, 'r') as archivo_de_texto: # 'r' lee
        # recorrer lineas
        lineas = archivo_de_texto.readlines()
        # siempre que haya lineas para leer
        if len(lineas) > 0:
            for linea in lineas:
                lista_ventas.append((linea.strip()).split(',')) # agregar la linea a la lista, separando con la coma el vendedor y precio de venta
                print((linea.strip()).split(',')) # mostrar en consola esa linea
                venta = linea.strip().split(',') # creo la variable venta con el precio
                vendedor = venta[0] # la variable vendedor con el legajo
                precio = venta[1] # precio de la venta
                vendedores.append(vendedor) # agrego a la lista vendedores el vendedor (legajo)
                precios_ventas.append(precio) # agrego a la lista de ventas el precio de la venta

        # Si el archivo está vacío
        else:
            print("no hay movimientos en archivo.txt.\n")
            
except FileNotFoundError:
    print("no existe archivo.txt\n")

# mostrar en consola los vendedores (legajos)
for i in vendedores:
    print(i)

#mostrar en consola las ventas (precios)
for i in precios_ventas:    
    print(i)

# ==========================
# CORTE DE CONTROL
# =========================

indice = 0
cant_elementos = len(vendedores)

# variable de archivo nuevo
resumen = 'resumen_ventas.txt'
# lo creamos porque no existe
with open(resumen, 'w') as archivo_nuevo:
    pass 

while indice < cant_elementos:
    vendedor_actual = vendedores[indice]
    total = 0
    movimientos = 0

    while indice < cant_elementos and vendedores[indice] == vendedor_actual:
        venta_actual = float(precios_ventas[indice])
        total += venta_actual
        movimientos += 1
        indice += 1

    # mostramos en consola la suma de ventas por vendedor
    print("vendedor actual: ", vendedor_actual)
    print("total vendido: $", f"{total:.2f}")
    print("cantidad de movimientos: ",movimientos,"\n")

    # por cada vuelta agrega lo mostrado en consola al archivo nuevo
    with open(resumen, 'a') as archivo_de_texto: # 'a' es de append (agrega como en listas)
        archivo_de_texto.write("vendedor: " + vendedor_actual + '\n')
        archivo_de_texto.write("total vendido: " + f"{total:.2f}" + '\n')
        archivo_de_texto.write("ventas realizadas: " + str(movimientos) + '\n')
        archivo_de_texto.write("=============================" + '\n')


'''
##################################################
Usar este ejemplo para corregirlo:
##################################################

with open("viajes.txt", "r") as archivo:

    linea = archivo.readline().strip()

    mayor_recaudacion = 0
    empresa_mayor = ""
    viajes_empresa_mayor = 0

    while linea != "":

        datos = linea.split(",")

        cod_actual = int(datos[0])
        nom_actual = datos[1]

        total_viajes = 0
        total_recaudacion = 0

        # Corte de control
        while linea != "":

            datos = linea.split(",")

            codigo = int(datos[0])

            if codigo != cod_actual:
                break

            viajes = int(datos[2])
            recaudacion = float(datos[3])

            total_viajes += viajes
            total_recaudacion += recaudacion

            linea = archivo.readline().strip()

        print("Empresa:", nom_actual)
        print("Cantidad de viajes:", total_viajes)
        print("Recaudación total:", total_recaudacion)
        print("---------------------------")

        if total_recaudacion > mayor_recaudacion:
            mayor_recaudacion = total_recaudacion
            empresa_mayor = nom_actual
            viajes_empresa_mayor = total_viajes

    print("\nEMPRESA CON MAYOR RECAUDACIÓN DEL MES")
    print("Empresa:", empresa_mayor)
    print("Cantidad de viajes:", viajes_empresa_mayor)
    print("Recaudación:", mayor_recaudacion)



#####################################################################################################################################################################################
    El problema con corte.py es que crea listas cuando no son necesarias, la idea es traer la información para mostrarla en la consola sin antes tener que guardarla en memoria
#####################################################################################################################################################################################

    '''





