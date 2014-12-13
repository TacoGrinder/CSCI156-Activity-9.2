__author__ = 'ortus'


def qq(m):
    i = 1
    while i != 0:
        x = input("Input:")
        x.upper()
        if x == "q":
            return
        else:
            m.write(x.upper()+"\n")
    m.close()

def qareyou(n):
    for line in n:
        print(line.upper())
    n.close()

with open('rw.txt', 'w+', encoding='utf-8') as f:
    qq(f)
with open('rw.txt', 'r', encoding='utf-8') as f:
    qareyou(f)