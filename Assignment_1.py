y = input("Enter a sentence :")

lower_case=0
upper_case=0
digit=0
specialchar=0

for x in y:
    if x.islower():
       lower_case +=1

    elif x.isupper():
            upper_case +=1

    elif x.isdigit():
        digit +=1

    else:
        specialchar +=1

print("Lower case :", lower_case)
print("Upper case :", upper_case)
print("Digit :",digit)
print("Special character :",specialchar)
print("All the count of your sentence.")
