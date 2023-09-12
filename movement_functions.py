import time
import pyautogui


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
    check_champ(data)


def check_champ(data):
    tiempo = 0
    while not pyautogui.pixelMatchesColor(data["champ_select"]["x"], data["champ_select"]["y"], (30, 40, 45)):
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
    time.sleep(0.25)
    pyautogui.click(x=data["clic_champ_icon"]["x"], y=data["clic_champ_icon"]["y"])
    time.sleep(0.25)
    pyautogui.click(x=data["clic_select_champ"]["x"], y=data["clic_select_champ"]["y"])
