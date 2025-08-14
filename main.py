# wuolah-go - canjea tickets de wuolah de forma automatica

import pyautogui
import time
import threading
import keyboard
import sys
import random

def detectar_tecla(): # si pulso q se cierra el programa
    global detenerHilo # accesible a todo
    while True:
        if keyboard.is_pressed('q'):
            print("¡Tecla 'q' presionada! Saliendo del programa.")
            detenerHilo = True
            break


# flujo del main

detenerHilo=False # bandera para terminar

hilo_tecla = threading.Thread(target=detectar_tecla) # hilo diferente para lo de q
hilo_tecla.start()

time.sleep(10)
while (True): # bucle click - enter para sorteo
    #print("click raton")
    pyautogui.click()
    time.sleep(round(random.uniform(1, 1.5), 1))
    #print("click enter")
    pyautogui.press('enter')
    time.sleep(round(random.uniform(1, 1.5), 1))

    if detenerHilo == True:
        break

sys.exit()