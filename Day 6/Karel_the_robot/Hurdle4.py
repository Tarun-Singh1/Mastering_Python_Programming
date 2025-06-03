def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def tackle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        tackle()




