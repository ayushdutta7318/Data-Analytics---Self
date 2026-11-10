# Creating arrays:
import numpy as np;
print(np.__version__);

# arrays:
li = [1,2,3];
print(li);

arr_1 = np.array(li);
print(arr_1, type(arr_1));

# numpy array is efficient than list, also it stores only 1 datatype.

# 2d array:
li_1 = [1,2,3];
li_2 = [4,5,6];
arr_list_1_2 = np.array([li_1, li_2]);
print(arr_list_1_2);

# 3d arr:
li_1 = [1,2,3];
li_2 = [4,5,6];
li_3 = [7,8,9];
arr_list_3d = np.array([[li_1, li_2, li_3]]);
print(arr_list_3d, arr_list_3d.ndim);

# numpy arr attribute and properties:
print(f"Shape: {arr_list_3d.shape}");
print(f"size: {arr_list_3d.size}");
print(f"dtype: {arr_list_3d.dtype}");
# print(f"n_dim": {arr_list_3d.ndim});