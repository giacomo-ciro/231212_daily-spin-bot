from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def draw_timestamp(img_PATH):

    img = Image.open(img_PATH)
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    font = ImageFont.truetype("arial.ttf", 30)
    
    draw = ImageDraw.Draw(img)
    text_width = draw.textlength(current_date_time, font)
    position = ((img.width - text_width) // 2, 10)
    draw.text(position, current_date_time, fill=(255, 255, 255), font=font)
    img.save(img_PATH)
    
    return


def spin(USERNAME, PASSWORD, PATH = "", screenshot = False):
    
    driver = webdriver.Chrome()
    driver.get('https://www.snai.it/giochi/Daily-spin')
    # driver.get('https://www.snaigiochi.it/casual/login/?skin=SNAI&mobile=1&gioco=DAILYSPIN&a=oooo&openExtMode=1&id_network=1&prodotto=casual')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@id, "cookie_consent_banner_closer")]'))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "registerGhostButtonHeader")]'))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@placeholder, "Username")]'))).send_keys(USERNAME)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@placeholder, "Password")]'))).send_keys(PASSWORD)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@placeholder, "Password")]'))).send_keys(Keys.ENTER)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "gameButton")]//a'))).click()
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame(0)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "pulsazione")]')))
    print('Login successful.')
    
    if screenshot:
        fileName = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f'{PATH}/{fileName}.png')
        draw_timestamp(f'{PATH}/{fileName}.png')
        print(f'Saved to "{PATH}" as "{fileName}.png"')

    return
