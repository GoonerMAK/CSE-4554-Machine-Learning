# -*- coding: utf-8 -*-
"""200042115_ML_HW_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15AgPfnpH1bitGfnioMrIK5Bm9Fz6_XWN

Task 1: Generate two random 2x2 matrices A and B. Multiply them together and print the result.
"""

import numpy as np

a = np.random.randint(1, 10, size=(2, 2))
b = np.random.randint(1, 10, size=(2, 2))
print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

c = a.dot(b)

print("Matrix C:")
print(c)

"""Task 2: Create two 3x3 matrices C and D. Manually calculate the matrix multiplication CD and verify it is the same as C.dot(D)."""

rows_C = 3
cols_C = 3
rows_D = 3
cols_D = 4

C = np.random.randint(1, 10, size=(rows_C, cols_C))
D = np.random.randint(1, 10, size=(rows_D, cols_D))

print("Matrix C:")
print(C)

print("Matrix D:")
print(D)

result = np.zeros((rows_C, cols_D), dtype=int)

# iterate through rows of C
for i in range(len(C)):
   # iterate through columns of D
   for j in range(len(D[0])):
       # iterate through rows of D
       for k in range(len(D)):
           result[i][j] += C[i][k] * D[k][j]

print()
print("Manually calculated:")
for r in result:
   print(r)

print()

# Calculate matrix multiplication using numpy dot function
CD = np.dot(C, D)
print("Calculated via numpy dot:")
print(CD)

"""Task 3: Given a matrix A, calculate A(T)A where T denotes the transpose."""

rows_A = 3
cols_A = 2

A = np.random.randint(1, 10, size=(rows_A, cols_A))

print("Matrix A:")
print(A)

A_transpose = A.transpose()

print()
print("Transpose of Matrix A:")
print(A_transpose)

ATA = np.dot(A_transpose, A)

print()
print("Result of A(T)A:")
print(ATA)

"""Task 4: Multiply a 4x3 matrix B with a 3x2 matrix A. Confirm the dimensions of the resulting matrix."""

rows_A = 3
cols_A = 2
rows_B = 4
cols_B = 3

A = np.random.randint(1, 10, size=(rows_A, cols_A))
B = np.random.randint(1, 10, size=(rows_B, cols_B))

print("Matrix B:")
print(B)

print()
print("Matrix A:")
print(A)

BA = np.dot(B, A)

print()
print("Matrix BA:")
print(BA)

print()
print("Dimensions of the matrix BA:")
print(BA.shape)

"""Task 5: Given two matrices A and B, show that in general A · B ̸= B · A


"""

rows_A = np.random.randint(1, 4)
cols_A = np.random.randint(1, 4)
rows_B = np.random.randint(1, 4)
cols_B = np.random.randint(1, 4)

A = np.random.randint(1, 10, size=(rows_A, cols_A))
B = np.random.randint(1, 10, size=(rows_B, cols_B))

print("Matrix A:")
print(A)

print()
print("Matrix B:")
print(B)

if cols_A != rows_B:
    print("\nMatrix multiplication AB is not possible.")
elif cols_B != rows_A:
    print("\nMatrix multiplication BA is not possible.")
else:
    AB = np.dot(A, B)
    BA = np.dot(B, A)

    print("\nA·B:")
    print(AB)

    print("\nB·A:")
    print(BA)

    if np.array_equal(AB, BA):
        print("\nA·B is equal to B·A")
    else:
        print("\nA·B is not equal to B·A")

"""Task 6: Download the IRIS dataset as a CSV file and load the CSV file into a DataFrame. Examine the DataFrame using .head(), .tail(), .shape, .dtypes, etc."""

import pandas as pd
path = "/content/drive/MyDrive/Dataset/iris.csv"

df = pd.read_csv(path)
print(df.head(5))

print(df.tail(5))

print("\nShape of the DataFrame:")
print(df.shape)

print("\nData types of the columns:")
print(df.dtypes)

print("\nThe columns:")
print(df.columns)

"""Task 7: Select a specific column from the DataFrame. Create a Plot to visualize the data in that column."""

import matplotlib.pyplot as plt

sepal_length_column = df['sepal.length']

plt.figure(figsize=(20, 6))  # Setting the size of the plot

plt.plot(sepal_length_column, marker='o', linestyle='-', color='b')  # line plot
plt.title('Sepal Length Visualization')
plt.xlabel('Index')
plt.ylabel('Sepal Length')

plt.grid()  # Adding grid lines

plt.show()

sepal_width_column = df['sepal.width']     # Taking another column

plt.figure(figsize=(20, 6))  # Setting the size of the plot

plt.scatter(df.index, sepal_width_column, color='r', marker='x')  # scatter plot
plt.title('Sepal Width Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Sepal Width')

plt.grid()

plt.show()

sepal_petal_column = df["petal.length"]

plt.figure(figsize=(20, 6))

plt.hist(sepal_petal_column, bins=20, color='g', edgecolor='black')    # Histpgram plot
plt.title('Petal Length Histogram')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')

plt.grid()

plt.show()

import seaborn as sns

petal_width_column = df["petal.width"]

plt.figure(figsize=(20, 6))

sns.kdeplot(petal_width_column, fill=True, color='purple')
plt.title('Petal Width KDE Plot')
plt.xlabel('Petal Width')

plt.grid()

plt.show()

plt.figure(figsize=(10, 5))

categories = df['variety'].unique()
mean_sepal_length = df.groupby('variety')['sepal.length'].mean()

plt.bar(categories, mean_sepal_length, color='orange')
plt.title('Mean Sepal Length by Variety')
plt.xlabel('\nVariety')
plt.ylabel('Mean Sepal Length\n')

plt.grid()

plt.show()

"""Task 8: Filter the DataFrame to only show rows where a certain column value meets some criteria"""

filtered_df = df[(df['petal.width'] < 0.5) & (df['sepal.length'] > 5)]

print(filtered_df)

"""Task 9: Calculate summary statistics (mean, min, max, etc) for numerical columns in the DataFrame using .describe()."""

summary_stats = df.describe()

print(summary_stats)

"""Task 10: Group the DataFrame by one or more columns and calculate aggregates like count, mean, etc per group."""

grouped_data = df.groupby('variety')

agg_data = grouped_data.agg(['sum', 'mean', 'count'])

print(agg_data)
print()

grouped_by_multiple = df.groupby(['variety', 'sepal.width']).agg(['sum', 'mean', 'count'])
print(grouped_by_multiple)

"""Task 11: Sort the DataFrame values by a specific column in ascending or descending order."""

sepal_width_desc = df.sort_values(by='sepal.width',ascending=False)
print("Sepal Width Descending Order:")
print(sepal_width_desc)

sepal_width_asc = df.sort_values(by='sepal.width',ascending=True)
print("\nSepal Width Ascending Order:")
print(sepal_width_asc)

"""Task 12: Handle missing values in a DataFrame by dropping or filling."""

# Removing a value so that we can try to handle missing values in a Dataframe
missing_data = {
    'sepal.length': [5.7],
    'sepal.width': [4.4],
    'petal.length': [np.nan],  # Setting the value to NaN
    'petal.width': [0.4],
    'variety': ['Setosa']
}

missing_data_df = pd.DataFrame(missing_data)
print(missing_data_df)

rows_to_append = df.sample(n=10)
missing_data_df = pd.concat([missing_data_df, rows_to_append], ignore_index=True)
print(missing_data_df)

# # Dropping rows with missing values
# dropped_df = missing_data_df.dropna()
# print(dropped_df)

# Filling missing values with the mean of the column
mean_petal_length = missing_data_df['petal.length'].mean()
print("Mean: " + str(mean_petal_length))

filled_df = missing_data_df.fillna({'petal.length': mean_petal_length})
print(filled_df)