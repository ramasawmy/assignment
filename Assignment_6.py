list_1 = []
list_2 = []

list1 = int(input("Enter the length of list_1:"))
print("enter odd value in list_1:")

for i in range(list1):
    list1_value = int(input())
    list_1.append(list1_value)


list2 = int(input("Enter the length of list_2:"))
print("enter even value in list_2:")

for j in range(list2):
    list2_value = int(input())
    list_2.append(list2_value)

print("list_1 is :", list_1)
print("list_2 is :", list_2)

list_3 = []

for odd in list_1:
    if(odd % 2 != 0):
        list_3.append(odd)

    else:
        print("invalid")

for even in list_2:
    if(even % 2 == 0):
        list_3.append(even)

    else:
        print("invalid")

print("list_3 with odd value from list_1 and with even value from list_2 :", list_3)