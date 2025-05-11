import numpy as np

np_height= np.array([5.5,4.5,3.5,7.8,4.7,9.8])

print(type(np_height))

np_weight=np.array([100,45,65,76,89,34])
bmi = np_weight/np_height**2
print(bmi)
arr1=np.array([1,2,3,4,5])
arr1.ndim


extra=[1,2,9,3,'Hello',False]
print(type(extra))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,100]

print(list1+list2)

np_list1=np.array([1,2,3,4,5])
np_list2=np.array([6,7,8,9,100])

print(np_list1+np_list2)

print(np_list2>6)

print(np_list2[np_list2>6])


arr_2d=np.array([[1,2],
                 [3,4],
                 [5,6]])
print(arr_2d)

print(arr_2d.ndim)

print(arr_2d[1,0])

print(arr_2d[1,1])