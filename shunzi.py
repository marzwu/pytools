import datetime


def is_shunzi(s):
    temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
    mark = [0 for i in range(len(temp))]

    len_zero = 0
    has_A = False
    for i in s:
        if i == 1:
            has_A = True

        if i == 0:
            len_zero += 1
        else:
            if mark[i - 1] != 0:
                return False
            mark[i - 1] += 1

    len_gap = get_gap_len(mark)

    if has_A and len_gap > len_zero:  # TJQK1的情况
        mark[0] = 0
        mark[-1] = 1

        len_gap = get_gap_len(mark)

    return len_gap <= len_zero


def get_gap_len(mark):
    new_mark = None
    for i in range(len(mark)):
        if mark[i] != 0:
            new_mark = mark[i:]
            break
    for i in range(len(new_mark) - 1, -1, -1):
        if new_mark[i] != 0:
            new_mark = new_mark[:i]
            break
    len_gap = 0
    for i in range(len(new_mark)):
        if new_mark[i] == 0:
            len_gap += 1

    return len_gap


if __name__ == '__main__':
    d = {'T': 10, 'J': 11, 'Q': 12, 'K': 13}

    lst = ['45678', '98765', '9TJQK', '00123', '12045', '12567', 'TJQK1', '1TJQK', '11002', '00123', '120QK']

    for s in lst:
        # while True:
        #     s = input('>')
        data = []
        for i in s:
            if i in d:
                data.append(d[i])
            else:
                data.append(int(i))
        print("{}\t{}".format(is_shunzi(data), s, data))

    # 一亿次
    now = datetime.datetime.now()
    i = 0
    while i < 1e8:
        i += 1
        is_shunzi([1, 2, 3, 4, 5])
    print(datetime.datetime.now() - now)
