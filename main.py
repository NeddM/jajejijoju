# Nedd Chairi Muñoz
# https://github.com/NeddM

from os import system, name
import pyautogui
import keyboard
import time

textoComandos = """
Pulsa "o" para parar el bot.
Pulsa "i" para reanudar el bot.
Pulsa "p" para salir del bot.
"""

textoActivado = """
- - - - - - - - - - - - - -
- ¡AUTOCLICKER ACTIVADO!  -
- - - - - - - - - - - - - -
"""

textoDesctivado = """
- - - - - - - - - - - - - - -
- ¡AUTOCLICKER DESACTIVADO! -
- - - - - - - - - - - - - - -
"""

textoSalir = "Ha salido de Autoclicker."


def limpiarConsola():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def farmea():
    limpiarConsola()
    print(textoActivado)
    print(textoComandos)
    while True:
        time.sleep(5)
        pyautogui.write('trivNextPage()', interval=0)
        pyautogui.press('enter') # Press the Ctrl-C hotkey combination.

        if keyboard.is_pressed('o'):
            noFarmea()
            break
        elif keyboard.is_pressed("p"):
            limpiarConsola()
            print(textoSalir)
            break


def noFarmea():
    limpiarConsola()
    print(textoDesctivado)
    print(textoComandos)
    while True:
        if keyboard.is_pressed('i'):
            farmea()
            break
        elif keyboard.is_pressed('p'):
            limpiarConsola()
            print(textoSalir)
            break


if __name__ == "__main__":
    noFarmea()
