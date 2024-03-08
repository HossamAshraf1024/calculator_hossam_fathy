
class operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def areInputsValid(self):
            try:
                # Try converting input to float
                self.x = float(self.x)
                self.y = float(self.y)
                return True
            except ValueError:
                return False

    # to be overridden
    def do_operation(self):
        pass


"""
if operation.areInputsValid()
    operation.do_operation()
else 
    retry
"""
class addition(operation):
    def do_operation(self):
        return self.x + self.y


class subtraction(operation):
    def do_operation(self):
        return self.x - self.y


class multiplication(operation):
    def do_operation(self):
        return self.x * self.y


class division(operation):
    def do_operation(self):
        return self.x / self.y

