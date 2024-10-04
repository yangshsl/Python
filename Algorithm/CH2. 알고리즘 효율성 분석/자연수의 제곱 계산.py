def compute_square_A(n):
    return n*n

def compute_square_B(n):
    sum=0
    for i in range(n):
        sum=sum+n
    return sum

def compute_square_C(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum+1
    return sum
        