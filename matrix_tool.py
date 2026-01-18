import numpy as np

def get_matrix(name):
    """
    Takes matrix input from user with proper validation
    and returns it as a NumPy array.
    """

    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"Enter values for Matrix {name} row-wise (space separated):")

    matrix = []

    for i in range(rows):
        while True:
            row = list(map(float, input(f"Row {i+1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"❌ Error: Please enter exactly {cols} values.")

    return np.array(matrix)


# Taking matrix input
A = get_matrix("A")
B = get_matrix("B")

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

