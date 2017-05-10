# encode=utf-8
import os


def rename(rootpath):
    for item in os.listdir(rootpath):
        path = os.path.join(rootpath, item)
        print(path)

        num = int(item.split('_')[1].split('.')[0])
        if num > 20:
            num -= 1
        num -= 3
        print(num)

        r = num // 18
        c = num % 18

        os.rename(path, os.path.join(rootpath, '{}_{}.jpg'.format(r, c)))


if __name__ == '__main__':
    rename(r'C:\Users\marz\Desktop\images')
