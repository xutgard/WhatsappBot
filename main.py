from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

with open("message.txt", "r") as file:
    msg = quote(file.read())

numbers = []
with open("numbers.txt", "r") as file:
    for num in file.readlines():
        numbers.append(num.rstrip())  # rstrip /n deletes

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.maximize_window()  # Tarayıcı penceresini tam boyuta getir




link = "https://web.whatsapp.com/"
driver.get(link)
time.sleep(15)

# WhatsApp QR kodunu tarayarak giriş yapın ve bekle
input("QR kodunu tarayarak giriş yaptıktan sonra ENTER tuşuna basın:")

for num in numbers:
    link2 = f"https://web.whatsapp.com/send/?phone=90{num}&text={msg}"
    driver.get(link2)
    time.sleep(5)
    action=ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(5)

time.sleep(2000)
# Selenium oturumunu kapat
driver.quit()
