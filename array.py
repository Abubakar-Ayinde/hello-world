import array as arr

a = arr.array('d', [1,2,3,4,5,6,7])

temp = 0
while temp < len(a):
    print(a[temp])
    temp += 1