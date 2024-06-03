#Print Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89, 144

def fibo(x):
    if (x==0) or (x==1):
        return x
    else:
        return fibo(x-1)+fibo(x-2)

y = int(input("please enter a positive number : "))
i=0
while (i <= y):
    print (fibo(i))
    i+=1
