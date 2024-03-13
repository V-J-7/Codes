class circle:
    pi=0;
    radius=0
    def __init__(self):
        self.radius=5
        self.pi=3.14159265358979
    def area(self):
        print("Radius:",self.radius)
        return self.pi*self.radius**2
C1=circle()
print(C1.area())
