legajos   = [1000, 1000, 2000, 2000, 2300,3000]

apellidos = ["Perez", "Perez", "Gomez", "Gomez", "Lopez","Gimenez"]

sueldos   = [1000000, 1200000, 1500000, 1300000, 2000000,850000]

indice = 0
cant_elementos = len(legajos)

while indice < cant_elementos:
    legajo_actual = legajos[indice]
    apellido_actual = apellidos[indice]
    total = 0
    pagos = 0
    
    # Corte de control
    while indice < cant_elementos and legajos[indice] == legajo_actual:
        total += sueldos[indice]
        pagos += 1
        indice += 1
    
    promedio = total / pagos
        
    print("legajo: ", legajo_actual)
    print("apellido: ",apellido_actual)
    print("total sueldos: ", total)
    print("cantidad de pagos: ", pagos)
    print("promedio: ",promedio,"\n")