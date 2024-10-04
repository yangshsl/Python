def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

A = [4, 2, 7, 1, 9]  # 리스트 A
key = 7               # 찾고자 하는 값 (key)
index = sequential_search(A, key)  # 함수 호출
print(index)  # 출력: 2 (7이 리스트 A의 인덱스 2에 있음)
