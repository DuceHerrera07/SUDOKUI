#Importar libreria
import pygame#libreria para hacer juegos en dos dimensiones
import tkinter as tk #blioteca grafica (GUI)
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
        ven.geometry('1500x910')#dimension de ventana
        ven.title('Reglas de sodoku clásico')#titulo
        ven.iconbitmap(r"instruccion.ico")#icono
        ven.configure(bg="black")#color de fondo
        inst=Label(ven,text="Instrucción",bg="white")
        inf=Label(ven,text="Al hacer clic en un boton del tablero",bg="white")
        inf1=Label(ven,text="podra decidir las cordenas de sus",bg="white")
        inf2=Label(ven,text="barcos, cuando estos esten asignados",bg="white")
        inf3=Label(ven,text="correctamente se mostraran de color marron.",bg="white")
        m=Label(ven,text="Cierre esta ventana para continuar",bg="white")
        #para que se muestren en pantalla las variables anteriores que son str, columna y fila en la que apareceran
        inst.grid(column=11,row=2)
        inf.grid(column=11,row=3)
        inf1.grid(column=11,row=4)
        inf2.grid(column=11,row=5)
        inf3.grid(column=11,row=6)
        m.grid(column=11,row=7)
        salir=tk.Button(ven,text="Entendido")
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
    #editado por wilson Armando
    #cada fila debe contener los digitos de 1 al 9 sin repeticdión 
    def chequeo_filas(self,chequear_lista="todo el tablero");
     if chequear_lista =="todo el tablero":
         chequear_lista == self.tablero
     for fila in self.tablero
        for elemento in fila:
            if elemento != "0":
                assert fila.count(elemento) ==1, " tablero no valido"
                
                
    def chequeo_columnas (self):
        for columna_index in range(0.9):
            for row_index in range(0.9):
                self.lista_invertida.append(self.tablero[row_index][columna_index])
 
 
        self.chequeo_filas([self.lista_invertida])  
        self.lista_invertida.clear() 
    

                                         
        #rapidez de actualizacion de pantalla
        reloj.tick(60)
        pygame.display.update()#activa todo lo que este sobre pantalla sin ello no se ejecuta
        pygame.display.flip()#actualiza la superficie de visualizacion completa
        chequeo_filas() # estoy llamando a la funcion de rrepetición de filas 
        chequeo_columnas() #llamando a la funcion de repeticion de  columnas 

#IDLE_cerrar ventana    
pygame.quit()
