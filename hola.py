def start_game():

    # --- NIVEL 1 ---
    
    print("\n" + "="*50)
    print("EL CASTILLO DE AKENEA")
    print("\n" + "="*50)
    print("eres un joven aprendiz de mago enviado para recuperar un libro de hechizos de nombre EXCALIBUR,para ello te adentras en el castillo de akenea")
    print("Una vez dentro del castillo, un pilar te corta el paso")

    opcion = input("tienes dos maneras de pasar, ¿lo DESTROZAS con tu hechizo de fuego o BUSCAS otro camino?  ").upper()

    if opcion == "DESTROZAS":
       # --- NIVEL 2 --- Ruta al destruir el pilar
       print("\n" + "="*50)
       print("lo destruyes con tu hechizo de fuego y sigues tu camino de forma tranquila")
       print("Encuentras unos botones pero por aspecto,solo funcionan 3 de ellos")

       # --- NIVEL 3 --- Camino secreto

       print("\n" + "="*50)

       opcion = input("cada boton tiene un color, el primero es (VERDE,TURQUESA,ROJO) ¿cual presionas?   ").upper()

       print("\n" + "="*50)
       
       if opcion == "VERDE":
           print("el boton verde abre un camino secreto")
           print("sigues tu camino y llegas a una sala y hay tres cofres")

           opcion = input("uno es de ORO, el otro de PLATA y uno de BRONCE que es pequeño, ¿cual abres?  ").upper()

             # --- NIVEL 4 --- DESTINO DE LOS COFRES

           if opcion == "ORO":
               print("\n" + "="*50)
               print("El cofre de oro poseia un libro maldito que al leerlo, te convierte en un viejito,")
               print( "FIN DEL JUEGO BRO")
               print("No todo lo brillante es bueno ni aqui ni en la realidad -_-")
               print("\n" + "="*50)
           elif opcion == "PLATA":
               print("\n" + "="*50)
               print("El cofre de plata poseia otro libro de hechizos pero al agarrarlo")

               print("te teletransporta a otra dimension y te mata un zombie")

               print("FIN DEL JUEGO BRO")

               print("fuiste zombificado tu,ahora sigue tu PC")
               print("\n" + "="*50)
           elif opcion == "BRONCE":
               print("\n" + "="*50)
               print("BIEEEN! Encontraste el EXCALIBUR")

               print("FELICIDADES CUMPLISTE TU MISION")

               print("Incluso lo mas pequeño puede ser gigante,solo hay que darle la oportunidad")
               print("\n" + "="*50)
           else:
               print("\n" + "="*50)
               print("RESPUESTA NO VALIDA PARA LA AVENTURA")

               print("FIN DEL JUEGO BRO")

               print("La avaricia es mala bro,se bueno y escoge una de esas 3 opciones")
               print("\n" + "="*50)
       elif opcion == "TURQUESA":

           # ---- NIVEL 5 --- UN CAMINO ALGO COMESTIBLE
           
           print("\n" + "="*50)
           print("Pasas por un sendero que te lleva a una sala con tematica selvatica")
           print("hay 3 arboles con unos frutos diferentes cada uno,no sabes que son pero decides probar uno")

           opcion = input("¿Cual fruta de arbol comeras? el DERECHO, el IZQUIERDO o el de EN MEDIO   ").upper()
           print("\n" + "="*50)

           # --- NIVEL 6 --- DECISION ALGO RIESGOSA

           if opcion == "DERECHO":
               print("\n" + "="*50)
               print("Mueres envenenado y no traes ningun antidoto")

               print("FIN DEL JUEGO BRO")

               print("Vuelve a intentarlo")
               print("\n" + "="*50)
           elif opcion == "IZQUIERDO":
               print("\n" + "="*50)
               print("Al comer la fruta,te teletransporta al inicio... te da flojera empezar de cero y te vas")

               print("FIN DEL JUEGO BRO")

               print("Hasta a mi me daria flojera iniciar de nuevo,te entiendo... por ahora")
               print("\n" + "="*50)
           elif opcion == "EN MEDIO":
               print("\n" + "="*50)
               print("Te teletransporta a la sala donde esta el EXCALIBUR, MISION CUMPLIDA")

               print("FELICIDADES, LO LOGRASTE")

               print("Suertudo,escogiste la opcion buena")
               print("\n" + "="*50)
           else:
               print("\n" + "="*50)
               print("RESPUESTA INVALIDA,escoge otra cosa bro")
               print("\n" + "="*50)
       elif opcion == "AZUL":

           #--- nivel 7 --- CAMINO AZULADO OSCURO

           print("\n" + "="*50)
           print("Se abre un camino donde necesitas muchas llaves para abrir las puertas y avanzar")

           print("ademas de que varias habitaciones donde estan las llaves son submarinas")

           print("Logras avanzar sin problemas, y te toca luchar contra una version tuya oscura")
           print("\n" + "="*50)

           # --- NIVEL 8 --- BATALLA ¿DECISIVA?

           print("\n" + "="*50)
           opcion = input("¿Que haras para ganarle? ¿utilizaras tu HECHIZO DE FUEGO, Tu HECHIZO DE ENREDADERAS?   ").upper()
           print("\n" + "="*50)

           if opcion == "HECHIZO DE FUEGO":
               print("\n" + "="*50)
               print("Tu version oscura es inmune a todo,gracias a que absorbio tu hechizo")

               print("No puedes contraatacar y pierdes el combate")

               print("FIN DEL JUEGO BRO")
               print("\n" + "="*50)
           elif opcion == "HECHIZO DE ENREDADERAS":
               print("\n" + "="*50)
               print("logras acorralarlo y lo entierras en las profundidades")
               print("Desbloqueas una nueva habitacion y")

               print("FELICIDADES...")

               print("cumpliste la mision secundaria la cual era comprobar esa leyenda de tu version oscura")
               print("no consigues el excalibur pero aprendiste cosas y te vas a tu casas")
               print("\n" + "="*50)
           else:
               print("\n" + "="*50)
               print("RESPUESTA INVALIDA,INTENTALO DE NUEVO BRO")
               print("\n" + "="*50)
       elif opcion == "ROJO":

           # --- NIVEL 9 --- CAMINO CALIENTE PERO SEGURO

           print("\n" + "="*50)
           print("Se abre un camino,donde hay bastante lava pero el camino se divide en caminos con antorchas")
           print("Uno de los caminos con antorchas azules y el otro con antorchas rojas")
           print("\n" + "="*50)

           # --- NIVEL 10 --- UNA DECISION REVOLUCIONARIA

           print("\n" + "="*50)
           opcion = input("¿Que camino tomas, El de las antorchas AZULES o las antorchas ROJAS?  ").upper()
           print("\n" + "="*50)

           if opcion == "AZULES":
               print("\n" + "="*50)
               print(" llegas a una habitacion llena de magia, y te quedas mirando a los alrededores")

               print("Hay sillas volando,animales raros y mecanismos que no han descubierto")

               print("Te das cuenta de este lugar lleno de revelaciones y decidas dar por concluida la expedicion")
               print("FIN DEL JUEGO BRO")
               print("\n" + "="*50)
           elif opcion == "ROJAS":
               print("\n" + "="*50)
               print("El camino rojo te lleva a una cueva donde el calor te hace desmayarte y no traes agua contigo")

               print("Mueres de deshidratacion y llegaste lejos pero no lo suficiente...")

               print("FIN DEL JUEGO BRO")
               print("\n" + "="*50)
           else:
               print("\n" + "="*50)
               print("RESPUESTA INVALIDA,VOLVE A INTENTARLO")
               print("\n" + "="*50)
       else:
           print("\n" + "="*50)
           print("escoges un boton incorrecto y la habitacion explota")

           print("FIN DEL JUEGO BRO")

           print("¿Hiciste kabum kabum no?")
           print("\n" + "="*50)
    elif opcion == "BUSCAS":

        # --- NIVEL 11 --- UN PRUEBA DE CORAZON PURO

        print("\n" + "="*50)
        print("encuentras un sendero mucho mas largo que te lleva a un ojo misterioso que te hace una pregunta")
        print("estas un poco asustado pero decides hacerle caso")
        print("\n" + "="*50)


        print("\n" + "="*50)
        opcion = input("¿Que es lo mas importante en el mundo segun tu, el DINERO, la FAMILIA o CONOCERSE a si mismo?   ").upper()
        print("\n" + "="*50)

        if opcion == "DINERO":

            print("\n" + "="*50)
            print("el ojo te responde y te dice: mnnnn que mente tan vaga ¿solo te importa lo material no?")

            print("\n" + "="*50)

            print("\n" + "="*50)
            print("te mata de un rayo laser y hasta ahi llegaste pum")
            print("FIN DEL JUEGO BRO")
            print("no se proyecten aqui please")

            print("\n" + "="*50)
        elif opcion == "FAMILIA":

            print("\n" + "="*50)
            print("el ojo te responde y te dice : mnnnn no me gusta pero no me desagradas,puedes seguir tu camino")
            print("sigues tu camino y encuentras el EXCALIBUR un una habitacion y cumples tu mision")
            print("FELICIDADES,CUMPLISTE TU MISION")
            print("\n" + "="*50)
        elif opcion == "CONOCERSE":
            print("\n" + "="*50)
            print("el ojo te responde: mnnnn me encanta esa mentalidad tuya,toma lo que tanto ansiabas")
            print("consigues el EXCALIBUR y cumples tu mision")
            print("FELICIDADES MISION CUMPLIDA")
            print("conocerse es clave para estar tranquilo en esta vida")
            print("\n" + "="*50)
        else:
            print("OPCION INVALIDA,INTENTA DE NUEVO")
    else:
        print("OPCION INVALIDA,try again")

# Iniciar el programa
if __name__ == "__main__":
    start_game()
               
           
       

           
