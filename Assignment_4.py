print("the L.C.M of two input number")

def l_c_m(x, y):
    if x > y:
        z = x

    else:
        z = y

    while (True):
        if ((z % x == 0) and (z % y == 0)):
            l_c_m = z

            break

        z += 1

    return l_c_m

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1, "and", num2, "is", l_c_m(num1, num2))
