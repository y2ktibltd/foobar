#!/usr/bin/env python3
def solution(n):
    n = int(n)
    m = 0
    while n > 1:
        if (n&1) == 0:
            n >>= 1
        elif (n&3) == 1 or n == 3:
            n -= 1
        else:
            n += 1
        m += 1
    return m

print(solution('15'),"\n") # 5
print(solution('4'),"\n") # 2
print(solution(str(pow(12,345))),"\n")
