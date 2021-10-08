class Vehicle:
    def __init__(self,regno,color):
        self.regno=regno
        self.color=color

class car(Vehicle):
    def __init__(self,regno,color):
        Vehicle.__init__(self,regno,color)

    def get_type(self):
        return "car"