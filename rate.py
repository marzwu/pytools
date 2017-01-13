from random import random
import pandas as pd
import numpy as np


def get_level(rates):
    total = sum(rates)
    r = random() * total

    rise = 0
    for i in range(len(rates)):
        rise += rates[i]
        if r <= rise:
            return i

    return -1


if __name__ == '__main__':
    hist = pd.read_csv(r'E:\workspace\SAServer\mainVersion\bin\dat\cfg\ZCJB.csv').head(1)
    cfg = list(pd.read_csv(r'E:\workspace\SAServer\mainVersion\bin\dat\cfg\ConfigValue.csv').tail(1)['content'])[0]
    cfg = cfg.split(';')
    _cfg = []
    for x in cfg:
        k, v = x.split(',')
        _cfg.append(float(k))
        _cfg.append(float(v))

    rates = []
    for i in range(4):
        rates.append(list(hist['chance{}'.format(i + 1)])[0])

    levels = []
    rewards = []
    for i in range(10000):
        level = get_level(rates)
        levels.append(level)

        getmin = list(hist['getMin'])[0]
        getmax = list(hist['getMax'])[0]

        _min = _cfg[level * 2]
        _max = _cfg[level * 2 + 1]
        a = 1.0 / int(random() * 1000 + 1)
        reward = (_min + (_max - _min) * a) * getmin
        reward = int(max(getmin, min(getmax, reward)))
        rewards.append(reward)

    print(levels)
    print(rewards)

    reward_set = set(rewards)
    reward_unique = list(reward_set)
    print(reward_unique)

    reward_key = np.array(reward_unique)
    reward_key.sort()
    print(reward_key)
    print()

    nrewards = np.array(rewards)
    percents = []
    for x in reward_key:
        x__sum = (nrewards == x).sum()
        percent = round(x__sum / 10000 * 100, ndigits=2)
        percents.append(percent)
        print(x, x__sum, '{}%'.format(percent))

    sum = 0
    for i in range(5):
        sum += percents[i]
    print('抽到最低五个数的概率：{}%'.format(sum))

    n = np.array(levels)
    print('一档', (n == 0).sum(), '{}%'.format(round((n == 0).sum() / 10000 * 100, ndigits=2)))
    print('二档', (n == 1).sum(), '{}%'.format(round((n == 1).sum() / 10000 * 100, ndigits=2)))
    print('三档', (n == 2).sum(), '{}%'.format(round((n == 2).sum() / 10000 * 100, ndigits=2)))
    print('四档', (n == 3).sum(), '{}%'.format(round((n == 3).sum() / 10000 * 100, ndigits=2)))
