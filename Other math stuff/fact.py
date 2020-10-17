import scipy.integrate as integ
import numpy as np
def fact(z):
    """
    Factorial function which includes the possibility of decimal numbers.
    """
    y = lambda x: x**(z) * np.exp(-x)
    return integ.quad(y, 0, np.inf)[0]

