"""Core functions for the manima package"""

import os
import pathlib
import turtle

def carrega_imagens(categoria: str, tamanho: int) -> None:
    caminho = pathlib.Path(__file__)
    caminho_imagens = caminho.parent / 'images' / categoria / str(tamanho)
    # if caminho.exists() and caminho.is_dir():
    img_animais = caminho_imagens.glob('*.gif')
    pwd = os.getcwd()
    os.chdir(caminho_imagens.parent.parent)

    for img in img_animais:
        shape = f'{categoria}/{tamanho}/{img.name}'
        print(os.getcwd(), shape)
        turtle.addshape(f'{shape}')

    os.chdir(pwd)
    # else:
    #     raise FileNotFoundError(f'O caminho {caminho_imagens} não existe')