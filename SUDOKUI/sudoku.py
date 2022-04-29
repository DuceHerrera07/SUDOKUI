#linea 1 hasta la 106 hecho por Dulce Herrera
#Importar libreria
import pygame#libreria para hacer juegos en dos dimensiones
import random
#Inicio de pygame
pygame.init()

#ventana donde estaran los tableros aliado y enemigo
pantalla = pygame.display.set_mode((900,810))#ancho y altura
#fondo de ventana
pantalla.fill("white")
#icono de ventana pygame
icono=pygame.image.load ("sudoku_Icono.jpg")
pygame.display.set_icon(icono)
#titulo de la ventana
pygame.display.set_caption("Sudoku")
#tipo de fuente para texto
fuente_texto=pygame.font.SysFont(None,70)
#actualizar pantalla
reloj=pygame.time.Clock()

#condiciones y funciones
def dibujo_tablero(): 
    color_bordes=pygame.Color("black")
    pygame.draw.rect(pantalla,color_bordes,pygame.Rect(15,15,785,785),10)#marco del tablero bordes externos
    a=1
    #crea las lineas que forman el tablero
    while(a*165) < 1468:
        ancho_de_linea= 5 if a % 3 > 0 else 10#para hacer nueve divisones en el tablero
        pygame.draw.line(pantalla,color_bordes,pygame.Vector2((a*88)+ 15,15),pygame.Vector2((a*88)+15,800),ancho_de_linea) #Lineas Verticales
        pygame.draw.line(pantalla,color_bordes,pygame.Vector2(15,(a*88)+ 15),pygame.Vector2(795,(a*88)+15),ancho_de_linea) #Lineas Horizontales
        a+=1
#Dibujar numeros sobre el tablero
def numero_sobre_tablero():
    fila=0
    Compensar=40#nos ayudara para alinear numeros dentro del tablero
    while fila < 9:
        columna=0
        while columna < 9:
            Numero1=[random.randint(1,9) for x in range(1)]#genera numero random/aleatorios
            sin_corchetes_Numero1=str(Numero1)[1:-1]#variable para que no muestre los corchetes en cada numero
            #crear condicional para que la variable Numero1 no se repita entre columnas y filas
            
            
            #formato del texto de los numeros
            texto_numeros=fuente_texto.render(str(sin_corchetes_Numero1),True,pygame.Color("black"))#formato del texto
            pantalla.blit(texto_numeros,pygame.Vector2((columna*88) + Compensar,(fila * 88) + Compensar))#para mostrar los numero sobre el tablero
            columna += 1 
        fila += 1
                
#llamando a las funciones
dibujo_tablero()
numero_sobre_tablero()  
      
#Bandera      
bandera=True
#funciones de mouse y teclado sobre el tablero
while bandera:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera=False
        #acceder al mouse en este caso obtener sus cordenadas donde haga click el jugador    
        if event.type==pygame.MOUSEBUTTONDOWN:
            #si el usuario presiona el mouse se obtiene posicion
            posicion=pygame.mouse.get_pos()
            print("X,Y",posicion,"Coordenadas de la reticula")    
        #acceso al teclado para teclas en especifico del 1 al 9
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                key=1
                print("Soy la  tecla 1")
            if event.key==pygame.K_2:
                key=2
                print("Soy la tecla 2")
            if event.key==pygame.K_3:
                key=3
                print("Soy la tecla 3")
            if event.key==pygame.K_4:
                key=4
                print("Soy la tecla 4")
            if event.key==pygame.K_5:
                key=5
                print("Soy la tecla 5")
            if event.key==pygame.K_6:
                key=6
                print("Soy la tecla 6")
            if event.key==pygame.K_7:
                key=7
                print("Soy la tecla 7")
            if event.key==pygame.K_8:
                key=8
                print("Soy la tecla 8")
            if event.key==pygame.K_9:
                key=9
                print("Soy la tecla 9")
            #para eliminar, aun no funciona del todo.
            if event.key==pygame.K_DELETE:
                posicion.clear()
                key=None
                                         
    #rapidez de actualizacion de pantalla
    reloj.tick(60)
    pygame.display.update()#activa todo lo que este sobre pantalla sin ello no se ejecuta
    pygame.display.flip()#actualiza la superficie de visualizacion completa
#IDLE_cerrar ventana    
pygame.quit()
