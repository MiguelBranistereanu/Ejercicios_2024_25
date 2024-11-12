#Dividimos el texto en palabras

def espliteador():
    frase=raw_input("Digame algo inteligente: ")
    nueva_frase=frase.split(',') #El carácter para que lo parta según aparezca
    print(nueva_frase)

espliteador()
