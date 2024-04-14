import numpy as np
#applying transformations in arrays
learned = np.array([
    ['sin(theta)', '1'],
    ['cos(theta)', '0']
])


transformed = np.array([
    ['-sin(theta)', '0'],
    ['cos(theta)','1']
    ])
print (transformed)