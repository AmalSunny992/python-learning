# Q1. List out all the even numbers from 2 to 222 using lists in Python.

even = [e for e in range(2,223) if e%2 == 0 ]
print (even)

# Q2. List out all the odd numbers from 3 to 99 using lists in Python.

odd = [o for o in range (3,100) if o%2 != 0]
print (odd)

print(type(even))
print(type(odd))
