from itertools import permutations
def solution(L):
  p1=[s for i in range(2,len(L)+1) for s in permutations(L,i)]#find permutations of length 2 upto the length of list
  p2=[t for t in p1 if sum(t)%3==0]#find if the sum of the digits are divisible by 3(which means the number is divisible by 3)
  p3=[int(''.join(map(str,n))) for n in p2]#since t is a tuple and has to be converted to integer, we first convert it into a string and then convert it into an integer
  try:
    return max(p3)#finding the maximum element which is divisible by 3
  except ValueError:
    return 0#if there is no number which is divisible by 3 it returns 0

print(solution([3,1,4,1,5,9]))#prints output 94311
print(solution([3,1,4,1]))#prints output 4311

'''Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, 
to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 
for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a 
number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, 
but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large 
numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number 
that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, 
return 0 as the solution. L will contain anywhere from 1 to 9 digits. The same digit may appear multiple times in the list, 
but each element in the list may only be used once.

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
Solution.solution({3, 1, 4, 1})
Output:
    4311

Input:
Solution.solution({3, 1, 4, 1, 5, 9})
Output:
    94311

-- Python cases -- 
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311'''
