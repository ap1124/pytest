class Dogs:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Pets:
    l1 = []
    def __init__(self,list1):
        for i in list1:
            self.l1.append(i)
        print(f"I have {len(self.l1)}")
        for i in self.l1:
            print(f"{i.name} is {i.age}")
        print("And they're all mammals, of course.")

tom = Dogs("Tom",6)
flet = Dogs("Fletcher",7)
lar = Dogs("Larry",9)

p_obj = Pets([tom, flet, lar])
