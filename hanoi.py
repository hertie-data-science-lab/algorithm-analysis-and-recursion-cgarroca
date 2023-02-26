# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:37:20 2023
@authors: Jorge Roa (226454 Git: jurjoroa) & Carmen Garro (226594 Git: cgarroca)
"""

import sys

# n: number of disks, cannot be less than 1
# from_rod, to_rod, aux_rod: A,B,C (three towers)
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n <= 0:
        sys.exit("Number of disks shouldn't be less than one!")
    elif n == 1:
        # only one movement needed if there's only one disk
        print("Move disk 1 from rod ", from_rod, " to rod ", to_rod)
        return #send the function's result back to the user
    #problem of more than 1 disk is solved in two steps
    #this is a recursive function that breaks the amount
    #of steps until the n == 1 which will go to the
    #first step
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk ", n," from rod ", from_rod, " to rod ", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

TowerOfHanoi(3, 'A', 'C', 'B')
