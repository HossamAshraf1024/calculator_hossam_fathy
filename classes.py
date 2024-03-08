class Operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to be overridden by subclasses
    def do_operation(self):
        pass

class Addition(Operation):
    def do_operation(self):
        # Perform addition
        return self.x + self.y

class Subtraction(Operation):
    def do_operation(self):
        # Perform subtraction
        return self.x - self.y

class Multiplication(Operation):
    def do_operation(self):
        # Perform multiplication
        return self.x * self.y

class Division(Operation):
    def do_operation(self):
        # Perform division
        return self.x / self.y
