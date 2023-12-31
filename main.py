import exit
import time
import pyautogui
from mode_selector import select_mode
from movement_functions import *
import json

mode = select_mode()
time.sleep(5)

with open('2K.json') as json_file:
    data = json.load(json_file)

if mode == 1:
    # Seleccionar modo coop y buscar partida
    coop_select(data)

    # Esperar a que salte partida y aceptarla
    accept_match(data)

    # Escribir y seleccionar champ
    write_champ("kaisa", data)

    # Esperar la aparición en grieta
    waiting_game(data)

    in_game(data)

    print("FIN")

elif mode == 2:
    print("2")