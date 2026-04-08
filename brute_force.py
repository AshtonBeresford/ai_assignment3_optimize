import numpy as np

c = np.array([[1200, 2500, 1800, 2200, 3500, 900, 1600, 1400, 2000, 2800, 1100, 1900, 1000, 3200, 2100], [4.5, 6.2, 5.1, 4.8, 3.9, 6.8, 5.5, 4.7, 5.9, 4.2, 5, 5.4, 4.6, 6, 4.9]]) # Space Requested-first row, Bid-second row 
#example: print(c1[1][2]) prints 5.1
c_sum = np.array([c[0][0]*c[1][0], c[0][1]*c[1][1], c[0][2]*c[1][2], c[0][3]*c[1][3], c[0][4]*c[1][4], c[0][5]*c[1][5], c[0][6]*c[1][6], c[0][7]*c[1][7], c[0][8]*c[1][8], c[0][9]*c[1][9], c[0][10]*c[1][10], c[0][11]*c[1][11], c[0][12]*c[1][12], c[0][13]*c[1][13], c[0][14]*c[1][14],]) # Total Bid (Bid x space)
b_names = np.array(["Polar Brew Coffee", "Tech Haven", "Green Leaf Market", "Campus Books & Co.", "FitZone Gym", "Byte Repair", "Urban Threads", "Clyde's Photo, Ada", "GameSphere", "Serenity Spa", "QuickPrint Center", "EcoHome Goods", "Smoothie Spot", "VR Arena", "Study Lounge Café"])

# will recursively call itself until its found the optimal path
# @param path = np.array of boolean values to show which places have been selected 
# @param untested = shows which paths have not been tested yet
# @param space = how much space has been taken
def least_path(path, untested, space):

    for i in untested:
        print("here for now")
    print("here for now")


# Basically my main function
path_to_test = np.full(15,0)
path_untested = np.full(15, 1)

print(least_path(path_to_test, path_untested))
