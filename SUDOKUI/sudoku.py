#Importar libreria
import pygame#libreria para hacer juegos en dos dimensiones
import tkinter
import tkinter as tk #blioteca grafica (GUI)
import tkinter.font as tkFont#libreria del texto y abrevacion del llamdo de la funcion
from tkinter import*#para gregar la funcion de texto

#Inicio de pygame
pygame.init()

numeros_del_tablero=[
        [5,3,"","",7,"","","",""],#1
        [6,"",2,1,9,5,"","",""],#2
        ["",9,8,"","","","",6,""],#3
        [8,"","","",6,"","","",3],#4
        [4,"","",8,"",3,"","",1],#5
        [7,"","","",2,"","","",6],#6
        ["",6,"","","","",2,8,""],#7
        ["","","",4,1,9,"","",5],#8
        ["","","","",8,"","",7,9]#9
    ]
solucion_tablero=[
        [5,3,4,6,7,8,9,1,2],#1
        [6,7,2,1,9,5,3,4,8],#2
        [1,9,8,3,4,2,5,6,7],#3
        [8,5,9,7,6,1,4,2,3],#4
        [4,2,6,8,5,3,7,9,1],#5
        [7,1,3,9,2,4,8,5,6],#6
        [9,6,1,5,3,7,2,8,4],#7
        [2,8,7,4,1,9,6,3,5],#8
        [3,4,5,2,8,6,1,7,9]#9
    ]

#ventana
pantalla = pygame.display.set_mode((1500,810))#ancho y altura
#fondo de ventana
pantalla.fill("white")
#icono de ventana pygame
icono=pygame.image.load ("sudoku_Icono.jpg")
pygame.display.set_icon(icono)
#titulo de la ventana
pygame.display.set_caption("Sudoku")
#tipo de fuente para texto
fuente_texto=pygame.font.SysFont(None,70)
#ancho y alto
ancho=15
alto=15

#actualizar pantalla
reloj=pygame.time.Clock()
#libreria tkinter
def ventana2():
        #iniciando/activando pantalla
        ven = tk.Tk()
        #ancho y largo (orden de geometry)
        ven.geometry('1300x720')#dimension de ventana
        ven.title('Reglas de sodoku clásico')#titulo
        ven.iconbitmap(r"instrucion.ico")#icono
        ven.configure(bg="white")#color de fondo
        #imagen-formato de imagen
        imagen=tkinter.PhotoImage(file="tkinter_imagen_N.gif")#variable que guarda la imagen
        sobre_ventana=tkinter.Label(ven,image=imagen).place(x=0,y=0)#activa la imagen y posiciona en cordenadas especificas
        #funcion para agregar estilo de fuente y tamaño
        estilo_fuente=tkFont.Font(family="Cascadia Mono SemiLight",size=20)
        fuente=tkFont.Font(family="Berlin Sans FB Demi",size=15)#para el botón
        #inicia el los textos que se mostraran sobre la ventana de tkinter
        texto=Label(ven,text="Un rompecabezas en Sudoku comienza con una",font=estilo_fuente,bg="white")
        texto1=Label(ven,text="cuadricula en el cual algunos de los números ya,",font=estilo_fuente,bg="white")
        texto2=Label(ven,text="están en su lugar en dependencia de la dificultad del juego. Se completa",font=estilo_fuente,bg="white")
        texto3=Label(ven,text="de un rompecabezas cuando cada número del 1 al 9 ",font=estilo_fuente,bg="white")
        texto4=Label(ven,text="aparecen solamente una vez en cada una de las 9",font=estilo_fuente,bg="white")
        texto5=Label(ven,text="filas,",font=estilo_fuente,bg="white",foreground="yellow")
        texto6=Label(ven,text="columnas",font=estilo_fuente,bg="white",foreground="red")
        texto7=Label(ven,text="y",font=estilo_fuente,bg="white")
        texto8=Label(ven,text="celdas.",font=estilo_fuente,bg="white",foreground="green")
        texto9=Label(ven,text="Analice la cuadrícula para encontar los números",font=estilo_fuente,bg="white")
        texto10=Label(ven,text="que pudiera encajar en cada celda del tablero.",font=estilo_fuente,bg="white")
        #para que se muestren en pantalla las variables anteriores que son str, x & y en la que apareceran
        texto.place(x=500,y=5)#x= lo corre hacia la derecha e izquierda
        texto1.place(x=500,y=40)#y= lo corre hacia abajo y arriba
        texto2.place(x=500,y=80)#+40 en y=
        texto3.place(x=500,y=120)
        texto4.place(x=500,y=160)
        texto5.place(x=500,y=200)#yellow
        texto6.place(x=600,y=200)#red
        texto7.place(x=740,y=200)#y
        texto8.place(x=770,y=200)#green
        texto9.place(x=500,y=280)
        texto10.place(x=500,y=320)
        #crear boton que cierre la ventana de tkinter
        tk.Button(text="¡Entendido!",command=ven.destroy,height=3,width=15,font=fuente,bg="blue").place(x=750,y=400)
        ven.mainloop()
grid=[ ]        
#condiciones y funciones para la ventana del juego
def dibujo_tablero(): 
    #imagen sobre pantalla pygame
    instruccion=pygame.image.load("instruccionnew.jpg")
    pantalla.blit(instruccion,(800,100))
    #
    color_bordes=pygame.Color("black")
    pygame.draw.rect(pantalla,color_bordes,pygame.Rect(15,15,785,785),10)#marco del tablero/bordes externos
    a=1
    #crea las lineas que forman el tablero
    while(a*165) < 1468:
        ancho_de_linea= 5 if a % 3 > 0 else 9#para hacer nueve divisones en el tablero
        pygame.draw.line(pantalla,color_bordes,pygame.Vector2((a*88)+ ancho,alto),pygame.Vector2((a*88)+ancho,800),ancho_de_linea) #Lineas Verticales
        pygame.draw.line(pantalla,color_bordes,pygame.Vector2(ancho,(a*88)+ alto),pygame.Vector2(795,(a*88)+alto),ancho_de_linea) #Lineas Horizontales
        a+=1
     
#Dibujar numeros sobre el tablero
def numeros_sobre_tablero_funcion():
    fila=0
    Compensar=45#nos ayudara para alinear numeros dentro del tablero
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
ventana2()#tkinter        
dibujo_tablero()#dibujo de lineas 
numeros_sobre_tablero_funcion() 

#Bandera      
bandera=True
#funciones de mouse y teclado
while bandera: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera=False
        #acceder al mouse en este caso obtener sus cordenadas donde haga click el jugador    
        if event.type==pygame.MOUSEBUTTONDOWN:
            #si el usuario presiona el mouse se obtiene posicion
            posicion=pygame.mouse.get_pos()
            columna = posicion[0] // (ancho + 15)
            fila = posicion[1] // (alto + 15)
            
                    #acceso al teclado para teclas en especifico del 1 al 9
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                tecla=1
                print("Soy la  tecla 1")
            if event.key==pygame.K_2:
                tecla=2
                print("Soy la tecla 2")
            if event.key==pygame.K_3:
                tecla=3
                print("Soy la tecla 3")
            if event.key==pygame.K_4:
                tecla=4
                print("Soy la tecla 4")
            if event.key==pygame.K_5:
                tecla=5
                print("Soy la tecla 5")
            if event.key==pygame.K_6:
                tecla=6
                print("Soy la tecla 6")
            if event.key==pygame.K_7:
                tecla=7
                print("Soy la tecla 7")
            if event.key==pygame.K_8:
                tecla=8
                print("Soy la tecla 8")
            if event.key==pygame.K_9:
                tecla=9
                print("Soy la tecla 9")          
        #rapidez de actualizacion de pantalla
        reloj.tick(60)
        pygame.display.update()#activa todo lo que este sobre pantalla sin ello no se ejecuta
        pygame.display.flip()#actualiza la superficie de visualizacion completa

#IDLE_cerrar ventana    
pygame.quit()