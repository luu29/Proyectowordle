import random
from traceback import format_exc 
import colorama
from colorama import Fore
colorama.init(autoreset=True)
#ETAPA 1
if __name__ == "__main__":
    archivo = open("listado.txt")
    palabras = []
    #print(">>> FILTRANDO PALABRAS DE 5 LETRAS")
    #print("### se realiza el proceso del filtrado de palabras ###")
    for i in range(1290):
        lineas = archivo.readline()
        if len(lineas) == 6:
            palabras.append(lineas.rstrip())
    #print(palabras)
    #print(">>> OPERACIÓN COMPLETADA CON EXITO")
  
    primero = ">>> SE ENCONTRARON "
    segundo = len(palabras)
    tercero = " PALABRAS DE 5 LETRAS"
    frase = (str(primero) + str(segundo) + str(tercero))
    #print(frase)


#ETAPA 2
    
    
   # palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
    
    #while palabra not in palabras:
     #   if palabra.isalpha:
       #     print("!!! ERROR: La palabra introducida contiene caracteres que no son letras. Por favor vuelva a ingresar una palabra.")
        #if len(palabra) != 5:
         #   print("!!! ERROR: La palabra introducida tiene una cantidad incorrecta de caracteres. Por favor vuelva a ingresar una palabra.")
       # print("!!! ERROR: La palabra introducida no pertenece a la lista. Por favor vuelva a ingresar una palabra.")
       # palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")


#ETAPA 3

#para iniciar colorama
for intentos in range(1,5):
    intentos = 5
    print("TIENES " + str(intentos) + " INTENTOS")
    random1 = random.choice(palabras)
    for a in range(1, 7):
        palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
        while palabra not in palabras:
            print(Fore.RED + "!!! ERROR: La palabra introducida no pertenece a la lista. Por favor vuelva a ingresar una palabra.")
            if len(palabra) != 5:
                print(Fore.RED + "!!! ERROR: La palabra introducida tiene una cantidad incorrecta de caracteres. Por favor vuelva a ingresar una palabra.")
            if palabra.isalpha() == False:
                print(Fore.RED + "!!! ERROR: La palabra introducida contiene caracteres que no son letras. Por favor vuelva a ingresar una palabra.")
            palabra = input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:")
        for i in range(len(palabra)):
            if palabra[i] == random1[i]:
                print(Fore.GREEN + palabra[i],end=" ")
            elif palabra[i] in random1:
                print(Fore.YELLOW + palabra[i],end=" ")
            else:             
                print(Fore.RED + palabra[i],end=" ")
        if intentos == 0:
            print(" ")
            print(Fore.RED + "NO TIENES MÁS INTENTOS, PERDISTE")
        else:
            intentos = intentos - 1
            print(" ")
            print("TE QUEDAN " + str(intentos) + " INTENTOS")
            print(" ")
    break
