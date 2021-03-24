articulos={}

while True:
    print("\n\tMain menu")
    print("1-Registrar una venta")
    print("2-Consultar una venta")
    print("X-Salir ")
    opcion = input("Elige una opcion")
    if opcion =='1':
        print("Registrar")
        contador= max(articulos,default=0)+1
        descripcion = input(f"Escribe la descripcion del articulo {contador}")
        cantidad = int(input("Escribe la cantidad a comprar del articulo"))
        precio= float(input(f"Escribe el precio de piezas vendidas"))
        articulos[contador]=[descripcion.upper(),cantidad,precio,cantidad*precio]
        print(f"\nN° {contador} de Ventas\nDescripcion: {descripcion}\t {cantidad}X ${precio}\tMonto Total: {cantidad*precio}\n")
        input("<<ENTER>>")
    elif opcion=='2':
        print("\n\tConsulta tus ventas\n")
        buscar=input("Introduce la descripcion a buscar sobre la venta")
        lista = [i for i in articulos if buscar.upper()==articulos[i][0]]
        if len(lista)!=0:
            for registro in lista:
                print(f"N° {registro} de Ventas\nDescripcion: {articulos[registro][0]}\t {articulos[registro][1]}X ${articulos[registro][2]}\tTotal: {articulos[registro][3]}")
        else:
            print("\nNo se ha encontrado ninguna venta\n")
            input("<<ENTER>>")
    elif opcion =='X':
        print("\nSaliendo...\n")
        break
    else:
        print("\n\nError vuelve a intentarlo\n\n")
        input("<<ENTER>>")

'''
def registrar(articulos):
    print("Registrar")
    contador= max(articulos,default=0)+1
    descripcion = input(f"Escribe la descripcion del articulo {contador}")
    cantidad = int(input("Escribe la cantidad a comprar del articulo"))
    precio= float(input(f"Escribe el precio de piezas vendidas"))
    articulos[contador]=[descripcion,cantidad,precio,cantidad*precio]
    print(f"\nN° {contador} de Ventas\nDescripcion: {descripcion}\t {cantidad}X ${precio}\tTotal: {cantidad*precio}\n")
    input("<<ENTER>>")
    return articulos

def consultar(articulos):
    print("\n\tConsulta tus ventas\n")
    buscar=input("Introduce la descripcion a buscar sobre la venta")
    lista = [i for i in articulos if buscar==articulos[i][0]]
    if len(lista)!=0:
        for registro in lista:
            print(f"N° {registro} de Ventas\nDescripcion: {articulos[registro][0]}\t {articulos[registro][1]}X ${articulos[registro][2]}\tTotal: {articulos[registro][3]}")
    else:
        print("\nNo se ha encontrado ninguna venta\n")
        input("<<ENTER>>")
'''
