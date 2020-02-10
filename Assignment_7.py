pharmacy_stock_1= ["medicine1", "medicine2", "medicine3", "medicine4", "medicine5"]

stock = input("which stock to add  :")
pharmacy_stock_1.append(stock )
print(pharmacy_stock_1)

pharmacy_stock_2=["medicine1", "medicine2", "medicine3", "medicine4", "medicine5"]

stock_to_remove = input("which stock to remove:")
if stock_to_remove in pharmacy_stock_2:
    pharmacy_stock_2.remove(stock_to_remove)
    print(pharmacy_stock_2)
else:
    print("that is not in the stock")

pharmacy_stock_3= ["medicine1", "medicine2", "medicine3", "medicine4", "medicine5"]

stock = input("insert a stock:")
pos = int(input("where to add stock:"))

if pos<len(pharmacy_stock_3):
    pharmacy_stock_3.insert(pos,stock)
    print(pharmacy_stock_3)
else:
    print("invalid")

print(pharmacy_stock_1)
print(pharmacy_stock_2)
print(pharmacy_stock_3)



