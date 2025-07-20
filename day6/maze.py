#!/usr/bin/env python3

def turn_right() -> None:
    turn_left()
    turn_left()
    turn_left()

def act() -> None:
    if right_is_clear():
            turn_right()
    if front_is_clear():
            move()
    elif wall_in_front():
        if right_is_clear():
            turn_right()
        elif wall_on_right():
            turn_left()


while not at_goal():
    act()

done()