while True:
    num = int(input())
    if num == 0 :
        break
    elif str(num) == str(num)[::-1]:
        print("yes")
    else :
        print("no")

