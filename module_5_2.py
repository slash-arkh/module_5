class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

zel = House(2)
zel.setNewNumberOfFloors(8)
