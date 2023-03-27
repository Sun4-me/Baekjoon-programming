dad = 0
child = 0

for _ in range(int(input())):
    candy_nums , child_nums = map(int,input().split())
    child = candy_nums // child_nums
    dad  = candy_nums % child_nums
    print(f"You get {child} piece(s) and your dad gets {dad} piece(s).")