import numpy as np

def read_matrix(name):
    print(f"\nEnter {name} matrix:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    data = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1} ({cols} values): ").split()))
        if len(row) != cols:
            raise ValueError(f"Enter exactly {cols} values.")
        data.append(row)
    return np.array(data)

def menu():
    print("""
========== MATRIX OPERATIONS TOOL ==========
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Exit
============================================
""")

while True:
    menu()
    choice = input("Choose an option: ").strip()
    try:
        if choice == "1":
            A, B = read_matrix("first"), read_matrix("second")
            print("\nResult:\n", A+B if A.shape == B.shape else "Error: dimensions must match.")

        elif choice == "2":
            A, B = read_matrix("first"), read_matrix("second")
            print("\nResult:\n", A-B if A.shape == B.shape else "Error: dimensions must match.")

        elif choice == "3":
            A, B = read_matrix("first"), read_matrix("second")
            print("\nResult:\n", A@B if A.shape[1] == B.shape[0] else "Error: columns of A must equal rows of B.")

        elif choice == "4":
            A = read_matrix("matrix")
            print("\nTranspose:\n", A.T)

        elif choice == "5":
            A = read_matrix("matrix")
            if A.shape[0] != A.shape[1]:
                print("Error: determinant requires a square matrix.")
            else:
                print("\nDeterminant:", round(np.linalg.det(A), 6))

        elif choice == "6":
            print("Thank you for using Matrix Operations Tool!")
            break
        else:
            print("Invalid choice.")
    except ValueError as e:
        print("Input error:", e)
