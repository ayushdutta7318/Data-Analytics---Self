# Math operations on Array:
import numpy as np;
a = np.array([10,20,30,40,50]);
print(a+20);
print(a-20);
print(a*20);
print(a/20);

# square array element
print(np.square(a));
print(np.sqrt(a));

b = np.array([4,5,6]);
d = np.array([7,8,9]);
print(np.add(b,d));
print(np.subtract(b,d));
print(np.multiply(b,d));
print(np.divide(b,d));

z = np.array([[1,2,3], [4,5,6]]);
z = z.T;
print(z); #Transpose

# statistical fn
print(np.sum(z));
print(np.mean(z));
print(np.median(z));
print(np.std(z));

w = np.array([4,5,6]);
q = np.array([7,8,9]);
print(w == q);
print(np.not_equal(w,q));
print(np.array_equal(w,q));

# Broadcasting: math operartion on high and low dimensional array:
p = np.array([[78,24,96], [78,16,485]]);
t = np.array([10]);
print(p+t);

p = np.array([[78,24,96], [78,16,485]]);
t = np.array([10,55,80]);
print(p+t);

# Handling with nan and inf
data1 = np.array([1,2,3, np.nan, 5, np.inf]);
print(data1);