from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
tt = Turtle()


def change(x, y):
    # cobra muda a direção
    aim.x = x
    aim.y = y


def inside(head):
    return -270 < head.x < 250 and -260 < head.y < 260  # espaço da morte


def move():
    # "Move a cobra
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print(f'Pontuação: {len(snake) - 1}')
        tt.undo()  # apaga o antigo placar
        tt.hideturtle()
        tt.penup()
        tt.setposition(250, 225)
        tt.write(f'Pontuação: {len(snake) - 1}', True, align='right', font=("Arial", 20, "bold"))  # Placar
        food.x = randrange(-25, 25) * 10  # espaço que a comida aparece
        food.y = randrange(-25, 25) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)  # velocidade


setup(520, 519, 450, 0)
tt.undo()
tt.hideturtle()
bgcolor("orange")
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()


