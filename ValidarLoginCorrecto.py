# Importa la clase webdriver
from selenium import webdriver
# Importar time para poder usar el sleep
import time
#importar By para poder usar los Xpath de la página
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#importar librerias para mostrar popup
import tkinter as tk
from tkinter import messagebox




#variable tiempo para mantener la pestaña abierta
tiempo=10
# Inicializa un objeto Chrome (navegador) 
driver=webdriver.Chrome()
# Abre la página web en el navegador
driver.get("https://test-qa.inlaze.com/auth/sign-in")
# Agrandar pantalla
driver.maximize_window()

# Ubicar campo correo e ingresar campos
mail=driver.find_element(By.XPATH, "//input[contains(@id,'email')]").send_keys("vjhons299@gmail.com")
passw=driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("Yaxo8145")
btn_sign=driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Sign in')]")
btn_sign.click()

#muestra que quedó logeado correctamente
print("Logeado correctamente")
messagebox.showinfo("popup", "Logeado Correctamente")

time.sleep(tiempo)


   


