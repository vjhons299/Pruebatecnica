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
# Ubicar campos a ingresar
name=driver.find_element(By.XPATH, "//input[contains(@id,'full-name')]").send_keys("sebastián vargas")
mail=driver.find_element(By.XPATH, "//input[contains(@id,'email')]").send_keys("vjhons@hotmail.com")  
passw=driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Yaxo8145") 
passw_conf=driver.find_element(By.XPATH, "//input[@id='confirm-password']").send_keys("Yaxo8145") 
btn_signup=driver.find_element(By.XPATH, "//button[@type='submit']")
btn_signup.click()

#muestra que quedó registrado correctamente
print("registrado correctamente")
messagebox.showinfo("popup", "Registrado Correctamente")

time.sleep(tiempo)


   


