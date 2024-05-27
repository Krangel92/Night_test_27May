class Animal():
    def __init__(self, name, color):
        self.name = name 
        self.color = color

    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def changeName(self, new_name):
        self.name = new_name
        return self.name
    
animal1 = Animal('buddy', 'black')
animal1.getName()
