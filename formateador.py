#Uso del m�todo format()

def formateador():
    nombre=raw_input("NOMBRE: ")
    edad=raw_input("EDAD: ")
    frase="Buenos dias, me llamo () y tengo () a�os".format(nombre,edad)
    print(frase)

formateador()