#Dulce Herrera
print("""¿Cuántos números capicúa?
°°°°°°°°°°°°°°°°°°°°°°°°°
Ingrese un número positivo del 1 al 100,000.\n""")
numero_usuario=int(input("Ingrese el número: "))
final=100000
capicua_almacenamiento=[]
for capicua in range(numero_usuario,final+1):
    cadena=str(capicua) 
    reverso=cadena[::-1]
    if cadena==reverso:
        capicua_almacenamiento.append(capicua)
print(capicua_almacenamiento)   
print("el numero ingresado tiene %s digitos capicúa" % len(str(capicua_almacenamiento)))