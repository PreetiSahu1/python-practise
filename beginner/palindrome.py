#----1----#using join reverse

s = input("Enter the name : ")
j= ''.join(reversed(s))

if s==j:
    print("this is palindrome")
else:
    print("this is not a palindrome")




#----2----# using slicing

s = "nitin"
if s==s[::1]:
    print("Palindrome")
else:
    print("Not a palindrome")