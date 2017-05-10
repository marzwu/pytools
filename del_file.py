import os

if __name__ == '__main__':
    lst = os.listdir(r'F:\xxx')
    for i in lst:
        if '(' in i:
            os.remove('F:/xxx/' + i)
