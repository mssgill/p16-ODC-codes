# MSSG
# 7-18-2018
# This is to show where the derivative of the BB law crosses the zero
# point, which translates back to the max value of lambda(T)
# -- See https://en.wikipedia.org/wiki/Wien%27s_displacement_law#Derivation_from_Planck%27s_law

import matplotlib.pyplot as plt
import numpy as np


def y(x):  # This is the deriv of the BB law, x here is hc/(lambda k T)
    return (x-5) * np.exp(x) + 5 

x=np.arange(4.5, 5.5, 0.01)
plt.plot(x, y(x),'o') # The o here makes the plot as points vs. continuous line
plt.axhline(y=0, color='r', linestyle='-')
plt.show()

