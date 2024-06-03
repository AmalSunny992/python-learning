#Code Challenge 8
#Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price to 10%.
# Function number 2 is for additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both the discounts on the products.
# Design the above two mentioned functions and apply them both simultaneously on the price.
def stu_disc (curr_price):
    return curr_price - (curr_price*(10/100))
def reg_disc(curr_price):
   return curr_price - (curr_price*(5/100))

price = float(input("enter the price of product : "))
cust = input("enter the type of customer r: regular , s: student : ")
if (cust == 'r'):
    print("Price after Regular discount is Rs %3.2f"%(reg_disc(stu_disc(price))))
elif (cust == 's'):
    print("Price after Student discount is Rs %3.2f" %(stu_disc(price)))
else :
    print("no discount")
