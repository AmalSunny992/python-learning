def division(dividend,divisor):
    try:
        return (dividend/divisor)
    except:
        if (divisor == 0):
            print ("division by zero not possible")
            return 0
x = float(input("enter dividend : "))
y = float(input("enter divisor : "))
print (division(x,y))
