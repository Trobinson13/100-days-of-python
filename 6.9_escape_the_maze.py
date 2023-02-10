# Code used in the Reeborgs World Maze challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# also used to upload Files\problem_world(1-3).json to reeborg and test against infinite loops

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() != True :
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()