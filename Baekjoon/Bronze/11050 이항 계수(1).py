import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(N) // (factorial(N-K) * factorial(K)))