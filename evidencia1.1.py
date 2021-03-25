articulos={}
while True:
    print("\n\tMain menu")
    print("1-Registrar una venta")
    print("2-Consultar una venta")
    print("X-Salir ")
    opcion = input("Elige una opcion")
    if opcion =='1':
        monto_total=0
        print("Registrar")
        contador= max(articulos,default=0)+1
        articulos[contador]=[]
        while opcion !='0':
            descripcion = input(f"Escribe la descripcion de la venta {contador}: ")
            cantidad = int(input("Escribe la cantidad a comprar del articulo"))
            precio= float(input(f"Escribe el precio de piezas vendidas"))
            compra = (descripcion.upper(),cantidad,precio,cantidad*precio)
            monto_total=monto_total+cantidad*precio
            articulos[contador].append(compra)
            opcion=input("Escribe si deseas continuar (1-Continuar registrando/0-Dejar de registar: ")
        print(f"N° {contador}")
        for i in range(len(articulos[contador])):
            print(f"Descripcion: {articulos[contador][i][0]}\t {articulos[contador][i][1]}X ${articulos[contador][i][2]}\tMonto Total: {articulos[contador][i][3]}\n")
        print("\nMonto total a pagar: ",monto_total)
        input("<<ENTER>>")
        
    elif opcion=='2':
        total=0
        print("\n\tConsulta tus ventas\n")
        buscar=int(input("Introduce la descripcion a buscar sobre la venta"))
        if buscar in articulos:
            for consulta in articulos[buscar]:
                print(f"Descripcion: {consulta[0]}\t {consulta[1]}X ${consulta[2]}\tMonto Total: {consulta[3]}\n")
                total=total+consulta[3]
            print(f"Precio a pagar {total}")
        else:
            print("\n\tNo se ha encontrado dicho numero de venta")
        input("<<ENTER>>")
    elif opcion =='X':
        print("\nSaliendo...\n")
        break
    else:
        print("\n\nError vuelve a intentarlo\n\n")
        input("<<ENTER>>")
