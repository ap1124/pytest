listt = list(input("Enter the list: ").split())
#take list from user

list1 = [int(i) for i in listt]
#change each element to int

sval = int(input("Enter shift value: "))
#take rotation value

i = [*range(len(list1))]
list2 = list(map(lambda i : list1[(i+sval)%len(list1)] , i ))
#perform and store rotated list

print(f"Original list: {list1}\nOutput list: {list2}")
