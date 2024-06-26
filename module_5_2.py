class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

zel = House(0)
zel.setNewNumberOfFloors(8)
