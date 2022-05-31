import random
from traceback import format_exc 
import colorama
from colorama import Fore
colorama.init(autoreset=True)

#ETAPA 1
if __name__ == "__main__":
    archivo = open("listado.txt")
    palabras = []
    print(">>> FILTRANDO PALABRAS DE 5 LETRAS")
    print("### se realiza el proceso del filtrado de palabras ###")
    for i in range(1290):
        lineas = archivo.readline()
        if len(lineas) == 6:
            palabras.append(lineas.rstrip())
    #print(palabras)
    print(">>> OPERACIÓN COMPLETADA CON EXITO")
  
    primero = ">>> SE ENCONTRARON "
    segundo = len(palabras)
    tercero = " PALABRAS DE 5 LETRAS"
    frase = (str(primero) + str(segundo) + str(tercero))
    print(frase)


    #ETAPA 2
    def selectRandom(palabras):
        return print("PALABRA ELEGIDA AL AZAR: ", random.choice(palabras))
    
    palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
    
    while palabra not in palabras:
        if palabra.isalpha:
            print("!!! ERROR: La palabra introducida contiene caracteres que no son letras. Por favor vuelva a ingresar una palabra.")
        if len(palabra) != 5:
            print("!!! ERROR: La palabra introducida tiene una cantidad incorrecta de caracteres. Por favor vuelva a ingresar una palabra.")
        print("!!! ERROR: La palabra introducida no pertenece a la lista. Por favor vuelva a ingresar una palabra.")
        palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
      
 
#ETAPA 3

#para iniciar colorama
random1 = random.choice(palabras)
for a in range(1, 7):
    palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
    while palabra not in palabras:
        if palabra.isalpha:
            print("!!! ERROR: La palabra introducida contiene caracteres que no son letras. Por favor vuelva a ingresar una palabra.")
        if len(palabra) != 5:
            print("!!! ERROR: La palabra introducida tiene una cantidad incorrecta de caracteres. Por favor vuelva a ingresar una palabra.")
        print("!!! ERROR: La palabra introducida no pertenece a la lista. Por favor vuelva a ingresar una palabra.")
        palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
    for i in range(len(palabra)):
        if palabra[i] == random1[i]:
            print(Fore.GREEN + palabra[i])
        elif palabra[i] in random1:
            print(Fore.YELLOW + palabra[i])
        else:             
            print(Fore.RED + palabra[i])
        print("¡¡GANASTE!!")
