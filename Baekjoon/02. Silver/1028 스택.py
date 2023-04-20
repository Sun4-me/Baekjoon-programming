import sys
N = int(input())

stack = []

for i in range(N):
    massage = sys.stdin.readline().split()
    if massage[0] == "push":
        stack.append(massage[1])
    
    elif massage[0] == "top":
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[-1])

    elif massage[0] == "size":
        print(len(stack))
    
    elif massage[0] == "empty":
        if len(stack) == 0:
            print(1)
        else :
            print(0)

    elif massage[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())