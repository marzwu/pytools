# encode=utf-8
import os


def rename(rootpath, src, des):
    for item in os.listdir(rootpath):
        path = os.path.join(rootpath, item)
        print(path)

        item = item.replace(src, des)
        os.rename(path, os.path.join(rootpath, item))


if __name__ == '__main__':
    rename(r'C:\Users\DELL\Desktop\2017-08-15', 'png', 'jpg')
