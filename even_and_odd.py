################## count of even numbers and odd numbers #################

user = int(input("Enter the values: \n"))
user += 1
i = 0
print("It is either even nor odd:   " , i)
for j in range(1,user):
    if j%2 == 0 :
        print("The even numbers is: ", j)
    else :
        print("The odd numbers is:  ", j)
