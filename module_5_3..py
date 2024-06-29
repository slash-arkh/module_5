class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



    #def go_to(self, new_floor):
    #    if 1 <= new_floor <= self.number_of_floors:
    #        for i in range(1, new_floor+1):
    #            print(i)
    #    else:
    #        print('"Такого этажа не существует"')
#
   # def __len__(self):
   #     return self.number_of_floors
#
   # def __str__(self):
   #     return f'Название: {self.name}, кол-во этажей {self.number_of_floors}'
#
   # def __eq__(self, other):
   #     return self.number_of_floors == other.number_of_floors
#
   # def __lt__(self, other):
   #     return self.number_of_floors < other.number_of_floors
#
   # def __le__(self, other):
   #     return self.number_of_floors <= other.number_of_floors
#
   # def __gt__(self, other):
   #     return self.number_of_floors > other.number_of_floors
#
   # def __ge__(self, other):
   #     return self.number_of_floors <= other.number_of_floors
#
   # def __ne__(self, other):
   #     return self.number_of_floors != other.number_of_floors
#
   # def __add__(self, value):
   #     self.number_of_floors = self.number_of_floors + value
#
   # def __iadd__(self, value):
   #     self.number_of_floors = self.number_of_floors + value
#
   # def __radd__(self, value):
   #     self.number_of_floors = self.number_of_floors + value
#

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)

del h2
del h3

print(House.houses_history)


#print(h1)
#print(h2)
#
#print(h1 == h2)
#h1.__add__(10)
#print(h1)
#print(h1 == h2)
#
#h1.__iadd__(10)
#print(h1)
#h2.__radd__(10)
#print(h2)
#print(h1 > h2) # __gt__
#print(h1 >= h2) # __ge__
#print(h1 < h2) # __lt__
#print(h1 <= h2) # __le__
#print(h1 != h2) # __ne__

