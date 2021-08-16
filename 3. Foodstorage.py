#item sortieren

#foodsorter for Gordon Ramsey
from datetime import datetime

date = datetime.now()

storageList = [1,2,3]
dateStoredItem =[1,2,3]
counter = 0
contin = input("Press y if you want to continue ")  

while storageList[2] == 3:
    while contin == "y":
        Items = ["Meat", "Fish", "Veggies"]
        print("pls Choose the Item you want to Add", Items)

        addItem = [input("What food do you want to add? "), print("The food gets added at ", date) ]
        addItem[0] = addItem[0].lower()
        addItem[1] = 2021

        if addItem[0] == "meat" or addItem[0] == "veggies" or addItem[0] == "fish":
            print(addItem[0], "has been added to the Kitchen")

            addedItem = addItem[0]
            
            storageList[counter] = addedItem 
            counter = counter + 1
            
        else:
            print("This food doesn't exist. Pls try again")
            
        if storageList[2] == 3:
            contin = input("Press y if you want to continue ")
        else:
            contin = "n"

    if storageList[2] != 3:
        print("The storage is Full!")
        print("Can't add any more Items!")
    else:
        print("Stopped adding Items")
    break

y = 0

for x in storageList:
    if x == "meat":
        dateStoredItem[y] = 2022 
                    
                    
    elif x == "fish":
        dateStoredItem[y] = 2025

    elif x  == "veggies":
        dateStoredItem[y] = 2021

    else: None
    y = y + 1

print(storageList)
print(dateStoredItem)

