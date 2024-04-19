#Crear presentación para que el usuario interaccione con la lista de juegos disponibles y se inscriba como jugador.
# Cargar módulos necesarios en el código de los juegos:
import os               #  os proporciona funciones para interacturar con el archivo o el sistema operativo.
import random           #  radom para generar funciones que impliquen elementos aleatorios.



#Crear una clase donde los métodos permitirán al usuario interactuar con el juego.

class Juegos:
#Definir los parametros nombre y equipo:
  def __init__(self,nombre,equipo):
      
      self.nombre = nombre
      self.equipo = equipo
      pass

#Este método menu, permite al usuario interactuar con la lista de juego
  def menu(self):


    # Definimos una presentación gráfica del juego mediante el método print()
    
    self.figura_menu_inicio()  #imprimimos rotulo definido -lin-
    #Ofrecemos al usuario la lista de juegos disponibles:


    print("Listado de juegos")
    print("")
    print("  1. Preguntas y respuestas")
    print("  2. Ahorcado")
    print("  3. Piedra,papel o tijera")
    print('')
    print('  4. Reglas de los juegos')
    print("  5. Salir")
    print("")
    print("")

    print("================================================")

#indicar al jugador que seleccione un juego con la función input()
#El jugador, debe indicar el dígito asociado a cada juego:1,2,3
#O 4 y 5 para las reglas y salir del juego
    
    seleccion=input(f"{nombre} elige uno de los juegos (1,2,3 o 4 reglas y 5 salir):  ")

#crear una sentencia de control asociada a una funcion de cada juego:
#cada condición llama a la función del juego seleccionado.

   
    if seleccion =="1":
        self.preguntas_y_respuestas(nombre)
   
    elif seleccion == "2":
        self.ahorcado(nombre)
            
    elif seleccion =="3":
        self.piedra_papel_tijera(nombre)


    elif seleccion =="4":
        self.reglas_juego()    

    #Le damos la opción al jugador de salir del juego.
    #Esta función nos saca de la consola.
    elif seleccion =="5":      
        self.salir()      

   
    else:
        print("No has elegido una opción valida") 

#Definir los parámetros del juego Ahorcado:

  def ahorcado(self,nombre):
    intentos=10
    acierto=False
    palabra_aleatoria=""
    palabra_guiones=''
    lista_palabra=''
    lista_guiones=''
    palabra_jugada=''
    letra_usada=[]
    letra=''
    palabras_aleatorias = [
      "perro", "gato", "casa", "coche", "mesa", "silla", "libro", "computadora", "planta",
      "ciudad", "pared", "puerta", "ventana", "reloj", "manzana",
      "banana", "naranja", "fresa", "uva", "kiwi",  "piña", "papaya",
      "nube", "sol", "luna", "estrella", "mar", "océano", "lago", "montaña", "colina",
      "valle", "pradera", "desierto", "playa", "arena", "roca", "nieve", "hielo", "fuego", "viento"   
    ]
    
        
    os.system("clear")  #Limpiar pantalla.

    #Imprir rótulo del juego seleccionado.
    print("=================================================================================")
    print("=                      _   _   _   _   _   _   _   _                            =")
    print("=                     / \ / \ / \ / \ / \ / \ / \ / \                           =")
    print("=                    ( a | h | o | r | c | a | d | o )                          =")
    print("=                     \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                           =")
    print("=                                                                               =")
    print("=================================================================================")

    print(f"\n\n              ¡¡¡ {nombre} bienvenid@ al juego del Ahoracado !!!\n\n")    
    print ("          El juego consiste en adivinar la palabra oculta letra a letra.\n\n")
    print("                     ¡¡¡¡   E M P E C E M O S  !!!\n\n\n")
    input('Presiona "ENTER" para continuar')
    os.system("clear")


    palabra_aleatoria = random.choice(palabras_aleatorias).lower()  #Genera una palabra aleatoria de las definidas antes.
    palabra_guiones = "_"*len(palabra_aleatoria)         #oculta la palabra. Imprime un '_' por cada letra de la palabra.
    lista_palabra=list(palabra_aleatoria)                #guarda la palabra seleccionada
    lista_guiones=list(palabra_guiones)                  #guarda la palabra oculta 

#Crear un bucle limitado por los aciertos e intentos
    
    while 0 < intentos <= 10 and acierto==False:

      # Imprime la figura del ahorcado en funcion de los intentos. -lin.434-
        self.figura_Ahoracado(intentos)
    
        print(f"\nEstas son las letras ocultas de la palabra:   {' '.join(lista_guiones)}")
      #Imprime las letras seleccionadas por el usuario durante el juego.
        print(f'\n\nLas letras usadas hasta ahora son: {letra_usada}\n\n')

      # preguntar al usuario la letra
        letra=input("Introduce una letra a ver si está en la palabra =>  ").lower()
      #Usamos el condicional para buscar la letra seleccionada en la palabra oculta.
        if letra in lista_palabra:
          print(f'\n\nGenial! la letra {letra.upper()} está en la palabra oculta.')
          print("-------------------------------")
  
         #crear un bucle for para buscar la letra en la palabra ocualta.  
          aux=0  #metemos el indice en la variable aux.
          for i in lista_palabra:      
            if i == letra:                #Si encuentra coincidencia.
                lista_guiones[aux]=letra  #Sustituye en la palabra oculta el '_' localizada con el indice, por la letra.

            aux += 1
            
        else:                              #Si no hay coincidencia de letra, resta un intento.
            intentos-=1
            print(f'\n\nNo, la letra {letra.upper()} no está.\n\n{nombre} te quedan {intentos} intentos.')
            print("-------------------------------")
    
      # Imprimi la palabra con la letra encontrada 
        palabra_jugada = ''.join(lista_guiones)      
    
      # Imprimir las letras usadas
        if letra not in letra_usada:
          letra_usada.append(letra)
          letra_usada.sort()
        
        print('\n\n\n')
        input('Presiona "ENTER" para continuar')
        os.system("clear")                   

        if palabra_jugada == palabra_aleatoria:
            acierto = True                   #Para el bucle al coincidir la palabra adivinada con la oculta.

    #Imprime mensaje al usuario al completar el juego.
    if acierto == True:   
          print(f"\n  Felicidades {nombre} eres GANADOR@ de la partida  !!!!\n")
          print(f'\n       La palabra oculta era {palabra_aleatoria.upper()}\n') #Imprime la palabra escondida.
          print('          :)  :)  :)  :)  :)  :)\n\n\n')
                    
             
    else:
          self.figura_Ahoracado(intentos)
          print(f"\n        Lo sentimos {nombre} PERDISTE \n")
          print(f'\n       La palabra oculta era {palabra_aleatoria.upper()}.\n') #Imprime la palabra escondida.
          print('          :(  :(  :(  :(  :(  :(\n\n\n')
          
    print('')
    #pregunta al usuario si desea continuar.
    self.volver_a_jugar()
              
      
  #Define el método para el juego preguntas y respuestas.
  def preguntas_y_respuestas(self, nombre):
      
      intentos_juego = 3
      acertadas = 0
      ronda = 0

      #Lista de preguntas aleatorias:
       #cada pregunta es un diccionario con pregunta y opciones asociada a la respuesta correcta.
      listado_preguntas =  {"¿Cuál es el río más largo de la Península Ibérica? \n\na) Tajo \nb) Guadiana \nc) Ebro \n\n=> " : "a",      "¿Cuál es el país más pequeño del mundo? \n\na) Francia \nb) Portugal \nc) El Vaticano \n\n=>" : "c", 
      "¿Cuántos océanos hay en la Tierra?  \n\na) Cuatro \nb) Cinco \nc) Tres  \n\n=> " : "b",
      "¿Qué país tiene más habitantes? \n\na) España \nb) Austria \nc) China  \n\n=> " : "c",
      "¿Qué país es el más grande del mundo? \n\na) Rusia \nb) Hungría \nc) Italia  \n\n=> " : "a",
      "¿Cuál es la montaña más alta del mundo? \n\na) Everest \nb) Kilimanjaro \nc) Teide  \n\n=> " : "a",
      "¿Cuál es el río más largo del mundo? \n\na) Nilo \nb) Amazonas \nc) Támesis  \n\n=> " : "a",
      "¿Cuál es la capital de Francia?  \n\na) Roma \nb) París \nc) Londres  \n\n=> " : "b",
      "¿Dónde podemos ver las auroras boreales?  \n\na) Finlandia \nb) Suiza \nc) Dinamarca \n\n=> " : "a",
      "¿Cuál es la capital de España? \n\na) Barcelona \nb) Sevilla \nc) Madrid  \n\n=> " : "c"}

      #limpia pantalla
      os.system("clear")
      #Imprir rótulo del juego seleccionado.  
      print("===============================================================================")
      print("=                    _   _   _   _   _   _   _   _                            =")
      print("=                   / \ / \ / \ / \ / \ / \ / \ / \                           =")
      print("=                  ( p | r | e | g | u | t | a | s)                           =")
      print("=                   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                           =")
      print("=                                 _                                           =")
      print("=                                / \                                          =")
      print("=                               | y |                                         =")
      print("=                                \_/                                          =")      
      print("=                 _   _   _   _   _   _   _   _   _   _                       =")
      print("=                / \ / \ / \ / \ / \ / \ / \ / \ / \ / \                      =")
      print("=               ( r | e | s | p | u | e | s | t | a | s )                     =")
      print("=                \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                      =")
      print("=                                                                             =")
      print("===============================================================================")
      
      print(f"\n\n     ¡¡¡ {nombre} bienvenid@ al juego de Preguntas y respuestas !!!\n\n")    
      print("                    ¡¡¡¡   E M P E C E M O S  !!!\n\n\n")
      input('Presiona "ENTER" para continuar')
      os.system("clear") #limpia pantalla
    #Crea bucle en funcion de los aciertos e intentos:  
      while intentos_juego > 0 and acertadas < 5:

        os.system("clear")  #limpia pantalla
    #imprimimos la ronda en la que se encuentra el usuario.
        ronda +=1    

        print("")            
        print("  RONDA", ronda)
        print("*" * 11)
        print('\n')
    #selecciona una pregunta al azar y la instanciamos en una variable
        pregunta = random.choice(list(listado_preguntas.keys()))
    #Instanciamos la respuesta en minusculas
        respuesta = input(pregunta).lower()
    
        #crea un bucle donde compara la respuesta con la guardada   
        while respuesta != 'a' and respuesta != 'b' and respuesta != 'c':
            print("")
            print("")     
            print(f"ERROR! {nombre}, la opción que has intorducido no existe.\n\nVuelve a intentaerlo. Introduce 'a', 'b' o 'c.")
            print("-------------------------------\n\n")
            respuesta = input('=> ')
            
      
        if respuesta == listado_preguntas.get(pregunta):
            acertadas +=1    #aumenta los aciertos
            print("")
            print("")
            print(f"Muy bien {nombre}! Has acertado la pregunta. \n\nSigue jugando, ya tienes {acertadas} aciertos")
            print("-------------------------------")
            print("")
            print("")
    #Elimina la pregunta para evitar repeticiones.      
            listado_preguntas.pop(pregunta)

            input('Presiona "ENTER" para continuar')
    #Crea condición que finaliza el juego:      
            if acertadas ==5:
                os.system("clear")     #limpia pantalla
    #Imprime felicitación.
                print("\n")
                print("              ===   ===                      ")
                print("             |  _| |  _|                     ")
                print("             | | | | | |                     ")
                print("              ===   ===   OLEEEEEE!!!        ")
                print("                  O                          ")
                print("               _     _                       ")
                print("                _____                        ")
                print("                                             ")
                print("\n\n")
                print(f"Felicidades {nombre}!!!, has ganado el juego!\n")
                print("=============================================")
        
        
        else:
            intentos_juego -= 1  #resta intentos
    #Crea condición que finaliza el juego:        
            if intentos_juego !=0: 
                print("")
                print("")     
                print(f"Has fallado la pregunta {nombre}.\n\nTe quedan {intentos_juego} intentos")
                print("-------------------------------")
                print("")
                print("")
                input('Presiona "ENTER" para continuar')
                
            else:
                os.system("clear")   #limpia pantalla
    #imprime no superación del juego
                print("\n")
                print("               ===   ===          ")
                print("              |  _| |  _|         ")
                print("              | | | | | |         ")
                print("               ===   ===   OHHH!!!")
                print("                   O              ")
                print("                  ---             ")
                print("                 |   |            ")
                print("                  ---             ")
                print("                                  ")
                print("\n\n")
                print(f"Lo sentimos {nombre}, te has quedado sin intentos")
                print("=============================================")
          

      self.volver_a_jugar()

    #Define el método para el juego preguntas y respuestas.            
  def piedra_papel_tijera(self,nombre):
        
        os.system("clear")     #limpia pantalla
    #Crea tupla con las opciones del juego.    
        opciones = ("PIEDRA", "PAPEL", "TIJERA")
    
        rondas = 1
        jugador1_gana = 0
        jugador2_gana = 0
    
    #Imprir rótulo del juego seleccionado. 
        print(f"\n\n¡¡¡ {nombre} bienvenid@ al juego de Piedra, Papel o Tijera !!!\n\n")
        print(f'                       S U E R T E     \n\n\n')
    #llamamos a la funcion que imprime parte del rotulo del juego.   
        self.figura_Piedra_Papel_o_Tijera()
        print('')
        input('Presiona "ENTER" para continuar')
        os.system("clear")      #limpia pantalla
        
        while True:
            os.system("clear")
            self.figura_Piedra_Papel_o_Tijera()  #imprime dibujo decorativo


            print("=" * 11)               
            print("  RONDA", rondas)
            print("=" * 11)
            print('')
        
           #pregunta al usuario e instancia la respuesta.
            respuesta_jugador1 = input(f" {nombre} elige una opcion entre Piedra, Papel o Tijera =>  ").upper()
            print("\n")
            #Busca coincidencia de la respuesta con las opciones.
            if respuesta_jugador1 not in opciones:
                print("Esa opción no es válida\n")
                input('Presiona "ENTER" para continuar')
                print('')
                continue   #Permite continuar sin problema con la respuesta.
            #selecciona una opcion aleatoria:
        
            respuesta_jugador2 = random.choice(opciones)
            #Imprime dibujo decorativo:
            print(f'Respuesta {nombre}      vs      Respuesta Ordenador')
            print('      |                                |          ')
            print('     \|/                              \|/         ')
            print('      \'                                \'          ')
            print(f'    {respuesta_jugador1}                           {respuesta_jugador2}\n') #imprime respuestas del jugador y aleatoria
            #Crea sentencia de control que busca coincidencia con las respuestas.
            #Define las coincidencias ganadoras.m
            if respuesta_jugador1 == respuesta_jugador2:
                print("\nEMPATE!\n")
        
            elif respuesta_jugador1 == "PIEDRA":
                if respuesta_jugador2 == "TIJERA":
                    print("\nPIEDRA gana a TIJERA\n")
                    print(f"{nombre} ganas !!!\n")
                    jugador1_gana +=1   
        
                else:
                    print("\nPAPEL gana a PIEDRA\n")
                    print("El Ordenador gana!!!\n")
                    jugador2_gana +=1   
        
            elif respuesta_jugador1 == "PAPEL":
                if respuesta_jugador2 == "PIEDRA":
                    print("\nPAPEL gana a PIEDRA\n")
                    print(f"{nombre} ganas !!!\n")
                    jugador1_gana +=1    
            
                else:
                    print("\nTIJERA gana a PAPEL\n")
                    print("El Ordenador gana!!!\n")
                    jugador2_gana +=1    
             
            elif respuesta_jugador1 == "TIJERA":
                if respuesta_jugador2 == "PAPEL":
                    print("\nTIJERA gana a PAPEL\n")
                    print(f"{nombre} ganas !!!\n")
                    jugador1_gana +=1    

                else:
                    print("\nPIEDRA gana a TIJERA\n")
                    print("El Ordenador gana!!!\n")
                    jugador2_gana +=1     
            #imprime marcadores de puntos.
            print(f"Marcador {nombre} : ", jugador1_gana)
            print("Marcador Ordenador :", jugador2_gana)
            print('')

            input('Presiona "ENTER" para continuar')
  
            #Sentencia de control que finaliza el el juego                      
            if jugador1_gana == 3:  #compara puntos jugador.
                os.system('clear')
                print(f"\nFelicidades {nombre} eres GANADOR@ de la partida  !!!!\n")
                print('              :)  :)  :)  :)  :)  :)\n')
                break  #Detiene el juego
    
            if jugador2_gana == 3:  #compara puntos del ordenador.
                os.system('clear')
                print("\nEl ganador de la partida es el Ordenador\n")
                print('        :(  :(  :(  :(  :(  :(\n')
                break  #Detiene el juego 
            
            
            rondas +=1  #suma ronda por ciclo
      
        
        self.volver_a_jugar()



    
  def salir (self):
      exit()


#Define función que permite al jugador volver a jugar
  def volver_a_jugar(self):
      volver_a_jugar = 0
      
      #Define ciclo while 
      while volver_a_jugar == 0:
        print('')

         #pregunta al usuario con funcíón input()
        volver_al_menu = input(f'{nombre}, quieres volver a jugar?\n\nS : sí\n\nN : no\n\n=>  ').upper()

        if volver_al_menu == 'S':
          #llama a la función menu del comienzo juego.
          self.menu()
          volver_a_jugar =1

        elif volver_al_menu == 'N':
            os.system("clear") #limpia pantalla
            print(f'\n\n   ¡¡¡  Muchas gracias {nombre}  !!! \n\n  Esperamos volver a verte pronto. \n\n       :)  :)  :)  :)  :) '  )
            print('\n\n')
            input('Presiona "ENTER" para continuar')
            os.system("clear") #limpia pantalla.
            self.salir()       #llama a funcion de salida.
            volver_a_jugar=1

        else:
            print('\n\nERROR! La opción introducida no existe.')
            print('\n')    

  def reglas_juego(self):
      os.system("clear")
      self.figura_menu_inicio()
      print('')
      print('''1. PREGUNTAS Y RESPUESTAS:
            
   DESCRIPCIÓN:
    - El juego va a constar de 10 preguntas aleatorias sobre geografía.
    - Cada pregunta tendrá tres opciones de respuesta (a, b, c) y sólo una será correcta.
    - Se obtiene un punto por cada respuesta acertada.

   REGLAS DEL JUEGO:
    - El jugador tendrá dos intentos por cada pregunta.
    - El jugador empieza con 3 vidas y se le restará una cada vez que conteste incorrectamente una pregunta.
    - El juego termina si el jugador pierde todas sus vidas o si responde a 5 preguntas correctamente.
            

2. AHORCADO:
            
   DESCRIPCIÓN:
    - El jugador tiene que adivinar una palabra.
    - El jugador tiene que ir adivinando letras hasta completar la palabra.

   REGLAS DEL JUEGO:
    - El jugador tiene 10 vidas.
    - Por cada fallo se dibuja una parte del cuerpo en la horca y se pierde una vida.
    - El juego termina si el jugador adivina la palabra o si se dibuja el cuerpo entero en la horca y el jugador pierde todas sus vidas.
            
            
3. PIEDRA, PAPEL O TIJERA
            
   DESCRIPCIÓN:
    - Dos jugadores eligen una de las tres opciones: "Piedra", "Papel" o "Tijera"
    - Se obtiene un punto por cada ronda ganada.
    - Gana el jugador que consiga 3 puntos.

   REGLAS DEL JUEGO:
    - Piedra vence a Tijera.
    - Tijera vence a Papel.
    - Papel vence a piedra
            ''')
      print('')
      print("-------------------------------")
      input('Presiona "ENTER" para continuar')
      
      self.menu()
   

    #función que imprime dibujo rótulo:
  def figura_menu_inicio (self):
      os.system("clear")
      print("================================================================================")
      print("=        xxxxxxx      xxxxxxx                                                  =")
      print("=          xxxxx      xxxxx     xxxxx  xxxxx  xxx  xxx  xxxxxx  xxxxxx         =")
      print("=             xxx    xxx        x      x   x  x  xx  x  x       x              =")
      print("=               xxx xxx         x  xx  xxxxx  x   x  x  xxxxxx  xxxxxx         =")
      print("=             xxx    xxx        x   x  x   x  x      x  x            x         =")
      print("=          xxxxx      xxxxx     xxxxx  x   x  x      x  xxxxxx  xxxxxx         =")
      print("=        xxxxxxx      xxxxxxx                                                  =")
      print("================================================================================")
      print("")
      print(" Bienvenido a los juegos interactivos de X Games ")
      print("================================================")
      print("")  



#función que imprime dibujos decorativos:
  def figura_Piedra_Papel_o_Tijera (self):
        print("Piedra:                Papel:                   Tijera:           ")
        print("    _______             _______                  _______          ")
        print("---'   ____)       ---'    ____)____        ---'     ____)____    ")
        print("      (_____)                 ______)                   ______)   ")
        print("      (_____)                _______)              __________)    ")
        print("      (____)                 _______)             (____)          ")
        print("---.__(___)        ---.__________)          ---.__(___)           ")
        print("\n")

#función que define las etapas de vida de juego Ahorcado:
  def figura_Ahoracado(self, vidas):
        figura=[
         '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /|\\
          |       / | \\
          |        / \\
          |       /   \\
         ==================''',
           '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /|\\
          |       / | \\
          |        /
          |       /  
         ==================''',
                '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /|\\
          |       / | \\
          |         |
          |          
         ==================''',
                '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        / \\
          |       /   \\ 
          |         
          |          
         ==================''',
                '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /   
          |       /   
          |        
          |        
         ==================''',
                  '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |          
          | 
          |         
          |        
         ==================''',
                  '''
          +---------+
          |        _|_
          |        |__|
          |        
          |          
          |         
          |   
          |     
         ==================''',
                    '''
          +---------+
          |         |
          |        
          |        
          |          
          |         
          |
          |
         ==================''',
                        '''
          +
          |         
          |         
          |        
          |        
          |                  
          |
          |
         ==================''',
                            '''
                   
              
              
                       
      
                            


         ==================''','''         
              
              
                       
      
                            


                  
         ------------------''']
        
        print(figura[vidas])
      
      
#MEJORA. Lista de jugadores  
class Jugadores:
  
  def __init__(self):
    self.lista_jugadores = []
  
  def alta_jugador(self,nombre, equipo):
      if nombre not in self.lista_jugadores:
        jugador = Jugador(nombre, equipo)
        self.lista_jugadores.append(nombre)
      else:
        pass

class Jugador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

os.system("clear")
print("================================================================================")
print("=        xxxxxxx      xxxxxxx                                                  =")
print("=          xxxxx      xxxxx     xxxxx  xxxxx  xxx  xxx  xxxxxx  xxxxxx         =")
print("=             xxx    xxx        x      x   x  x  xx  x  x       x              =")
print("=               xxx xxx         x  xx  xxxxx  x   x  x  xxxxxx  xxxxxx         =")
print("=             xxx    xxx        x   x  x   x  x      x  x            x         =")
print("=          xxxxx      xxxxx     xxxxx  x   x  x      x  xxxxxx  xxxxxx         =")
print("=        xxxxxxx      xxxxxxx                                                  =")
print("================================================================================")
print("")
print(" Bienvenido a los juegos interactivos de X Games ")
print("================================================")
print("")


#Introducimos los datos del usuario para identificar al jugador y a la consola.
#Utilizamos la función input() para preguntar al usuario:

nombre=input("Introduce tu nombre: ").capitalize()             
equipo=input("A que equipo perteneces: ").capitalize()

# Creamos la instancia de la classe Juegos
juego = Juegos(nombre,equipo)
juego.menu()

#*MEJORA EN PROCESO: Registro de jugadores.
#Creamos un registro de jugadores para registrar las rachas ganadas y puntuaciones:

lista_jugadores=Jugadores()
lista_jugadores.alta_jugador(nombre,equipo)

