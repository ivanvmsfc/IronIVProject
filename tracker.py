import exit
import time
import pyautogui
import keyboard
from time import sleep
from win32gui import FindWindow, GetWindowRect

client_title = "League of Legends"
game_client_title = "League of Legends (TM) Client"


def size(window_title):
    window_handle = FindWindow(None, window_title)
    window_rect = GetWindowRect(window_handle)
    return window_rect[0], window_rect[1], window_rect[2], window_rect[3]


def print_ratios(window_title):
    p = pyautogui.position()
    x1, y1, x2, y2 = size(window_title)
    rx = (p[0] - x1) / (x2 - x1)
    ry = (p[1] - y1) / (y2 - y1)
    print("({}, {})".format(round(rx, 4), round(ry, 4)))


def mi_funcion():
    pos = pyautogui.position()
    print(f"Posición del ratón global (x,y): {pos}")

    try:
        print(f"Ratio (x,y): {print_ratios(game_client_title)}")    
    except:
        print("LoL no está abierto")

    print(f"Color del pixel (r,g,b): {pyautogui.pixel(pos.x, pos.y)}")


print("Iniciando Tracker...")
time.sleep(2)
print(f"Tamaño de la pantalla: {pyautogui.size()}")
time.sleep(1)
print("Tracker Iniciado")
print("SITUA EL RATÓN DONDE QUIERAS Y PULSA ALT PARA CONOCER LA POSICIÓN DEL RATÓN - PULSA F10 PARA DETENER EL PROGRAMA")


keyboard.add_hotkey('alt', mi_funcion)

keyboard.wait()
