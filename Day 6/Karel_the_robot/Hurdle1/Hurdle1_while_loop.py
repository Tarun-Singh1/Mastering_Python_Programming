def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


number_of_hurdles = 6

while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1

