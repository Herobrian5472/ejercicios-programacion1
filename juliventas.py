vendedor = [1,1,2,2,2,3,3,3]
montos = [10,20,30,40,50,50,70,100]

indice = 0
cant_elementos = len(vendedor)

while indice < cant_elementos:
    vendedor_actual = vendedor[indice]
    total = 0
    movimientos = 0
    
    # Corte de control
    while indice < cant_elementos and vendedor[indice] == vendedor_actual:
        total += montos[indice]
        movimientos += 1
        indice += 1
        
    print("vendedor: ", vendedor_actual)
    print("total vendido: ", total)
    print("cantidad de movimientos: ", movimientos,"\n")