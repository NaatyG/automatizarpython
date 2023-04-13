'''Bibliotecas necessárias para realizar a automoção'''
import pyautogui
from time import sleep

'''Realizando a automatização do login e senha do usuário'''
pyautogui.click(685, 385, duration=1)
pyautogui.write('jhonatan')
pyautogui.click(690, 412, duration=1)
pyautogui.write('123456')
pyautogui.click(593, 440, duration=2)

'''Abrindo o arquivo.txt para leitura'''
with open('produtos.txt', 'r') as file:

    '''Para cada linha do arquivo...'''
    for line in file:
        product = line.split(',')[0]  # Variável produto
        amount = line.split(',')[1]  # Variável quantidade
        price = line.split(',')[2]  # Variável preço

        '''Automatizando o cadastro de produtos no sistema'''
        pyautogui.click(405, 371, duration=1)
        pyautogui.write(product)

        pyautogui.click(404, 398, duration=1)
        pyautogui.write(amount)

        pyautogui.click(404, 424, duration=1)
        pyautogui.write(price)

        pyautogui.click(312, 585, duration=1)
        sleep(1)
