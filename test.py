import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_driver import get_chromedriver

from twocaptcha import TwoCaptcha
from config import config
from recaptcha import get_recaptchaV2_token


driver = get_chromedriver(use_proxy=True)


url = 'https://lessons.zennolab.com/captchas/'

driver.get(url)


data_sitekey = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.XPATH, "//a[contains(@href,'/captchas/recaptcha/v2_nosubmit.php?level=high')]"))).click()

sitekey = driver.find_elements(By.XPATH, "//script[@type='text/javascript']")[
    1].get_attribute("innerHTML").strip()[61:-2]

driver.execute_script("document.getElementById('g-recaptcha-response').style.display = 'block';")

token = get_recaptchaV2_token(sitekey, url)

driver.execute_script(f"___grecaptcha_cfg.clients['0']['V']['V']['callback']('{token}');")

print(token)
print("done")

sleep(10000)
