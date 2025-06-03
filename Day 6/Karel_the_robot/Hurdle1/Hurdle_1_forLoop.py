def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


for n in range(0, 6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()