def cuadrados():
    n_filas=int(input("De que tamaño quieres el cuadrado (1-10) "))
    #Esto es un buvle animado(nested)
    for filas in range(1,n_filas+1):
        for col in range(1,filas+1):
            print('* ',end='')
            print(" ") #/n hace un salto de linea

cuadrados()
