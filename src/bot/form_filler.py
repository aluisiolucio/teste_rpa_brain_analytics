import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_input_field(driver, field_id, value):
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, field_id))
    )
    input_field.send_keys(value)


def handle_hcaptcha(driver):
    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[contains(@src,'hcaptcha') and contains(@src,'checkbox')]")
        )
    )
    hcaptcha = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body"))
    )
    hcaptcha.click()
    
    time.sleep(2)
    driver.switch_to.default_content()


def new_query(driver):
    link = driver.find_element(By.XPATH, '//*[@id="idRodape"]/p[4]/a')
    link.click()
    
    time.sleep(3)
