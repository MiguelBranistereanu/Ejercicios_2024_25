#Dividimos el texto en palabras

def espliteador():
    frase=raw_input("Digame algo inteligente: ")
    nueva_frase=frase.split(',') #El car�cter para que lo parta seg�n aparezca
    print(nueva_frase)

espliteador()
