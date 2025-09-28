class Calculator:
        def __init__(self, num1,num2):
                self.num1 = num1
                self.num2 = num2

        def add(self):
                        return self.num1 + self.num2
                
        def subtract(self):
                        return self.num1 - self.num2
                
        def multiply(self):
                        return self.num1 * self.num2
        def divide(self):
                        if self.num2 == 0:
                                return "Error! Division by zero."
                        return self.num1 / self.num2
                
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

calc=Calculator(num1,num2)

print(f"Addition: {calc.add()}")
print(f"Subtraction: {calc.subtract()}")
print(f"Multiplication: {calc.multiply()}")
print(f"Division: {calc.divide()}")