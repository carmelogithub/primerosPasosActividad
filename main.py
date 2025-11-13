""" La primera función se llamará texto.
Esta función tiene una variable llamada carta en donde pone “en un lugar de la mancha”
Se pinta la frase por consola
se pinta la letra que está en la posición 10
y se pinta la frase al revés """
def texto():
    carta = "en un lugar de la mancha"
    print(carta)
    print(carta[10])
    print(carta[::-1])
texto()

""" La segunda función se llama calculo
tienes dos variables, a y b
a = 10
b= 5
Muestra la división y la suma de las dos
Además muestra b elevado a 3 """
def calculo():
    a,b = 10,5 #definimos las variables
    print("División:", a // b) #división entera // o division decimal /
    print("Suma:", a + b)
    print("b elevado a 3:", b ** 3)
calculo()
""" La tercera función se llama grupos
Tenemos una lista llamada jugadores y pone messi, cristiano, pelé y maradona.
muestra las jugadores en orden alfabético
añade zidane al final y lo muestras """
def grupos():
    jugadores = ["messi", "cristiano", "pelé", "maradona"]
    jugadores.sort() #ordenar la lista
    print("Jugadores en orden alfabético:", jugadores)
    jugadores.append("zidane") #añadir al final
    print("Lista después de añadir a zidane:", jugadores)
grupos()
    