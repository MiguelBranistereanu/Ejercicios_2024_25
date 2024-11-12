#Uso del método format()

def formateador():
    nombre=raw_input("NOMBRE: ")
    edad=raw_input("EDAD: ")
    frase="Buenos dias, me llamo () y tengo () años".format(nombre,edad)
    print(frase)

formateador()
