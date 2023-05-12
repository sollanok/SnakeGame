"""Snake, classic arcade game.

Exercises

1. La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
2. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes
   entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.

"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# variables de colores:
colors = ['black', 'blue', 'green', 'yellow', 'purple']
food_color_index = 0
snake_color_index = 0
food_color = 'black'
snake_color = 'black'
executed = False

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

# Cada vez que se corra el juego, 
# la víbora y la comida deberán tener colores diferentes entre sí, 
# pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
def random_color(colors):  
    global executed, food_color, snake_color
    if not executed:
        food_color_index = randrange(0,5)
        while True:
            snake_color_index = randrange(0,5)  
            if snake_color_index != food_color_index:
                break
        food_color = colors[food_color_index]
        snake_color = colors[snake_color_index]
        executed = True
    
    return food_color, snake_color


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)


    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Actualizar la posición de la comida aleatoriamente
    if randrange(10) == 0:
        food.x += 10
    elif randrange (10) == 1:
        food.y += 10

    for body in snake:
        square(body.x, body.y, 9, random_color(colors)[0]) # llama funcion de color a la serpiente

    square(food.x, food.y, 9, random_color(colors)[1]) # llama funcion de color a la comida
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
