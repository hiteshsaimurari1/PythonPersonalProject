class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale,Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("Move in water")

nemo = Fish()

print(nemo.num_eyes)
nemo.breathe()
nemo.swim()
