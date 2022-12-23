import palabras
import dibujos
print('El juego del ahorcado')
palabra_secreta = palabras.seleccionar_palabra()
print(f'Trata de adivinar las {len(palabra_secreta)} letras\n')

letra_ingresada=[]
vidas = 4
palabra_en_elementos =[]
for letra in range(len(palabra_secreta)):
    palabra_en_elementos.append('_ ')

usadas = len(palabra_secreta)
while usadas > 0 and vidas >0:
    print(f'Tienes {vidas} vidas y las letras que has ingresado son {"_".join(letra_ingresada)}')
    print("".join(palabra_en_elementos))

    letra_jugador = input('Ingresa un letra: ')

    for i in range(len(palabra_secreta)):
        if letra_jugador == palabra_secreta[i]:
            palabra_en_elementos[i] = letra_jugador.upper() + " "
    if letra_jugador in letra_ingresada:
        print('Esa letra ya la usaste, ingresa otra letra')
    else:
        letra_ingresada.append(letra_jugador)
        if letra_jugador in palabra_secreta:
            usadas= usadas - palabra_secreta.count(letra_jugador)
            print(f'La letra {letra_jugador}, si esta {palabra_secreta.count(letra_jugador)}')
        else:
            vidas -= 1
            if vidas == 3:
                dibujos.vida1()
            elif vidas == 2:
                dibujos.vida2()
            elif vidas == 1:
                dibujos.vida3()
            print(f'La letra {letra_jugador}, no se encuentra en la palabra secreta')
if vidas == 0:
    print(f'Ya no tienes vidas la palabra secreta es {palabra_secreta}')
    dibujos.vida4()
else:
    print(f'Felicidades adivnaste la palabra secreta')

    



