class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity


    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity


    def status(self):
        final_status = self.size - self.quantity
        return final_status


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
