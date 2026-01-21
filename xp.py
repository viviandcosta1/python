import numpy as np
a = np.array(([1,2,3],[2,3,7],[1,3,4]))
b = np.array(([2,3,4],[1,2,4],[5,6,7]))  # Fixed: made it 3x3 to match a
c = np.array(([1,0,0],[0,1,0],[0,0,1]))

print("Array a (3x3):")
print(a)
print("\nArray b (3x3):")
print(b)
print("\nArray c (3x3):")
print(c)

print("\na + b + c:")
print(a + b + c)

print("\na * b + c:")
print(a * b + c)
