list_1 = []
list_2 = []
list_3 = []
list_4 = []

print("enter value of list_1:")
num_1 = int(input("1st value list_1 :"))
num_2 = int(input("2nd value list_1 :"))
num_3 = int(input("3rd value list_1 :"))
num_4 = int(input("4th value list_1 :"))

list_1.append(num_1)
list_1.append(num_2)
list_1.append(num_3)
list_1.append(num_4)

print("enter value of list_2 :")
num_1 = int(input("1st value list_2 :"))
num_2 = int(input("2nd value list_2 :"))
num_3 = int(input("3rd value list_2 :"))
num_4 = int(input("4th value list_2 :"))

list_2.append(num_1)
list_2.append(num_2)
list_2.append(num_3)
list_2.append(num_4)

print("enter value of list_3 :")
num_1 = int(input("1st value list_3 :"))
num_2 = int(input("2nd value list_3 :"))
num_3 = int(input("3rd value list_3 :"))
num_4 = int(input("4th value list_3 :"))

list_3.append(num_1)
list_3.append(num_2)
list_3.append(num_3)
list_3.append(num_4)

print("enter value of list_4 :")
num_1 = int(input("1st value list_4 :"))
num_2 = int(input("2nd value list_4 :"))
num_3 = int(input("3rd value list_4 :"))
num_4 = int(input("4th value list_4 :"))

list_4.append(num_1)
list_4.append(num_2)
list_4.append(num_3)
list_4.append(num_4)

print("value of list_1, list_2, list_3, list_4 :")
print("list_1:", list_1)
print("list_2:", list_2)
print("list_3:", list_3)
print("list_4:", list_4)

sum_1 = 0
for num_1 in list_1:
    sum_1 += int(num_1)

sum_2 = 0
for num_2 in list_2:
    sum_2 += int(num_2)

sum_3 = 0
for num_3 in list_3:
    sum_3 += int(num_3)

sum_4 = 0
for num_4 in list_4:
    sum_4 += int(num_4)

if (sum_1 > sum_2) and (sum_1 > sum_3) and (sum_1 > sum_4):
    highest = sum_1
    print("the sum with the highest element is in :" ,list_1)

elif (sum_2 > sum_1) and (sum_2 > sum_3) and (sum_1 > sum_4):
    highest = sum_2
    print("the sum with the highest element is in :", list_2)

elif (sum_3 > sum_1) and (sum_3 > sum_2) and (sum_3 > sum_4):
    highest = sum_3
    print("the sum with the highest element is in :", list_3)

else:
    highest = sum_4
    print("the sum with the highest element is in :", list_4)