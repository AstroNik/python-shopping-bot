from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import cred

PATH = 'C:\Program Files (x86)\chromedriver.exe'

options = Options() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(PATH,options=options)


productLink = ""

driver.get(productLink)

isComplete = False

while not isComplete:
    try:
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "addToCartButton"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        add_to_cart_button.click()

        title_change = WebDriverWait(driver,10).until(
            EC.title_is("Best Buy Canada | Best Buy Canada")
        )

        driver.get("https://www.bestbuy.ca/en-ca/basket")

        con_to_checkout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]"))
        )

        con_to_checkout.click()

        username = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"username"))
        )

        username.send_keys(cred.bestBuyEmail)

        password = driver.find_element_by_id("password")
        password.send_keys(cred.bestBuyPass)

        sigin_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/div/button"))
        )

        sigin_button.click()

        cvv = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.ID,"cvv"))
        )

        cvv.send_keys(cred.cvv)

        place_order_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[6]/div[2]/div/div/div/section[2]/main/div[2]/section/section[1]/button"))
        )

        place_order_button.click()

        isComplete = True

    except:
        driver.get(productLink)
        print("Error - restarting bot")
        continue

print("Order successfully placed")
