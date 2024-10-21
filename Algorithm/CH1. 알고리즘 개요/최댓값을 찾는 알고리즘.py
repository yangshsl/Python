def find_max(A):
    max_num = A[0]
    for num in A[1: ]:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([1,2, 3, 4,5]))