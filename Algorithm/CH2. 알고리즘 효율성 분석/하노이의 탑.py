def hanoi_tower(n, fr, tmp, to): #n: 이동할 원판의 개수, fr: 시작 막대, tmp: 임시 막대, to: 목표 막대
    if(n==1): 
        print("원판 1: %s ==> %s" %(fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" %(n,fr, to))
        hanoi_tower(n-1, tmp, fr, to)

hanoi_tower(5, 'A', 'B', 'C')

#n: 5 (이동할 원판 개수는 5개)
