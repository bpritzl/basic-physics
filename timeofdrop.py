# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Define variables
g = 9.81

# Describe the program
print("This program calculates the time for an object to fall to the ground.")
print("Initial velocity is zero and air resistance is neglected.")

# Request inputs
h = float(input("Enter the height of the tower in meters: "))

# Calculate the time to reach the ground
t = (2*h/g)**0.5

# Print result
print("The time to reach the ground is",t,"seconds.")
