# Recusrive method to create the series
def computePascal(col, row):
    # There are three things to compute
    # 1. Left edge: col is 0
    # 2. Right edge: col is same as row
    if col == row or col == 0:
        return 1
    # 3. any other cell: col-1 + col of the previous row
    else:
        return computePascal(col - 1, row - 1) + computePascal(col, row - 1)


# Method to create the triangle for `N` row
def pascal_triangle(n):
    for r in range(n):
        # upon observation, we can deduce the relation
        # num_cols = num_rows + 1
        for c in range(r + 1):
            print(str(computePascal(c, r)), end=" ")
        print("\n")
