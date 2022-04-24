#Importar libreria
import pygame#libreria para hacer juegos en dos dimensiones
from pygame.locals import*
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

numeros=[
    [1,2,3,4,5,6,7,8,9],#1
    [1,2,3,4,5,6,7,8,9],#2
    [1,2,3,4,5,6,7,8,9],#3
    [1,2,3,4,5,6,7,8,9],#4
    [1,2,3,4,5,6,7,8,9],#5
    [1,2,3,4,5,6,7,8,9],#6
    [1,2,3,4,5,6,7,8,9],#7
    [1,2,3,4,5,6,7,8,9],#8
    [1,2,3,4,5,6,7,8,9] #9 
]

#intento de condiciones y funciones
def dibujo_tablero(): 
    color_bordes=pygame.Color("black")
    pygame.draw.rect(pantalla,color_bordes,pygame.Rect(15,15,785,785),10)#marco del tablero bordes externos
    a=1
    #tengo sueño Xc
    while(a*165) < 1468:
        ancho_de_linea= 5 if a % 3 > 0 else 10#para hacer nueve divisones en el tablero
        pygame.draw.line(pantalla,color_bordes,pygame.Vector2((a*88)+ 15,15),pygame.Vector2((a*88)+15,800),ancho_de_linea) #Lineas Verticales
        pygame.draw.line(pantalla,color_bordes,pygame.Vector2(15,(a*88)+ 15),pygame.Vector2(795,(a*88)+15),ancho_de_linea) #Lineas Horizontales
        a+=1
#numero sobre tablero        
    
#para que cierre la ventana
def bucle_cierre():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
           
    pygame.display.update()#activa todo lo que este sobre pantalla sin ello no se ejecuta
    dibujo_tablero()#se llama a la funcion 
    pygame.display.flip()#actualiza la superficie de visualizacion completa
while 1:
    bucle_cierre()#se llama la funcion, usar () sino se genera un bucle infinito
