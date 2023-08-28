# -*- coding: utf-8 -*-
"""200042115_ML_Lab_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GFhkDXFdU5yFNwZt_X8cTiFUSoabFYQb

Task 1: Create a one dimensional random numpy array of size 10.
"""

import numpy as np

array = np.arange(10)

print (array)

"""Task 2: Create a two dimensional numpy array of size 7x6 and reshape it to 3x14 array."""

my_array = np.zeros([7, 6])
print(my_array)
reshaped_array = my_array.reshape(3, 14)
print(reshaped_array)

"""**Task 3:** Create an array and extract all the odd numbers from it. [array([0,1,2,3,4,5,6,7,8,9])]."""

array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_indices = np.where(array % 2 == 1)
odd_values = array[odd_indices]
print(odd_values)

"""Task 4: Replace all the odd numbers in the previous array with -1."""

array = np.array([0, 1, 1, 3, 3, 5, 2, 7, 4, 9])
array[array % 2 == 1] = -1
print(array)

"""Task 5: Replace all the odd numbers in the previous array with -1 without affecting the original array."""

array = np.array([0, 1, 2, 3, 5, 5, 6, 7, 8, 9])
copy_array = np.copy(array)
copy_array[copy_array % 2 == 1] = -1
print(copy_array)

"""Task 6:
Get the positions where elements of a and b match
1.   a = np.array([1,2,3,2,3,4,3,4,5,6])
2.   b = np.array([7,2,10,2,7,4,9,4,9,8])




"""

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
matches = np.where(a == b)                      # compare = a[a==b]
print(matches)

"""Task 7: Get all the items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
"""

a = np.array([2, 6, 1, 9, 10, 3, 27])
matches = np.where((a >= 5) & (a <= 10))
matched_values = a[matches]
print(matched_values)

"""Task 8: Create a vector of size 10 with zeros. Then create a vector of size 10 with ones. Change their dimension and after that merge the the two vector vertically and horizontally using “concatenate”."""

zeroes = np.zeros(10)
ones = np.ones(10)

vertical_stacked = np.concatenate((zeroes, ones),axis=0).reshape((2,10))
horizontal_stacked = np.concatenate((zeroes, ones),axis=0).reshape((1, 20))

print(vertical_stacked)
print(horizontal_stacked)

zeros_reshaped = zeroes.reshape((10, 1))
ones_reshaped = ones.reshape((10, 1))

vertical_concatenated = np.concatenate((zeros_reshaped, ones_reshaped), axis=0)
horizontal_concatenated = np.concatenate((zeros_reshaped, ones_reshaped), axis=1)

print(vertical_concatenated)
print(horizontal_concatenated)

"""Task 9: Create an ndarray x of shape= (5, 4) with random numbers. Each of the 5 rows represents a sample with 4 features.

"""

x = np.random.randint(0, 100, size=(5, 4))

print(x)

"""Task 10: Create a flat ndarray y of shape=(5, ), whose elements are 0 and 1. Each element is the class label of the corresponding sample in x

"""

n_samples = 5
n_features = 4

x = np.random.randint(0, 100, size = (n_samples, n_features) )
y = np.random.randint(0, 2, n_samples)

print('x =', x)
print('y =', y)

"""Task 11: Define a function extract_subset(x, y, y0) that takes as input: the feature matrix x, and the labels y from the previous exercise. A target class y0 (i.e., either y0=0 or y0=1) and returns a feature matrix containing only samples belonging to y0."""

def extract_subset(x, y, y0):
  indices = np.where(y == y0)[0]
  new_set = x[indices]
  return new_set

y0 = 0
new_set_0 = extract_subset(x, y, y0)
print(new_set_0)

y0 = 1
new_set_1 = extract_subset(x, y, y0)
print(new_set_1)

"""Task 12: Import a dataset (IRIS dataset) by keeping the text and numbers intact."""

from sklearn.datasets import load_iris

iris = load_iris()

print(iris)

"""Task 13: Find the mean, median and standard deviation of the 1st column of the given dataset. Give statistical summary of the dataset as many as possible."""

from sklearn.datasets import load_iris

iris = load_iris()

first_column = iris.data[:, 0]

first_column_mean = np.mean(first_column)
first_column_median = np.median(first_column)
first_column_standard_deviation = np.std(first_column)

print("The Mean: " + str(first_column_mean))
print("The Median: " + str(first_column_median))
print("The Standard Deviation: " + str(first_column_standard_deviation))