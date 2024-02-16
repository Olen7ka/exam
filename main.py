a = []
for i in range(1, 20):
    a.append(2 ** i)
for x in range(31*2031, 10 ** 9, 31*2031):
    s = str(x)
    if '31' in s and s[-3:-1] == '65':
        delit = []
        for i in range(1, round(x ** 0.5)):
            if x % i == 0:
                delit.append(i)
                delit.append(x // i)
        if len(delit) in a:
            print(x, x // 2031)
print('hello, world!')