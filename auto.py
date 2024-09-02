import pyautogui
import time

# Função para clicar em uma posição específica
def click_position(x, y):
    pyautogui.click(x, y)

# Definir a posição onde deseja clicar (substitua com suas coordenadas)
x_pos, y_pos = 1750, 470

# Loop para clicar a cada 130 segundos
while True:
    click_position(x_pos, y_pos)
    print(f"Clicado em ({x_pos}, {y_pos})")
    time.sleep(130)  # Espera 130 segundos antes de clicar novamente
