def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
    
A = [10, 25, 30, 45, 60]
key = 30