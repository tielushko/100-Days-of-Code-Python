def turn_right():
    turn_left()
    turn_left()
    turn_left()

#fix for the bug where the robot can stuck in an infinite right loop
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear() and not wall_in_front():
        move()
    else:   
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
