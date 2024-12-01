#!/usr/bin/env python3

import time
import turtle
from manima.core import carrega_imagens

def main():
    turtle.setup(800, 600)
    turtle.title('Manima: Animações que me animam')
    carrega_imagens('animal', 128)
    print(turtle.getshapes())
    gato = turtle.Turtle(
        shape='animal/128/_cat.gif',
        visible=True
        )

    formas_gato = ['animal/128/_cat.gif', 
                   'animal/128/cat_.gif']
    i = 0
    while True:
        gato.shape(formas_gato[i])
        i = (i + 1) % 2
        time.sleep(0.5)
        turtle.update()

    turtle.mainloop()

if __name__ == '__main__':
    main()