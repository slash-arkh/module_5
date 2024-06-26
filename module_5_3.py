class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors or self.buildingType == other.buildingType

house = Building(2, '3') #Ставим один из атрибутов одинаковым и в консоли получаем True
house_1 = Building(1, '2') #Ставим различные атрибуты и в консоли получаем False
print(house == house_1)