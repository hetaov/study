# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 5*x**2 +9

x = np.linspace(-5, 5, num=100)

y = f(x)

print y

plt.plot(x, y)
plt.show()
