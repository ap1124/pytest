import random

listt = list(input("Enter the list: ").split())

list1 = [int(i) for i in listt]

sval = int(input("Enter shift value: "))
i = [*range(len(list1))]

list2 = list(map(lambda i : list1[(i+sval)%len(list1)] , i ))

print(f"Original list: {list1}\nOutput list: {list2}")
