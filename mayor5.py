#Leo cinco n�meros y me dice cu�l es el mayor
def mayor():
    mayor=0#inicializar la variable.
    for cont in range(1,6):
        numero=int(input("Dime un n�mero entero mayor que cero: "))
        if(numero>mayor):
            mayor=numero
    print("EL MAYOR ES "+str(mayor))

mayor()
