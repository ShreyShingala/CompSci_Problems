import pyautogui
import time

time.sleep(3)

items = []

for item in items:
    pyautogui.typewrite(item)
    pyautogui.press("enter")
    time.sleep(0.5)

print("Script completed.")
