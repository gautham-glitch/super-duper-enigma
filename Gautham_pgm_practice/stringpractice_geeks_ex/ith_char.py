###Ways to remove i’th character from string in Python###

string = "bicycle"
i = int(input("put a number between 0-6: "))
list_of_str = list(string)
for x in range(0,len(list_of_str)+1):
    x+=1
    if x == i:
        removal = list_of_str[x]
list_of_str.remove(removal)
true_str = ''.join(list_of_str)
print(true_str)
