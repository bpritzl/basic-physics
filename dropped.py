
# Import packages
import math

# Request inputs
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Calculate the polar coordinates
r = math.sqrt(x**2 + y**2)
theta_rad = math.atan(y/x)

# Convert the angle into degrees
theta_deg = theta_rad*180/math.pi

# Print result
print("The r-coordinate is",r)
print("The theta-coordinate is",theta_deg)
