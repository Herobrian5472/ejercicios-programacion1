vendedor = int(input("\n\nIngrese al vendedor: "))

ventas = 0
total = 0
vendedores = 0

lista_vendedores = []
lista_montos = []

while vendedor != 99:
    
    vendedor_actual = vendedor
    monto = 0
    movimientos = 0
    
    while vendedor_actual == vendedor:
        
        
        print("__________________")
        print("\nVendedor: ",vendedor_actual)
        venta = float(input("De cuánto fue la venta: $"))
        monto += venta
        movimientos += 1
        lista_vendedores.append(vendedor)
        lista_montos.append(monto)
        vendedor = int(input("\nIngrese al vendedor: "))
    
    print("===================")    
    print("Vendedor: ",vendedor_actual)
    print("Ventas: ",movimientos)
    print("Total: ",monto)
    print("===================")   
    
    ventas += movimientos
    total += monto
    vendedores += 1
    
print("\n\n===================")
print("Fin de las ventas.\n")    
print(f'Se realizaron un total de {ventas} ventas')
print(f'Por un monto total de ${total}')
print(f'Entre {vendedores} vendedores')
print("===================")  

print(lista_vendedores)
print(lista_montos)
    