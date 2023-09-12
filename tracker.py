import exit
import time
import pyautogui
import keyboard


def mi_funcion():
    pos = pyautogui.position()
    print(f"Posición del ratón (x,y): {pos}")
    print(f"Color del pixel (r,g,b): {pyautogui.pixel(pos.x, pos.y)}")
    print(f"Color del pixel (r,g,b): {pyautogui.pixel(1275, 1017)}")


print("Iniciando Tracker...")
time.sleep(2)
print(f"Tamaño de la pantalla: {pyautogui.size()}")
time.sleep(1)
print("Tracker Iniciado")
print("SITUA EL RATÓN DONDE QUIERAS Y PULSA ALT PARA CONOCER LA POSICIÓN DEL RATÓN - PULSA F10 PARA DETENER EL PROGRAMA")


keyboard.add_hotkey('alt', mi_funcion)

keyboard.wait()
