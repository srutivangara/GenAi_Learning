import numpy as np
array_1D = np.arange(1,10)
array_2D = np.arange(1,10).reshape(3,3)
List = [10,20,30,40,50]
arr_list = np.array(List)
print("-----Shape of each array-----")
print(array_1D.shape)
print(array_2D.shape)
print(arr_list.shape)
print("-----Data type of each array-----")
print(array_1D.dtype)
print(array_2D.dtype)
print(arr_list.dtype)