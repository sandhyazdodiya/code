"""
Input: ‘N’ = 3

Output: 
* * *
* * *
* * *

"""

def nForest(n:int) ->None:
    for i in range(0, n):
        for i in range(0, n):
            print("* ", end="")
        print()

"""
Example:
Input:  ‘N’ = 3

Output: 
* 
* *
* * *
"""

def nForest(n:int) ->None:
    for i in range(1, n+1):
        print("* " * i)


"""
Example:
Input: ‘N’ = 3

Output: 
1
1 2 
1 2 3

"""

def nTriangle(n:int) ->None:
    for i in range(0, n):
        for i in range(0, i+1):
            print(i+1 , end=" ")
        print()