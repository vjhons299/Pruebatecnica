# Importa la clase webdriver
from selenium import webdriver
# Importar time para poder usar el sleep
import time
#
import re
#importar By para poder usar los Xpath de la página
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#importar librerias para mostrar popup
import tkinter as tk
from tkinter import messagebox

#variable tiempo para mantener la pestaña abierta
tiempo=5
# Inicializa un objeto Chrome (navegador) 
driver=webdriver.Chrome()
# Abre la página web en el navegador
driver.get("https://test-qa.inlaze.com/auth/sign-in")
# Agrandar pantalla
driver.maximize_window()
time.sleep(2)

# Encontrar y enviar contraseña
password_input = driver.find_element(By.XPATH, "//input[contains(@id, 'password')]")
#Ingresar contraseña
password_input.send_keys("Yaxo8145")
time.sleep(2)
contraseña = password_input.get_attribute("value")

longitudmin = 7
longitudmax = 20

#If para validar la longitud, se muestra contraseña solo para mostrar que está usando el texto enviado

if len(contraseña) < longitudmin or len(contraseña) > longitudmax:
    print("La contraseña", contraseña, "no cumple con la longitud mínima o máxima requerida.")    
else:
    print("La longitud de la contraseña es válida.")


# Verificar que la contraseña cumple con los requisitos una mayuscula y al menos un nmero
if not re.search(r"[A-Z]", contraseña) or not re.search(r"[0-9]", contraseña):
    print("La contraseña ", contraseña, " no cumple con los requisitos de caracteres.")
    
else:
    print("La contraseña cumple con los requisitos de caracteres.")