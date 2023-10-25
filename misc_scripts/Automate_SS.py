#REMEMBER TO GIVE PERMS, FAILUREEEEE
import os
from pynput import mouse, keyboard
import pyautogui


x, y = pyautogui.size()

x = 2560/x
y = 1600/y

# Folder to save screenshots
screenshot_folder = "ants"

# Create the screenshot folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.mkdir(screenshot_folder)

# Variable to store screenshot number
screenshot_number = 1

# Variable to store the top-left and bottom-right coordinates
top_left = None
bottom_right = None

# Function to take a screenshot and save it with a custom name
def take_screenshot():
    #try:
        global screenshot_number, top_left, bottom_right
        if top_left is not None and bottom_right is not None:
            screenshot_name = f"{screenshot_folder}/screenshot_{screenshot_number}.png"
            screenshot_number += 1
            x1 = top_left[0] * x
            y1 = top_left[1] * y
            x2 = bottom_right[0] * x
            y2 = bottom_right[1] * y
            screenshot = pyautogui.screenshot(region=(x1, y1, (x2-x1)* (2.2/x), (y2-y1)* (2.2/y)))
            screenshot.save(screenshot_name)
            top_left = bottom_right = None
    #except:
    #    print("Error taking screenshot.")

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    global top_left, bottom_right
    if pressed:
        if top_left is None:
            top_left = pyautogui.position()
            print("Top-left corner set.")
        else:
            bottom_right = pyautogui.position()
            print("Bottom-right corner set.")
            take_screenshot()

# Function to handle keypress events
def on_key_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop the listener

# Set up mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Set up keyboard listener
with keyboard.Listener(on_release=on_key_release) as listener:
    print("Screenshot automation started. Click on two points to capture a screenshot. Press 'Esc' to exit.")
    listener.join()

mouse_listener.stop()
print("Screenshot automation terminated.")
