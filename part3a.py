__author__ = 'ortus'


def qq(m):
    i = 1
    while i != 0:
        x = input("Input:")
        x.upper()
        if x == "q":
            return
        else:
            m.write(x+"\n")
    m.close()

with open('rw.txt', 'w+', encoding='utf-8') as f:
    qq(f)

