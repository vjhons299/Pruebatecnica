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
tiempo=5
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

#agregamos tiempo para que pueda visualizarse la foto de perfil
time.sleep(2)

# Identificar y hacer clic en la foto de perfil
profile_picture = driver.find_element(By.CSS_SELECTOR, "img[src='/assets/rengoku.webp']")
profile_picture.click()

#Esperar a que se despliegue el botón de cerrar sesión
time.sleep(2)
logout_button = driver.find_element(By.XPATH, "//a[contains(.,'Logout')]")

# Hacer clic en el botón de cerrar sesión
logout_button.click()

#muestra pop up indicando que se cerro sesión correctamente
messagebox.showinfo("popup", "se cerro sesión correctamente")


time.sleep(tiempo)


   


