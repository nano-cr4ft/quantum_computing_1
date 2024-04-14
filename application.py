import numpy as np

# the first problem we had
a = 0
b = 1
c = -1
d = 0
matrix = np.matrix(
    [a, b]
)
matrix_2 = np.matrix(
    [c, d]
)
# print(matrix)
# print(matrix_2)

input_1 = 0
# x
input_2 = 1
# y
combined = ([input_1, input_2])

x = (input_1 * a) + (input_2 * b)
y = (input_1 * c) + (input_2 * d)
print(np.array([[x, y]]))