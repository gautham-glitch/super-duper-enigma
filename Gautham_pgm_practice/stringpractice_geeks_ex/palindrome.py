###Python program to check whether the string is Symmetrical or Palindrome###

str = "Nithya"
revstr = str[::-1]
print(revstr)
if str == revstr:
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")