#Using the concept of object oriented programming and inheritance,create a super class named vehicles, which has two sub classes named car and bike.
#Define two methods in the vehicles class named getspecs and displayspecs, to get the specifications and display the specifications of the vehicles.
#You can use any specifications which you want.
#The car class and the bike class should have one specification which is exclusive to them
#for example wheels can have marks as a special specification.
#Make sure that the sub classes have their own methods to get and display their special specification.
#Create an object of car/ bike and make sure to call all the methods from the vehicle class as well as the methods from the own class.
class vehicles :
    def __init__(self):
        self.brand="default"
        self.make="default"
        self.color ="default"
        self.topspeed = "default"
    def getspecs(self):
        self.brand = input(" please enter brand Name : ")
        self.make = input("please enter make year : ")
        self.color = input("please enter color : ")
        self.topspeed = input("please enter top speed : ")
    def putspecs(self):
        print("Vehicle Brand : ",self.brand)
        print("Vehicle make(year) : ", self.make)
        print("Vehicle color : ", self.color)
        print("Vehicle top speed : ", self.topspeed)
class car (vehicles):
    def __init__(self):
        self.fueltype = "default"
    def getcarspec(self):
        print("Enter details of your Car")
        vehicles.getspecs(self)
        self.fueltype = input("Please enter fuel used : ")
    def putcarspec(self):
        vehicles.putspecs(self)
        print ("fuel type : ",self.fueltype)
class bike (vehicles):
    def __init__(self):
        self.pillion = "default"
    def getbikespec(self):
        print("Enter details of your Bike")
        vehicles.getspecs(self)
        self.pillion = input("Is Pillion seat available(y/n) : ")
    def putbikespec(self):
        vehicles.putspecs(self)
        print ("Pillion seat available : ",self.pillion)
obj1 = car()
obj2 = bike()
obj1.getcarspec()
obj1.putcarspec()
obj2.getbikespec()
obj2.putbikespec()
