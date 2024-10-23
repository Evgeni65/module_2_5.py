def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)

result1 = get_matrix(2, 3, 20)
result2 = get_matrix(4, 5, 8)
result3 = get_matrix(5, 2, 6)