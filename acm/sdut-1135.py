n = int(input())
for i in range(n * 2 - 1):
    mid = int((n * 2 - 1) / 2)
    if i < mid:
        s = ' ' * int(mid - i) + '+'
        s += '*' * i + '+'
    else:
        s = ' ' * int(i - mid) + '+'

    print(s)
