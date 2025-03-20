import pyautogui
import time
import random

# Perguntar ao usuário onde deseja que o clique ocorra
input("Posicione o cursor onde deseja que o clique ocorra e pressione ENTER...")
x_pos, y_pos = pyautogui.position()
print(f"Posição selecionada: ({x_pos}, {y_pos})")

# Loop para clicar a cada intervalo de tempo aleatório
def click_position(x, y):
    pyautogui.click(x, y)

while True:
    delay = random.randint(80, 120)  # Define um tempo aleatório entre 70 e 110 segundos
    time.sleep(delay)  # Espera o tempo aleatório antes de clicar
    click_position(x_pos, y_pos)
    print(f"Clicado em ({x_pos}, {y_pos}) após {delay} segundos")
