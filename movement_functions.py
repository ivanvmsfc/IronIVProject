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
        time.sleep(0.5)
    pyautogui.click(x=data["accept"]["x"], y=data["accept"]["y"])
    check_champ(data)


def check_champ(data):
    while True:
        if pyautogui.pixelMatchesColor(data["emote_select"]["x"], data["emote_select"]["y"], (30, 35, 40)):
            break
        