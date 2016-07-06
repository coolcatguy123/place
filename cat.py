import math
n = int(input("Enter a whole number greater than 0: "))
b = (math.factorial(n)) + 2
a = 1
while 1 <= n:
    a = a * n
    n = n - 1
if a == b:
    print (a)
else: 
    print ("ERROR :(")
