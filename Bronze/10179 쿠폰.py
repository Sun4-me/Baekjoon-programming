for i in range(int(input())):
    price = float(input())
    price = round(price * 4 / 5, 2)
    print("${:.2f}".format(price))