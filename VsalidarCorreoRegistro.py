# Importa la clase webdriver
from selenium import webdriver
# Importar time para poder usar el sleep
import time

import re
#importar By para poder usar los Xpath de la página
from selenium.webdriver.common.by import By
#importar librerias para mostrar popup
import tkinter as tk
from tkinter import messagebox



#variable tiempo para mantener la pestaña abierta
tiempo=3
# Inicializa un objeto Chrome (navegador) 
driver=webdriver.Chrome()
# Abre la página web en el navegador
driver.get("https://test-qa.inlaze.com/auth/sign-up")
# Agrandar pantalla
driver.maximize_window()
time.sleep(2)
# Ubicar campos a ingresar
mail=driver.find_element(By.XPATH, "//input[contains(@id,'email')]")
#Ingresar correo
mail.send_keys("vjhons299@gmail.com")  

email= mail.get_attribute("value")
# Expresión regular para validar la estructura de un correo electrónico
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Validar la estructura del correo electrónico
if re.match(pattern, email):
    print("El correo ", email, " tiene una estructura válida.")
    messagebox.showinfo("popup","El correo  tiene una estructura válida.")
else:
    print("El correo ", email, " no tiene una estructura válida.")
    messagebox.showinfo("popup","El correo no tiene una estructura válida.")
time.sleep(tiempo)


   


