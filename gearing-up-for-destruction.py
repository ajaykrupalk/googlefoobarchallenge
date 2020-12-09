from fractions import Fraction  
def answer(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):#checks for the length of the array
        return [-1,-1]
    even = True if (arrLength % 2 == 0) else False#checks if array has odd or even number of elements
    #according to the equations https://i.stack.imgur.com/fVBLd.jpg
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])  
    #since the first and last pegs have definite signs, we calculate the first and last peg
    if (arrLength > 2):
        for index in range(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]#calculating the sum of the other pegs 
       

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()#calculating r0
    #checking if the radius of the first gear is twice of that the last radius which is calculated by sum and stored in FirstGearRadius
    if FirstGearRadius < 2:
        return [-1,-1]
    currentRadius = FirstGearRadius
    for index in range(0, arrLength-2):
        #finding p[1]-p[0],p[2]-p[1]
        CenterDistance = pegs[index+1] - pegs[index]
        #finding r1=p[1]-p[0]-r0
        NextRadius = CenterDistance - currentRadius
        #checking if the ration of the radius is greater than 1
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius
    #returns the numerator and denominator value of the FirstGearRadius
    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

print(answer([4,30,50]))

'''Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. 
It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and 
the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. 
You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different 
sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates 
at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and 
turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) 
which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius 
in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all 
support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) 
should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, 
and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and 
solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases -- 
Input:
Solution.solution({4, 17, 50})
Output:
    -1,-1

Input:
Solution.solution({4, 30, 50})
Output:
    12,1

-- Python cases -- 
Input:
solution.solution([4, 30, 50])
Output:
    12,1

Input:
solution.solution([4, 17, 50])
Output:
    -1,-1

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
If your solution passes the test cases, it will be removed from your home folder.
'''
