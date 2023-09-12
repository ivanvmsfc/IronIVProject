import time
import pyautogui
import keyboard

x = 0

def mi_funcion1():
    global x
    
    x = 1
    return x

def mi_funcion2():
    global x
    
    x = 2
    return x

def select_mode():
    print("Iniciando bot...")
    global x
    
    time.sleep(1.5)
    print("Pulsa 1 para MODO LEVEO | Pulsa 2 para MODO RANKEDS")

    keyboard.add_hotkey('1', mi_funcion1)
    keyboard.add_hotkey('2', mi_funcion2)
    1
    while True:
        if x==1:
            print("MODO LEVEO SELECCIONADO")
            break
        elif x==2:
            print("MODO LEVEO SELECCIONADO")
            break
    
    print("Tienes 5 segundos para mostrar en pantalla el LoL")
    return x

