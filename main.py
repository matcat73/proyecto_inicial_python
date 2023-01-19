
import csv
import random
import interfaz


def leer_palabra_secreta(csvfilename):
    csvfile = open(csvfilename, "r")
    file_data = list(csv.DictReader(csvfile))
    csvfile.close()
    palabras = []
    for i in file_data:
        palabras.append(i['palabras'])

    palabra_random = random.choice(palabras)
    return palabra_random


def pedir_letra(letras_usadas):
    
    # Listado de letras autorizadas
    letras_aceptadas = 'abcdefghijklmnñopqrstuvwxyz'

    while True: 
        # Valor que se utiliza para cortar el bucle
        exito = 1

        # Se solicita el ingreso de una nueva letra
        letra = str(input('Ingrese una nueva letra:'))
        letra = letra.lower()

	    # Se verifica que el largo de letra_solicitada no sea mayor que 1
        if len(letra) > 1:
            exito = 0
	
        # Se verifica si la letra ingresada es válida
        letra_valida = letras_aceptadas.find(letra)

        # Si la letra ingresada no es válida, se retorna FALSE
        if letra_valida == -1:
            exito = 0
    
        # Si la letra ingresada ya ha sido utilizada, se retorna FALSE
        if letra in letras_usadas:
            exito = 0
        
        if exito == 1:
            break
    letras_usadas.append(letra)
    return letra
    
    

def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True

    return False


def validar_palabra(letras_usadas, palabra_secreta):
    for i in palabra_secreta:
        if i not in letras_usadas:
            return False
    
    return True




if __name__ == '__main__':
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')
