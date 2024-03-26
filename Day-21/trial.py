class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal):
    def __init(self):
        super().__init__() 
        self.num_fins = 5
        
    def breathe(self):
        super().breathe()
        print("Underwater")
        
    def swim(self):
        print("moving in water.")
        
nemo = Fish()
nemo.swim()
nemo.breathe()

