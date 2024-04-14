import numpy as np

# gives angles
#radian initial = np.angle(1+1j, deg=True)

# converts to radians
#deg = np.array(initial)
#angle = np.radians(deg)

# experiment
#sin_thing = np.sin(angle)
#print(sin_thing)

# Final Product
x = 45
initial_array = np.array([[np.cos(x), 1],
                            [np.sin(x), 0]])


a = 1
b = 0

vector = np.array([[a, b]])

c = (np.cos(x) * a) + (np.sin(x) * b)
d = (np.cos(x) * a) + (np.sin(x) * b)

final_result = ([[c, d]])
print(final_result)

#result is pi/4