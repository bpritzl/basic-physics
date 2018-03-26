
# Import packages
import math

# Define variables
G = 6.67*10**(-11)
M = 5.97*10**24
R = 6371*10**3

# Describe the program
print("The program calculates the altitude of a satellite based on the period.")

# Request inputs
T = float(input("Enter the period of the satellite in seconds: "))

# Calculate the time to reach the ground
h = (G * M * T**2/(4*math.pi**2))**(1/3) - R

# Print result
print("The altitude is",h,"meters.")
