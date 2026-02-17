num1=int(input("Enter the number "))    ## num -> square -> reverse -> -> square root -> reverse

sq=num1**2
## reverse 144 to 441
sq=str(sq)
rev=sq[-1::-1]
# typecasete rev str to int
rev=int(rev)
num1=int(num1)
sqrt=sq**(0.5)



print(num1)
print(sq)
print(sqrt)
print(type(rev))

