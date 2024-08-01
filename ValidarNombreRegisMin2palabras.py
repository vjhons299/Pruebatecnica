# Importa la clase webdriver
from selenium import webdriver
# Importar time para poder usar el sleep
import time
#importar By para poder usar los Xpath de la página
from selenium.webdriver.common.by import By
#importar librerias para mostrar popup
import tkinter as tk
from tkinter import messagebox



#variable tiempo para mantener la pestaña abierta
tiempo=5
# Inicializa un objeto Chrome (navegador) 
driver=webdriver.Chrome()
# Abre la página web en el navegador
driver.get("https://test-qa.inlaze.com/auth/sign-up")
# Agrandar pantalla
driver.maximize_window()
time.sleep(2)
# Ubicar campos a nombre
name=driver.find_element(By.XPATH, "//input[contains(@id,'full-name')]")
name.send_keys("sebastián")

# Separar el texto del campo de nombre en palabras
nombre = name.get_attribute("value")
#usamos split para crear una lista con cada palabra y almacenarlas en palabras
palabras = nombre.split()

# Verificar si hay al menos dos palabras, usamos el len para usar la cantidad de palabras que se almaceno
if len(palabras) < 2:
    print("El campo de nombre debe contener al menos dos palabras.")
    messagebox.showinfo("popup", "El campo de nombre debe contener al menos dos palabras.")
else:
    print("el campo contiene 2 o más palabras")
    messagebox.showinfo("popup", "el campo contiene 2 o más palabras")


time.sleep(tiempo)


   


