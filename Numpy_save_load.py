import numpy as np

 # save a np array
arr = np.array([[1,2,3],[4,5,6]])
np.save("data1",arr)
print("Done!")

# Load the numpy array
arr = np.load("data1.npy")
print(arr)

# Save multipler np arrays
arr1= np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1.1,1.2,1.3,1.4])
arr3= [101,201,301,401]
np.savez("data2",arr1,arr2,arr3)
# np.savez_compressed("data2",arr1,arr2,arr3) # compressed version of above but slower comparatively and takes lesser memory also
print("Done!")

#Load the multiple np arrays
arrays = np.load("data2.npz")
print(arrays['arr_1'])