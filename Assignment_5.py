print("the H.C.F of two input number")

def H_C_F(x,y):

    while(y):

        x, y = y, x % y

    return x

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

print("The H.C.F of", num1, "and", num2, "is", H_C_F(num1, num2))