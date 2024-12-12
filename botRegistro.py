from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time 


# Ingresamos a Google
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://katalon-demo-cura.herokuapp.com/#summary')


# ------------------------------------------------  -------------------

# Aplicar su lógica para la extracción de las capitales de los países.


try:

    botonInicio = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    botonInicio.send_keys(Keys.ENTER)

    # Formulario 1
    campo_nomUsuario = driver.find_element(By.XPATH, "//input[@id='txt-username']")
    campo_nomUsuario.send_keys(str('John Doe'))

    campo_contrasena = driver.find_element(By.XPATH, "//input[@id='txt-password']")
    campo_contrasena.send_keys(str('ThisIsNotAPassword'))

    botonLogin = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    botonLogin.send_keys(Keys.ENTER)

    # Formulario 2
    menu_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='combo_facility']"))
    menu_dropdown.select_by_index(1)

    botonCheckbox = driver.find_element(By.XPATH, "//input[@id='chk_hospotal_readmission']")
    botonCheckbox.click()

    botonCheckboxNone = driver.find_element(By.XPATH, "//input[@id='radio_program_none']")
    botonCheckboxNone.click()

    inputFecha = driver.find_element(By.XPATH, "//input[@id='txt_visit_date']")
    inputFecha.click()

    dia = driver.find_element(By.XPATH, "//td[text()='15']")
    dia.click()
    
    comentarioTextarea = driver.find_element(By.XPATH, "//textarea[@id='txt_comment']")
    comentarioTextarea.send_keys(str('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'))

    botonEnviar = driver.find_element(By.XPATH, "//button[@id='btn-book-appointment']")
    botonEnviar.send_keys(Keys.ENTER)

    # Ultimo boton
    botonFinal = driver.find_element(By.XPATH, "//a[@class='btn btn-default']")
    botonFinal.send_keys(Keys.ENTER)

    time.sleep(10)


finally:
    
     driver.quit()
   

