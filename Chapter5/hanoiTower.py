count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("({})->({})".format(src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("({})->({})".format(src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)

hanoi(3,"A","c","B")
print(count)