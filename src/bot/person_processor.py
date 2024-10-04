import time

from bot.form_filler import fill_input_field, handle_hcaptcha
from bot.error_handler import handle_error, handle_error_anti_robot
from entities.output_person import OutputPerson
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_output_person(driver):
    return OutputPerson(
        cpf=driver.find_element(By.XPATH, '//*[@id="mainComp"]/div[2]/p/span[1]/b').text,
        name=driver.find_element(By.XPATH, '//*[@id="mainComp"]/div[2]/p/span[2]/b').text,
        birth_date=driver.find_element(By.XPATH, '//*[@id="mainComp"]/div[2]/p/span[3]/b').text,
        registration_status=driver.find_element(By.XPATH, '//*[@id="mainComp"]/div[2]/p/span[4]/b').text,
        registration_date=driver.find_element(By.XPATH, '//*[@id="mainComp"]/div[2]/p/span[5]/b').text,
        message='CPF Válido'
    )


def process_person(driver, input_person, sheet_output, attempts=0, max_attempts=3):
    if attempts >= max_attempts:
        print(f"Máximo de {max_attempts} tentativas atingido para CPF: {input_person.formatted_cpf()}")
        return

    cpf = input_person.formatted_cpf()
    birth_date = input_person.formatted_birth_date()

    if cpf is None or birth_date is None:
        return

    fill_input_field(driver, 'txtCPF', cpf)
    fill_input_field(driver, 'txtDataNascimento', birth_date)

    handle_hcaptcha(driver)
    
    btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'id_submit'))
    )
    btn.send_keys(Keys.ENTER)
    time.sleep(3)

    if handle_error_anti_robot(driver):
        print(f"Tentativa {attempts + 1} para CPF: {input_person.formatted_cpf()}")
        process_person(driver, input_person, sheet_output, attempts + 1)
        return

    if handle_error(driver, sheet_output, input_person, '//*[@id="content-core"]/div/div/div[1]/span/h4/b', 'Data de Nascimento Inválida'):
        return

    if handle_error(driver, sheet_output, input_person, '//*[@id="content-core"]/div/div/div[1]/span/h4', 'CPF Inválido'):
        return

    output_person = extract_output_person(driver)

    sheet_output.append([
        output_person.cpf, output_person.name, output_person.birth_date,
        output_person.registration_status, output_person.registration_date, output_person.message
    ])
