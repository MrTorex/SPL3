l = input("Enter elements: ").split()
l = [int(num) for num in l]
m = 1

for i in range(0, len(l), 2):
    m *= l[i]
    
print("Lenght: ", len(l), ", m: ", m)