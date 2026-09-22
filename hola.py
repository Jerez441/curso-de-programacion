def start_game():
    print("\n" + "="*50)
    print("EL CASTILLO DE AKENEA")
    print("\n" + "="*50)
    print("eres un joven aprendiz de mago enviado para recuperar un libro de hechizos de nombre EXCALIBUR,para ello te adentras en el castillo de akenea")
    print("Una vez dentro del castillo, un pilar te corta el paso")

    opcion1 = input("tienes dos maneras de pasar, ¿lo DESTRUYES con tu hechizo de fuego o BUSCAS otro camino?  ").lower()

    if opcion1 == "destruyes":
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("destruyes el pilar y encuentras un monton de dinero para comprar suministros y sigues tu camino con tranquilidad")

        print("--------------------------------------------------------------------------------------------------------------------------------------------")



    elif opcion1 == "buscas":
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("encuentras un camino que te lleva a la misma habitacion que bloqueaba el pilar,pero terminas descansando ya que era un camino largo y reanudas tu camino al dia siguiente")
        
        print("--------------------------------------------------------------------------------------------------------------------------------------------")



    else:
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("opcion no disponible,caes en una trampa y te pierdes en un laberinto")
        print("---------------------------------------------------------------------------------------------------------------------------------------------")


    opcion2 = input("encuentras dos botones en la pared, uno en la DERECHA y otro a tu IZQUIERDA ¿cual presionas?  ").lower()
    if opcion2 == "derecha":
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("¡AUCH! el boton deja caer unas pierdras sobre ti,esquivas algunas pero te lastimas considerablemente,sigues tu camino y hay un enemigo que no logras identificar")

        print("--------------------------------------------------------------------------------------------------------------------------------------------")

    elif opcion2 == "izquierda":
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("el boton abre una puerta secreta que te lleva a un cofre donde esta el tan ansiado libro EXCALIBUR,pero algo aparece en tu camino pero no logras verlo bien")

        print("--------------------------------------------------------------------------------------------------------------------------------------------")

    else:
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("opcion no disponible,caes en una habitacion donde hay un soldado que te ataca por la espalda y te deja inconsciente")

        print("---------------------------------------------------------------------------------------------------------------------------------------------")

    print("¡CUIDADO,ES UN DRAGON! te percatas de su presencia y piensas en tu siguiente movimiento")
    print("Encuentras un camino que te lleva a la salida pero debes maniobrar para pasar el dragon")

    opcion3 = input("¿Qué haces? CORRES al camino y te arriesgas a que el dragon te atrape o LUCHAS contra él?  ").lower()

    if opcion3 == "corres":
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("el dragon te atrapa y te quema dejandote exhausto y el libro excalibur en cenizas y no logras cumplir tu mision--FIN DEL JUEGO---")

        print("--------------------------------------------------------------------------------------------------------------------------------------------")

    elif opcion3 == "luchas":
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("¡FELICIDADES! logras derrotar el dragon y recuperas el libro EXCALIBUR,pero debes salir del castillo ya que se esta llenando de lava")

        print("--------------------------------------------------------------------------------------------------------------------------------------------")

    else:
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("opcion no disponible,el dragon te ataca y te deja inconsciente y el libro excalibur en cenizas y no logras cumplir tu mision--FIN DEL JUEGO---")

        print("--------------------------------------------------------------------------------------------------------------------------------------------")

    print("Espero que esta historia te haya gustado y nos vemos en alguna otra leyenda, gracias por jugar y recuerdad")
    print("--¡TU VALENTIA Y TU INTELIGENCIA DEFINIRAN TU DESTINO EN UN MAÑANA!--")

if start_game():
    pass