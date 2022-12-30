userYear = int(input())

if userYear % 4 == 0 and userYear % 100 != 0 :
    print(1)
elif userYear % 400 == 0 :
    print(1)

else :
    print(0)