'''
We want to make a row of bricks that is goal inches long.
 We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
 Return True if it is possible to make the goal by choosing from the given bricks. 
 This is a little harder than it looks and can be done without any loops
 '''

def make_bricks(small, big, goal):
    isGoalAchieved = False
    numberOfFiveInchesInGoal = int(goal / 5)
    numberOfOneInchInGoal = goal % 5

    if numberOfFiveInchesInGoal <= big:
        if numberOfOneInchInGoal <= small:
            isGoalAchieved = True
    else:
        numberOfOneInchRequired = goal - (big * 5)

        if numberOfOneInchRequired <= small:
            isGoalAchieved = True

    #print(numberOfFiveInchesInGoal)
    #print(numberOfOneInchInGoal)
    

    

    return isGoalAchieved

print(make_bricks(20, 4, 39))

