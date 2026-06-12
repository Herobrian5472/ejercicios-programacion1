# Pedimos un primer legajo
while True:
    legajo = int(input("\n\nIngrese el legajo: "))
    
    if legajo == 0: # El primer legajo debe ser válido para que no rompa el promedio final
        print("Debe ingresar un primer legajo para iniciar.\n")
        continue
    
    if legajo != 0:
        break

# Variables para el promedio final
suma_sueldos = 0
cant_empleados = 0

while legajo != 0:
    
    legajo_actual = legajo
    suma = 0 # Por empleado
    cant_empleados += 1 # Para calcular el promedio final
    
    while legajo_actual == legajo:
        
        apellido = str(input("Ingrese el apellido: ").capitalize())
        sueldo = float(input("Ingrese el sueldo: $"))
        suma += sueldo
        
        print("Legajo: ",legajo)
        print("Apellido: ",apellido)
        print("Suelto ingresado: $",sueldo)
        
        legajo = int(input("Ingrese el nuevo legajo: "))
    
    suma_sueldos += suma
            
    print(f'\n======================\n'
          f'Resumen de: {apellido}\n'
          f'Legajo: {legajo_actual}\n'
          f'La suma de sus sueldos es :${suma}\n'
          f'======================\n')
    

promedio = suma_sueldos / cant_empleados    
    
print(f'\n======================================================\n'
      f'Se ingresó un total de {cant_empleados} empleados.\n'
      f'Todos sus sueldos dieron la suma de ${suma_sueldos}.\n'
      f'Y el promedio de sueldo por empleado es de ${promedio}.\n')