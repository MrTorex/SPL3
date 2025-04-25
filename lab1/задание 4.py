str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("String are annagrams.")
else:
    print("String aren't annagrams.")
