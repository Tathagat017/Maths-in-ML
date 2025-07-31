def add_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [a + b for a, b in zip(v1, v2)]

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return sum(a * b for a, b in zip(v1, v2))

def are_orthogonal(v1, v2):
    return dot_product(v1, v2) == 0

def multiply_matrices(m1, m2):
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    cols_m2 = len(m2[0])

    if cols_m1 != rows_m2:
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")

   
    result = [[0 for _ in range(cols_m2)] for _ in range(rows_m1)]

    
    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1): 
                result[i][j] += m1[i][k] * m2[k][j]

    return result
