## To show or get the all function methods of numpy we can use 
import numpy as np
print("1️⃣  To list to numpy function/method.")
print("2️⃣  To Get the User manual of Functions.")

choose=int(input("Enter your choice: "))
if choose==1:
    list_of_function=dir(np)
    print(list_of_function)
elif choose==2:
    func=input("Enter your function/method: ")
    help(np.func)

else:
    print("🤔 Bad choice!\nChoose between 1️⃣ or 2️⃣")