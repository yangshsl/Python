def gcd(a, b):
    # 두 수의 약수를 저장할 빈 리스트값을 만든다.
    first_list = []
    second_list = []

    # a의 약수 찾기
    for i in range(1, a + 1):
        if a % i == 0:  # 약수인지 확인
            first_list.append(i)  # 약수 추가

    # b의 약수 찾기
    for i in range(1, b + 1):
        if b % i == 0:  # 약수인지 확인
            second_list.append(i)  # 약수 추가

    # 두 리스트의 교집합 찾기
    common_divisors = set(first_list) & set(second_list)

    return max(common_divisors) if common_divisors else None

# 결과 출력
result = gcd(60, 20)
print(result)  # 출력: 20
