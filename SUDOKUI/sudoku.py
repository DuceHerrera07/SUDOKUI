#Importar libreria
import tkinter
import pygame#libreria para hacer juegos en dos dimensiones
import tkinter as tk #blioteca grafica (GUI)
import tkinter.font as tkFont#libreria del texto y abrevacion del llamdo de la funcion

from tkinter import*#para gregar la funcion de texto
#Inicio de pygame
pygame.init()

numeros_del_tablero=[
        [5,3,0,0,7,0,0,0,0],#1
        [6,0,3,1,9,5,0,0,0],#2
        [0,9,8,0,0,0,0,6,0],#3
        [8,0,0,0,6,0,0,0,0],#4
        [4,0,0,8,0,3,0,0,1],#5
        [7,0,0,0,2,0,0,0,6],#6
        [0,6,0,0,0,0,2,8,0],#7
        [0,0,0,4,1,9,0,0,5],#8
        [0,0,0,0,8,0,0,7,9]#9
    ]

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

def ventana2():
        ven = tk.Tk()
        #ancho y largo (orden de geometry)
        ven.geometry('1300x820')#dimension de ventana
        ven.title('Reglas de sodoku clásico')#titulo
        ven.iconbitmap(r"instruccion.ico")#icono
        ven.configure(bg="white")#color de fondo
        #imagen-formato de imagen
        imagen=tkinter.PhotoImage(file="tkinter_imagen_N.gif")#variable que guarda la imagen
        sobre_ventana=tkinter.Label(ven,image=imagen).place(x=0,y=0)#activa la imagen y posiciona en cordenadas especificas
        ven.configure(bg="white")#color de fondo
        estilo_fuente=tkFont.Font(family="Cascadia Mono SemiLight",size=15)
        texto=Label(ven,text="Un rompecabezas en Sudoku comienza con una cuadricula en el cual",font=estilo_fuente,bg="white")#60 caracteres para que ajuste bien sobre pantalla
        texto1=Label(ven,text="algunos de los números",font=estilo_fuente,bg="white")
        texto2=Label(ven,text="podra decidir las cordenas de sus",bg="white")
        texto3=Label(ven,text="barcos, cuando estos esten asignados",bg="white")
        
        #para que se muestren en pantalla las variables anteriores que son str, columna y fila en la que apareceran
        texto.place(x=500,y=5)
        #texto1.grid(column=11,row=3)
        #texto2.grid(column=11,row=4)
        #texto3.grid(column=11,row=5)
        #salir=tk.Button(ven,text="Entendido")
        ven.mainloop()
   
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
def numeros_sobre_tablero_funcion():
    fila=0
    Compensar=40#nos ayudara para alinear numeros dentro del tablero
    while fila < 9:
        columna=0
        while columna < 9:
            salida=numeros_del_tablero[fila][columna]
            #formato del texto de los numeros
            texto_numeros=fuente_texto.render(str(salida),True,pygame.Color("black"))#formato del texto
            pantalla.blit(texto_numeros,pygame.Vector2((columna*88) + Compensar,(fila * 88) + Compensar))#para mostrar los numero sobre el tablero
            columna += 1 
        fila += 1
#funciones  
ventana2()        
dibujo_tablero()
numeros_sobre_tablero_funcion()   
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
