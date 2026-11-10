# array stacking
import numpy as np

e = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print(e)
print(g)
print(np.vstack((e, g)))
print(np.hstack((e, g)))

# splitting:
z = np.array([[1, 2, 3], [4, 5, 6]])
print(z)

for el in np.hsplit(z, 3):
    print(el)

for el in np.vsplit(z,2):
    print(el);
