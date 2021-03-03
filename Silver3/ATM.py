# BOJ 11399 ATM
# 그리디 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
p = sorted(list(map(int, input().split())))
for i in range(1, n):
    p[i] += p[i-1]
print(sum(p))
