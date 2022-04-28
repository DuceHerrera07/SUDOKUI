#Importar libreria
import pygame#libreria para hacer juegos en dos dimensiones
import random
#import numpy
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
#Numeros sobre tablero
Numeros=[
    ["1","","","","","","","",""],#1
    ["","","","","","","","",""],#2
    ["","","","","","","","",""],#3
    ["","","","","","","","",""],#4
    ["","","","","","","","",""],#5
    ["","","","5","","","","",""],#6
    ["","","","","","","","",""],#7
    ["","","","","","","","",""],#8
    ["","","","","","","","",""]#9
]
#intento de condiciones y funciones
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
    
    Compensar=30#nos ayudara para alinear numeros dentro del tablero
    while fila < 9:
        columna=0
        while columna < 9:
            #se puede usar cualquiera de las dos 
            #Numero1=numpy.random.randint(low=1,high=9,size=1).tolist()#prueba para generar numeros random
            Numero1=[random.randint(1,9) for x in range(1)]#genera numero random/aleatorios
            #crear condicional para que la variable Numero1 no se repita entre columnas y filas
            
            #formato del texto de los numeros
            texto=fuente_texto.render(str(Numero1),True,pygame.Color("black"))#formato del texto
            pantalla.blit(texto,pygame.Vector2((columna*88) + Compensar,(fila * 88) + Compensar))#para mostrar los numero sobre el tablero
            columna += 1 
        fila += 1
#funciones
dibujo_tablero()
numero_sobre_tablero()        
#Bandera      
bandera=False
#para que cierre la ventana
while not bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #si el usuario presiona el mouse se obtiene posicion
            posicion=pygame.mouse.get_pos()
            print("Click",posicion,"Coordenadas de la reticula")
        elif event.type==pygame.KEYDOWN:
            detectar=pygame.key.get_pressed()
            return_detectar=detectar[pygame.K_RETURN]
            print("Estoy precionando una tecla:",return_detectar)#no reconoce mi tecla
                        
    #rapidez de actualizacion de pantalla
    reloj.tick(60)
    pygame.display.update()#activa todo lo que este sobre pantalla sin ello no se ejecuta
    pygame.display.flip()#actualiza la superficie de visualizacion completa
#IDLE_cerrar ventana    
pygame.quit()
