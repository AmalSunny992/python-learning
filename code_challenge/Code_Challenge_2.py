##Python - Code Challenge 2
##1. Using a for-loop,
        ##a. calculates the addition of each number
            ##Eg:
                ##INPUT
                ##X= [10,20,30,40]
                ##OUTPUT
                    ##20
                    ##40
                    ##60
                    ##80
# ##Answer 1
x=[10,20,30,40]
for i in x:
    sum = i + i
    print(sum)
##---------------------OR-----------------------------------##
##Answer 2
x = []
for i in range(1000):
    num = input("Please enter a number for addition")
    x.append(int(num))
    choice = input ("Do you want to enter another number? y/n")
    if (choice == 'y' or choice =='Y') :
        continue
    else : break
    i+=1
print ("Result after addition: ")
for j in x:
    sum = j + j
    print(sum)



##b.Print “I Love My India" 7 times.


##Answer 1
x = ["I", "Love", "My", "India"]
for i in range(7):
    for j in x :
        print (j, end= ' ')
    print()

##----------------------OR----------------------##

##Answer 2
for i in range(7):
    print("I Love My India")
