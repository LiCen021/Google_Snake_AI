import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
options.add_argument("--no-first-run")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://googlesnakemods.com/v/current/")

# Define a function which check if "play" button is available
# hit play if it becomes available
def check_press_play_button():
    # Define a WebDriverWait
    wait = WebDriverWait(driver, 5)  # Wait some time
    try:
        # Wait for the button to be clickable
        button = wait.until(EC.element_to_be_clickable((By.XPATH,  "//div[@aria-label='Play']")))
        button.click()
    except TimeoutException:
        pass

def snake_move(direction_num):
    # Find the body of the page
    body_element = driver.find_element(By.TAG_NAME, 'body')
    if direction_num == 1:
        body_element.send_keys(Keys.ARROW_UP)
    elif direction_num == 2:
        body_element.send_keys(Keys.ARROW_DOWN)
    elif direction_num == 3:
        body_element.send_keys(Keys.ARROW_RIGHT)
    elif direction_num == 4:
        body_element.send_keys(Keys.ARROW_LEFT)

check_press_play_button()

# Define the number of second between each keyboard input
reaction_speed = 0.1 
check_press_play_button()
# Find the final score
snake_move(1)
time.sleep(reaction_speed)
snake_move(3)
time.sleep(reaction_speed)
snake_move(2)
time.sleep(reaction_speed)
snake_move(4)

check_press_play_button()

input("Press Enter to exit...")
# time.sleep(10)
# # Move the mouse to an absolute position
# pyautogui.moveTo(100, 150)

# # # Move the mouse relative to its current position
# pyautogui.move(0, 10)  # Move the mouse down 10 pixels

# # # Click the mouse at its current location
# # pyautogui.click()

# # # Right-click
# # pyautogui.click(button='right')

# # # Double-click
# # pyautogui.doubleClick()

# # # Scroll the mouse
# # pyautogui.scroll(200)  # Scroll up

# # Capture the screen
# screen = np.array(ImageGrab.grab())
# # Convert the screen capture to a format OpenCV can work with
# screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

# # Convert to grayscale
# gray_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

# # Show the grayscale screen
# cv2.imshow('Grayscale Screen Capture', gray_screen)

# # Wait for a key press to close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()
