import time
import pyautogui
import pygetwindow as gw
import threading

titulo_ventana = "League of Legends (TM) Client"



def coop_select(data):
    pyautogui.click(x=data["play"]["x"], y=data["play"]["y"])
    time.sleep(1)
    pyautogui.click(x=data["coop"]["x"], y=data["coop"]["y"])
    time.sleep(1)
    pyautogui.click(x=data["confirm"]["x"], y=data["confirm"]["y"])
    time.sleep(5)
    pyautogui.click()


def accept_match(data):
    while not pyautogui.pixelMatchesColor(data["accept"]["x"], data["accept"]["y"], (30, 37, 42)):
        print("Buscando partida...")
        time.sleep(0.5)

    print("Partida encontrada")
    pyautogui.click(x=data["accept"]["x"], y=data["accept"]["y"])
    time.sleep(0.5)
    pyautogui.moveTo(data["champ_select"]["x"], data["champ_select"]["y"])
    check_champ(data)


def check_champ(data):
    tiempo = 0
    while not pyautogui.pixelMatchesColor(data["champ_select"]["x"], data["champ_select"]["y"], (240, 230, 210)):
        print("Esperando aceptación...")

        if tiempo >= 10:
            accept_match(data)

        tiempo = tiempo+0.5
        time.sleep(0.5)

    print("En champ select")
    

def write_champ(name, data):
    time.sleep(1)
    pyautogui.click(x=data["search_champ"]["x"], y=data["search_champ"]["y"])
    time.sleep(0.5)
    pyautogui.write(name)
    time.sleep(0.5)
    pyautogui.click(x=data["clic_champ_icon"]["x"], y=data["clic_champ_icon"]["y"])
    time.sleep(0.5)
    pyautogui.click(x=data["lock_champ"]["x"], y=data["lock_champ"]["y"])


def waiting_game(data):
    while not pyautogui.pixelMatchesColor(data["game_detection"]["x"], data["game_detection"]["y"], (0, 0, 0)):
        print("Cargando partida...")
        time.sleep(0.5)

    print("Partida cargada")


def in_game(data):
    global hilo_hola_activo
    hilo_hola_activo = True

    hilo_verificar_ventana = threading.Thread(target=verificar_ventana)

    # Inicia ambos hilos
    hilo_verificar_ventana.start()

    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.press('f2')

    while hilo_hola_activo:
        pass

        


def verificar_ventana():
     global hilo_hola_activo
     while True:
        time.sleep(1)
        ventanas = gw.getWindowsWithTitle(titulo_ventana)
        # Verifica si se encontraron ventanas con ese título
        if ventanas:
            # La ventana está abierta
            print(f"La ventana '{titulo_ventana}' está abierta.")
        else:
            # La ventana no está abierta
            print(f"La ventana '{titulo_ventana}' no está abierta.")
            hilo_hola_activo = False
            time.sleep(4)
            pyautogui.press('esc')
            break

        
