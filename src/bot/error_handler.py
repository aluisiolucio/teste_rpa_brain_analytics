from selenium.webdriver.common.by import By


def handle_error(driver, sheet_output, input_person, error_xpath, error_message):
    error_element = driver.find_elements(By.XPATH, error_xpath)
    if error_element:
        sheet_output.append([
            input_person.formatted_cpf(), '', input_person.formatted_birth_date(), '', '', error_message
        ])

        return True

    return False