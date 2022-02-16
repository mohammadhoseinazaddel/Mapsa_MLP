def trnsfering_matrix(mat2):
    m, n = len(mat2), len(mat2[0])
    result = []
    for col in range(n):
        result.append([])
        for row in range(m):
            result[col].append(mat2[row][col])
    print(result)
    return result

if __name__ == '__main__':
    trnsfering_matrix([[3,2],[6,13]])