import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button1 = browser.find_element_by_id("book")
button1.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id("input_value").text
print(x)
y = calc(int(x))

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
button = browser.find_element_by_id("solve")
button.click()

alert = browser.switch_to.alert
alert.accept()

time.sleep(5)

browser.quit()