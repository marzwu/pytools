import win32clipboard as w

import win32con


def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()


while True:
    raw = int(input('>'))
    output = '((0x0100 * {}) + {}),//{}'.format(raw // 256, raw % 256, raw)
    print(output)
    setText(output)
