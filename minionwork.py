#!/usr/bin/env python3
def solution(data,n):
    return [i for i in data if data.count(i)<=n]

print(solution([1, 2, 3],0))                      # None
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5],1))    # 1,4
