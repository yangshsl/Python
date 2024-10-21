#유사코드
gcd(a,b)
    while b != 0 do
        r <- a mob b
        a <- b 
        b <- r
    return a