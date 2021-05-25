class Parent:
    def __init__(self,lastname,age,height,looks):
        self.lastname= lastname
        self.age=age
        self.height=height
        self.looks=looks

    def getLastname(self):
        return self.lastname

    def getAge(self):
        return self.age
    
    def getHeight(self):
        return self.height
    
    def getLooks(self):
        return self.looks

class Child(Parent):
    def __init__(self, lastname, height, age, looks,weight):
        super().__init__(lastname,height,age,looks)
        self.weight=weight

    def getWeight(self):
        return self.weight

shriju=Child("Baral","1","20cm","Nice","5")
print("Lastname:",shriju.getLastname())
print("Age:",shriju.getAge())
print("height:",shriju.getHeight())
print("looks:",shriju.getLooks())
print("weight:",shriju.getWeight())