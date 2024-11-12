#Vamos a hacer un ejercio que genere al azar un número entre 1 y 6.
import random
import time

def dado():
    semilla=time.time()
    print("semilla= "+str(semilla))
    random.seed(semilla)
    respuesta=raw_input("¿Quieres que tire un dado 100 v(S/N)? ")
    while(respuesta=='S'):
        tirada=int((random.random()*10)%6)
        print("Ha salido un "+str(tirada))
        respuesta=raw_input("¿Quieres volver a tirar el dado (S/N)? ")
    print("Se acabó el juego")

dado()
