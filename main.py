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
  print(palabras)
  print(">>> OPERACIÓN COMPLETADA CON EXITO")
  
  primero = ">>> SE ENCONTRARON "
  segundo = len(palabras)
  tercero = " PALABRAS DE 5 LETRAS"
  frase = (str(primero) + str(segundo) + str(tercero))
  print(frase)
#ETAPA 2
  import random 

  def selectRandom(palabras):
    return random.choice(palabras)
  print("PALABRA ELEGIDA AL AZAR: ", selectRandom(palabras))

  while palabra == input (">>> INTRODUCIR PALABRAS DE 5 LETRAS:"):
    if palabra in listado.txt:
      print("gracias")
    if len(palabra) != 5:
      print("!!! ERROR: La palabra introducida tiene una cantidad incorrecta de caracteres. Por favor vuelva a  ingresar una palabra.")
    
