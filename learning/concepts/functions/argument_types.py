#args - puts all inputs into tuples
def add_master_2000(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print(add_master_2000(1,2,3,4,5,6,7,8,9,20,10))

#kwargs - puts all inputs into dicttionaries
def hello(**NAME):
    print("hello")
    for key,value in NAME.items():
        print(value, end = " ")
hello(firstname = "gautham",secondname = "kaarthik",lastname = "santhosh sivabalan")

