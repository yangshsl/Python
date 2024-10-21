def gcd(a, b):
    empty_list = []
    
    for i in range(1, a+1):
        if a % i == 0:
            empty_list.append(i)
    
    true_value = []

    while empty_list:
        value = empty_list.pop()
        if b % value == 0:
            true_value.append(value)

    return max(true_value) 

result = gcd(60, 28)
print(result)  # 출력: 4