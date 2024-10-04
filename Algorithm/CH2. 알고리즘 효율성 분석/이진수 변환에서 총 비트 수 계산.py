#반복 알고리즘
def binary_digits(n):
    count = 1
    while n > 1:
        count +=1
        n = n // 2 
    return count

# count를 0부터 안하는 이유는
# 0으로 시작해 자릿수가 하나 적게 계산됨으로 이를 방지하기 위해 1부터 시작