import numpy as np
import sympy

x = np.linspace(-np.pi, np.pi)

lnx = np.e**(1j*x)

rhs = sympy.cos(x) + 1j*sympy.sin(x)

print lnx
print rhs

print sum(lhs==rhs)==len(x)
