# mixed integer programing method
from scipy.optimize import LinearConstraint
from scipy.optimize import milp
import numpy as np

# Define Objective 
c = np.array([[1200, 2500, 1800, 2200, 3500, 900, 1600, 1400, 2000, 2800, 1100, 1900, 1000, 3200, 2100], [4.5, 6.2, 5.1, 4.8, 3.9, 6.8, 5.5, 4.7, 5.9, 4.2, 5, 5.4, 4.6, 6, 4.9]]) # Space Requested-first row, Bid-second row 
#example: print(c1[1][2]) prints 5.1
c_sum = np.array([c[0][0]*c[1][0], c[0][1]*c[1][1], c[0][2]*c[1][2], c[0][3]*c[1][3], c[0][4]*c[1][4], c[0][5]*c[1][5], c[0][6]*c[1][6], c[0][7]*c[1][7], c[0][8]*c[1][8], c[0][9]*c[1][9], c[0][10]*c[1][10], c[0][11]*c[1][11], c[0][12]*c[1][12], c[0][13]*c[1][13], c[0][14]*c[1][14],]) # Total Bid (Bid x space)
# Since milp is a minimization optimization algorithm, we will make c_sum negative so that the algorithm can work with our numbers correctly 
c_sum = c_sum*-1

# Define Constraints 
A = np.array([c[0][0], c[0][1], c[0][2], c[0][3], c[0][4], c[0][5], c[0][6], c[0][7], c[0][8], c[0][9], c[0][10], c[0][11], c[0][12], c[0][13], c[0][14]]) # Space Request for each place (will eventually be multiplied by the bool array)

b_l = np.array([0]) # lower limit of 0 ft of soace used
b_u = np.array([6000]) # max limit of space that can be used 6000 ft

constraints = LinearConstraint(A, b_l, b_u)

# Tells the solver to use integers
integrality = np.full(15,1) # makes all the 15 x values that wil be multiplied by the c values boolean (2)
bounds = np.array([np.full(15, 0), np.full(15, 1)]) 
#print(bounds)

res = milp(c=c_sum, constraints=constraints, integrality=integrality, bounds=bounds)
print(res)
print("\n", res.x)

c_sum = -1*c_sum # Changing the sign again so its positive and easier to look at down below 
# List of Business's in order
names = np.array(["Polar Brew Coffee", "Tech Haven", "Green Leaf Market", "Campus Books & Co.", "FitZone Gym", "Byte Repair", "Urban Threads", "Clyde's Photo, Ada", "GameSphere", "Serenity Spa", "QuickPrint Center", "EcoHome Goods", "Smoothie Spot", "VR Arena", "Study Lounge Café"])

# function to help print stuff out
def print_results():
    total_space = 0
    total_profit = 0
    for x in range(15):
        if res.x[x] == 1:
            print(names[x], " - Space Requested: ", c[0][x], ", Bid: ", c[1][x], ", Total Bid: ", c_sum[x])
            total_space += c[0][x]
            total_profit += c_sum[x]
    
    print("\nTotal space used = ", total_space, " ft^3. Which leaves ", 6000 - total_space, "ft^3 unused.")
    print("Total profit for ONU = $", total_profit, ".")
print_results()