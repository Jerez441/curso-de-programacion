# Mi programa de compras

productos = []
precios = []

mientras_tanto = True

while mientras_tanto:
    print("\n--- MENU ---")
    print("1. Agregar producto")
    print("2. Ver cesta")
    print("3. Eliminar producto")
    print("4. Ver total")
    print("5. Salir")
    
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Que vas a comprar?: ")
        costo = input("Cuanto cuesta?: ")
        
        # Guardamos en las listas
        productos.append(nombre)
        precios.append(float(costo))
        print("Listo, guardado!")

    elif opcion == "2":
        if len(productos) == 0:
            print("No has comprado nada todavia.")
        else:
            print("Tus productos:")
            pos = 1
            for p in productos:
                # Mostramos la posicion y el precio
                print(pos, "-", p, "($", precios[pos - 1], ")")
                pos = pos + 1

    elif opcion == "3":
        if len(productos) == 0:
            print("La cesta esta vacia")
        else:
            print("Productos en tu lista:")
            for i in range(len(productos)):
                print(i + 1, "->", productos[i])
            
            borrar = input("Ingresa el numero del que quieres borrar: ")
            num = int(borrar) - 1
            
            if num >= 0 and num < len(productos):
                print("Eliminado:", productos[num])
                productos.pop(num)
                precios.pop(num)
            else:
                print("Ese numero no existe en la lista")

    elif opcion == "4":
        # Sumamos los precios uno por uno
        total = 0
        for p in precios:
            total = total + p
        print("En total llevas gastado: $", total)

    elif opcion == "5":
        print("Chao!")
        mientras_tanto = False

    else:
        print("Esa opcion no vale, pon un numero del 1 al 5")
        