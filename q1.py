import random

#function to return index list
def retIdx(list1,value):
    for iter1 in range(len(list1)):
    #iter1 holds index number
        if (value == list1[iter1]):
        #checks if value is at iter1 and if it does returns index value
            return iter1
    return -1

list1 = [random.randint(0,30) for i in range(random.randint(10,21))]
#creates list with random numbers with random length
print(f"List: {list1}")

svalue = int(input("Element to be searched: "))
#takes user given value to be searched

print(f"Element is present at location {retIdx(list1,svalue)}")
#calls the retIdx function and returns index value
