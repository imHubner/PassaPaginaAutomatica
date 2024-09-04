import pyautogui
import time
import random

# Função para clicar em uma posição específica
def click_position(x, y):
    pyautogui.click(x, y)

# Definir a posição onde deseja clicar (substitua com suas coordenadas)
x_pos, y_pos = 1750, 500

# Loop para clicar a cada intervalo de tempo aleatório, dentro de uma media de "x" segundos
while True:
    delay = random.randint(70, 110)  # Define um tempo aleatório entre 70 e 115 segundos
    time.sleep(delay)  # Espera o tempo aleatório antes de clicar
    click_position(x_pos, y_pos)
    print(f"Clicado em ({x_pos}, {y_pos}) após {delay} segundos")
