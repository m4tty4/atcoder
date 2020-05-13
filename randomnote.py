a = 0
b = 36


List = []
n = 10000
for i in range(1, n + 1):
    x, y, z, w, v= 0, 0, 0, 0, 0
    x = i % 10
    if i >= 10:
        y = (i - x) % 100
        y = int(y / 10)
    if i >= 100:
        z = (i - x - y) % 1000
        z = int(z / 100)
    if i >= 1000:
        w = (i - x - y - z) % 10000
        w = int(w / 1000)
    if i >= 10000:
        v = (i - x - y - z) % 100000
        v = int(v / 10000)
    sumnum = x + y + z + w + v
    if sumnum >= a and sumnum <= b:
        List.append(int(i))
    print(i, x, y, z, w, v, sumnum, sep='\t')
print(sum(List))
