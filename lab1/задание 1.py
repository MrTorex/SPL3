x = int(input())
a = 0
b = False
while x/10 != 0:
    if (x%10)%2 == 0:
        b = True
    elif (x%10)%2 == 1:
        a = a + x%10
    x = int(x / 10)
if b:
    print(a)
else:
    print(0)
