lower = 0
upper = 0
vowels = "eyuoaуеыаоэяию"
vowels_num = 0

s = input()

for i in s:
    if i.lower() in vowels:
        vowels_num += 1

for i in range (0, len(s) - 1):
    if s[i].isupper() and s[i+1].isupper():
        upper += 1
        
    if s[i].islower() and s[i+1].islower():
        lower += 1

print("Upper: ", upper, ", Lower: ", lower, ", Vowels: ", vowels_num)