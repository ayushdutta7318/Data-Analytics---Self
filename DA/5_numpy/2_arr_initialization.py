# Array Initialization:
import numpy as np

zeros = np.zeros((2, 3))
# parentheses contains rows and columns
print(zeros)

ones = np.ones((2, 3))
print(ones)

full_arr = np.full((2, 3), 7)
print(full_arr)

# identity matrix:
id_arr = np.eye(3)
print(id_arr)

# random value
print(np.empty(2))

# evenly spaced array
even_arr = np.arange(1, 10, 2)
print(even_arr)

# specific number of equally spaced values:
print(np.linspace(1, 10, 5))

# random arr:
print(np.random.rand(2, 3))
print(np.random.randint(1, 100, (2, 3)))

# indexing and slicing in array:
a = np.array([1, 5, 3, 4, 7, 19])
print(a[0])
print(a[len(a) - 1])
print(a[0:4:2])
# array[start:stop:step]

# 2d Indexing and slicing:
b = np.array([[1, 3, 7], [7, 9, 15], [75, 84, 19]])
print(b)
print(b[0][1])
print(b[0][0:2])

print(b[1])  # 1d arr
print(b[1:])  # 2d arr

# arr reshaping:
d = np.array([1,2,3,4,5]);
print(d);
d = d.reshape(5,1);
print(d);
print(d.flatten());


