#Dulce Herrera
print("""   ¿Cuántos números capicúa?
    °°°°°°°°°°°°°°°°°°°°°°°°°""")
while True:
    def n_capicua():
        print("Ingrese un número positivo del 1 al 100,000.\n")
        numero_usuario=int(input("Ingrese el número: "))
        final=100000
        capicua_almacenamiento=[]
        for capicua in range(numero_usuario,final+1):
            cadena=str(capicua) 
            reverso=cadena[::-1]
            if cadena==reverso:
                capicua_almacenamiento.append(capicua)#lo agregara al final de la lista
            else:
                print("No es un número positivo")
        print(capicua_almacenamiento)#mostrar lista de los numero capicua 
        print("el número ingresado tiene %s digitos capicúa" % len(capicua_almacenamiento))#devuelve el numero de elementos en una lista
        
    si=input("Agregar número s/n: ")
    if si=="s":
       n_capicua() 
    else:
        break
