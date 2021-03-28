from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import cred

PATH = 'C:\Program Files (x86)\chromedriver.exe'

productLink = ""

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://www.amazon.ca")

sigin = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "nav-link-accountList")))

sigin.click()

email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ap_email")))

email_input.send_keys(cred.amazonEmail)

continueButton = driver.find_element_by_id("continue")
continueButton.click()

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ap_password")))

password.send_keys(cred.amazonPass)

signin = driver.find_element_by_id("signInSubmit")
signin.click()

driver.get(productLink)

isComplete = False

while not isComplete:

    try:
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-button")))

    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        add_to_cart_button.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hlb-ptc-btn-native")))

        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input")))

        element.click()

        isComplete = True

    except:
        driver.get(productLink)
        print("Error - restarting bot")
        continue

print("Order successfully placed")
