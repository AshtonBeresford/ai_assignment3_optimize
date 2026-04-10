#I'll use pymoo for the Genetic Algorithm

import numpy as np

from pymoo.algorithms.soo.nonconvex.ga import GA

from pymoo.core.problem import ElementwiseProblem
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.repair.rounding import RoundingRepair
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.optimize import minimize

from timeit import default_timer as timer

start = timer()

c_space = np.array([1200, 2500, 1800, 2200, 3500, 900, 1600, 1400, 2000, 2800, 1100, 1900, 1000, 3200, 2100]) # space requested
c_bid = ([4.5, 6.2, 5.1, 4.8, 3.9, 6.8, 5.5, 4.7, 5.9, 4.2, 5, 5.4, 4.6, 6, 4.9]) # Bid
c_total_bid = np.array([5400, 15500, 9180, 10560, 13650, 6120, 8800, 6580, 11800, 11760, 5500, 10260, 4600, 19200, 10290,]) # Total Bid (Bid x space)
b_names = np.array(["Polar Brew Coffee", "Tech Haven", "Green Leaf Market", "Campus Books & Co.", "FitZone Gym", "Byte Repair", "Urban Threads", "Clyde's Photo, Ada", "GameSphere", "Serenity Spa", "QuickPrint Center", "EcoHome Goods", "Smoothie Spot", "VR Arena", "Study Lounge Café"])

#start = timer()

class MyProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var=15, n_obj=1, n_ieq_constr=1, xl=0, xu=1, vtype=int)

    def _evaluate(self, x, out, *args, **kwargs):
        
        total_bid = 0#x*c_total_bid
        max_space = 6000
        space_used = 0#x*c_space
        # will loop through and bind total bid to the negative version of the amount of money ONU makes
        #   and binds space_used to the positive version of all the numbers added together
        for i in range(15):
            total_bid -= x[i] * c_total_bid[i]
            space_used += x[i] * c_space[i]
        #x = x*c_total_bid

        out["F"] = np.sum(total_bid).reshape(-1,1) #-np.sum(x).reshape(-1, 1)#total_bid
        out["G"] = np.sum(space_used) - max_space#space_used - max_space


problem = MyProblem()

method = GA(pop_size=20,
            sampling=IntegerRandomSampling(),
            crossover=SBX(prob=1.0, eta=3.0, vtype=int, repair=RoundingRepair()),
            mutation=PM(prob=1.0, eta=3.0, vtype=int, repair=RoundingRepair()),
            eliminate_duplicates=True,
            )

res = minimize(problem,
               method,
               termination=('n_gen', 40),
               seed=1,
               save_history=True
               )

print("Best solution found: %s" % res.X)
print("Function value: %s" % res.F)
print("Constraint violation: %s" % res.CV)


# Below just prints out information in a more readable manner
total_space = 0
total_profit = 0

for i in range(15):
    if res.X[i] == 1:
        print(b_names[i], " - Space Requested: ", c_space[i], ", Bid: ", c_bid[i], ", Total Bid: ", c_total_bid[i])
        total_space += c_space[i]
        total_profit += c_total_bid[i]

print("\nTotal space used = ", total_space, " ft^3. Which leaves ", 6000 - total_space, "ft^3 unused.")
print("Total profit for ONU = $", total_profit, ".")

end = timer()
print("Time to run: ", end - start)