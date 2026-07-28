# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, columns, name):
    matrix = []

    print(f"\nEnter values for Matrix {name}:")

    for row_index in range(rows):
        while True:
            values = input(f"Enter row {row_index + 1}: ").split()

            if len(values) != columns:
                print(f"Error: Enter exactly {columns} values.")
                continue

            row = []

            try:
                for value in values:
                    row.append(float(value))
            except ValueError:
                print("Error: Enter numbers only.")
                continue

            matrix.append(row)
            break

    return matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transpose = []

    for column_index in range(columns):
        new_row = []

        for row_index in range(rows):
            new_row.append(matrix[row_index][column_index])

        transpose.append(new_row)

    return transpose


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    result = []

    for row_index in range(rows):
        new_row = []

        for column_index in range(columns):
            value = matrix_a[row_index][column_index] + matrix_b[row_index][column_index]
            new_row.append(value)

        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])
    result = []

    for row_index in range(rows_a):
        new_row = []

        for column_index in range(columns_b):
            total = 0

            for index in range(columns_a):
                total += matrix_a[row_index][index] * matrix_b[index][column_index]

            new_row.append(total)

        result.append(new_row)

    return result


def display_matrix(matrix):
    formatted_matrix = []

    for row in matrix:
        formatted_row = []

        for value in row:
            formatted_row.append(f"{value:g}")

        formatted_matrix.append(formatted_row)

    column_widths = []

    for column_index in range(len(formatted_matrix[0])):
        width = 0

        for row_index in range(len(formatted_matrix)):
            value_length = len(formatted_matrix[row_index][column_index])

            if value_length > width:
                width = value_length

        column_widths.append(width)

    for row in formatted_matrix:
        for column_index in range(len(row)):
            print(f"{row[column_index]:>{column_widths[column_index]}}", end="  ")

        print()


def main():
    while True:
        print("\n============================")
        print("     MATRIX OPERATIONS")
        print("============================")
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Quit")

        choice = input("Select an operation (1-4): ")

        if choice == "1":
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            if rows <= 0 or columns <= 0:
                print("Error: Matrix dimensions must be positive.")
                continue

            matrix = read_matrix(rows, columns, "A")
            result = transpose_matrix(matrix)

            print("\nOriginal Matrix:")
            display_matrix(matrix)

            print("\nTransposed Matrix:")
            display_matrix(result)

        elif choice == "2":
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            if rows <= 0 or columns <= 0:
                print("Error: Matrix dimensions must be positive.")
                continue

            matrix_a = read_matrix(rows, columns, "A")
            matrix_b = read_matrix(rows, columns, "B")
            result = add_matrices(matrix_a, matrix_b)

            print("\nMatrix A:")
            display_matrix(matrix_a)

            print("\nMatrix B:")
            display_matrix(matrix_b)

            print("\nSum:")
            display_matrix(result)

        elif choice == "3":
            rows_a = int(input("Enter number of rows for Matrix A: "))
            columns_a = int(input("Enter number of columns for Matrix A: "))
            rows_b = int(input("Enter number of rows for Matrix B: "))
            columns_b = int(input("Enter number of columns for Matrix B: "))

            if rows_a <= 0 or columns_a <= 0 or rows_b <= 0 or columns_b <= 0:
                print("Error: Matrix dimensions must be positive.")
                continue

            if columns_a != rows_b:
                print("Error: Columns in Matrix A must equal rows in Matrix B.")
                continue

            matrix_a = read_matrix(rows_a, columns_a, "A")
            matrix_b = read_matrix(rows_b, columns_b, "B")
            result = multiply_matrices(matrix_a, matrix_b)

            print("\nMatrix A:")
            display_matrix(matrix_a)

            print("\nMatrix B:")
            display_matrix(matrix_b)

            print("\nProduct:")
            display_matrix(result)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice.")


main()
