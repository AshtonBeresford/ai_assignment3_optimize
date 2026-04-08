import numpy as np

import itertools

c = np.array([[1200, 2500, 1800, 2200, 3500, 900, 1600, 1400, 2000, 2800, 1100, 1900, 1000, 3200, 2100], [4.5, 6.2, 5.1, 4.8, 3.9, 6.8, 5.5, 4.7, 5.9, 4.2, 5, 5.4, 4.6, 6, 4.9]]) # Space Requested-first row, Bid-second row 
#example: print(c1[1][2]) prints 5.1
c_sum = np.array([c[0][0]*c[1][0], c[0][1]*c[1][1], c[0][2]*c[1][2], c[0][3]*c[1][3], c[0][4]*c[1][4], c[0][5]*c[1][5], c[0][6]*c[1][6], c[0][7]*c[1][7], c[0][8]*c[1][8], c[0][9]*c[1][9], c[0][10]*c[1][10], c[0][11]*c[1][11], c[0][12]*c[1][12], c[0][13]*c[1][13], c[0][14]*c[1][14],]) # Total Bid (Bid x space)
b_names = np.array(["Polar Brew Coffee", "Tech Haven", "Green Leaf Market", "Campus Books & Co.", "FitZone Gym", "Byte Repair", "Urban Threads", "Clyde's Photo, Ada", "GameSphere", "Serenity Spa", "QuickPrint Center", "EcoHome Goods", "Smoothie Spot", "VR Arena", "Study Lounge Café"])

# limits the itertools function to only using 1s and 0s
binary_nums = '01'

# Setting up variables to store the best values/paths
best_path = np.full(15, 0)
best_space = 0
best_profit = 0
max_space = 6000

# runs through every combination of 0 and 1 thats 15 characters long
for i in range (15, 16):
    for combo in itertools.product(binary_nums, repeat=i):
        attempt = ''.join(combo)
        #print(attempt) # uncomment this line if you want to see it print every possible combination, cool but uneeded for this project

        space = 0
        profit = 0
        path = np.full(15, 0)
        for j in range(15):
            path[j] = attempt[j]
            space += path[j]*c[0][j]
            profit += path[j]*c_sum[j]
        if (space <= max_space) and (best_profit < profit):
            best_path = path
            best_profit = profit
            best_space = space

print("\nbest path: ", best_path)
print("Space: ", best_space)
print("Profit: ", best_profit)