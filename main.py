from random import randint
from turtle import *
from freegames import vector

# Configuración de la pantalla
setup(width=800, height=600)
bgcolor("black")
title("Cosmic Rush")
tracer(False)

# Creación de la nave
ship = vector(-350, 0)
ship_shape = [
    (10, 0), (-5, 10), (-10, 0), (-5, -10)
]

# Variables
ship_speed = 20
asteroid_speed = 0.5
asteroid_spawn_interval = 50  # Menor valor = más asteroides
score = 0
game_over = False

# Lista para almacenar los asteroides
asteroids = []

# Funciones
def move_ship(x, y):
    ship.y = y

def create_asteroid():
    asteroid = vector(400, randint(-250, 250))
    asteroids.append(asteroid)

def move_asteroids():
    global asteroid_speed
    global asteroid_spawn_interval
    for asteroid in asteroids:
        asteroid.x -= asteroid_speed
    # Aumentar la velocidad de los asteroides con el tiempo
    asteroid_speed += 0.005

def draw_ship():
    up()
    goto(ship.x, ship.y)
    down()
    color("blue")  # Cambiamos el color de la nave
    begin_fill()
    for x, y in ship_shape:
        goto(ship.x + x, ship.y + y)
    end_fill()

def draw_asteroids():
    for asteroid in asteroids:
        up()
        goto(asteroid.x, asteroid.y)
        down()
        color("red")  # Cambiamos el color de los asteroides
        begin_fill()  # Rellenamos el círculo
        circle(15)
        end_fill()

def check_collision():
    global score, game_over

    for asteroid in asteroids:
        if abs(ship - asteroid) < 18.5:  # Ajustamos el valor de colisión
            game_over = True

def display_score():
    up()
    goto(-380, 260)
    color("white")
    write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

def game_over_message():
    up()
    goto(0, 0)
    color("white")
    write("Game Over", align="center", font=("Courier", 36, "normal"))

# Teclado
onkeypress(lambda: move_ship(0, ship.y + ship_speed), "Up")
onkeypress(lambda: move_ship(0, ship.y - ship_speed), "Down")
listen()

# Bucle principal del juego
while not game_over:
    # Crear asteroides aleatoriamente
    if randint(1, asteroid_spawn_interval) == 1:
        create_asteroid()

    # Mover asteroides
    move_asteroids()

    # Mover la pantalla
    if ship.y > 280 or ship.y < -280:
        game_over = True

    # Comprobar colisiones
    check_collision()

    # Dibujar elementos
    clear()
    draw_ship()
    draw_asteroids()
    display_score()
    update()

    # Aumentar puntuación
    score += 1
    if (score % 100) == 0:
        asteroid_spawn_interval -= 3
        asteroid_speed += 0.01

# Mostrar mensaje de fin de juego
game_over_message()

# Mantener la pantalla abierta
done()