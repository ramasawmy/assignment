x = int(input("Enter number: "))

def reverse(x):
    rev = 0

    while (x > 0):
        num = x % 10

        rev = rev * 10 + num

        x = x // 10

    return rev

z = reverse(x)

print("Reverse of the number:")


if (x == z):
    print("true")

else:
    print("false")