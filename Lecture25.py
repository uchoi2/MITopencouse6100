# Plotting
import matplotlib.pyplot as plt

nVals = []
linear = []
quadratic = []
cubic = []
exponential = []

for n in range(0,30):
    nVals.append(n)
    linear.append(n)
    quadratic.append(n**2)
    cubic.append(n**3)
    exponential.append(1.5**n)

# plt.plot(<xvar> # typically n, <yvar>)
plt.plot(nVals, linear)