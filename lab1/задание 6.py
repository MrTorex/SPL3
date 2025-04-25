set1 = input("Enter first set: ").split()
set2 = input("Enter second set: ").split()
set1 = {int(num) for num in set1}
set2 = {int(num) for num in set2}

for i in set1:
    if i in set2:
        print(i, end=' ')