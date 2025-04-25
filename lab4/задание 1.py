class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0

    def input_data(self):
        self.a = float(input("Введите первое число: "))
        self.b = float(input("Введите второе число: "))

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Ошибка: деление на ноль!"

calculator = Calculator()
calculator.input_data()

print("Сложение:", calculator.add())
print("Вычитание:", calculator.subtract())
print("Умножение:", calculator.multiply())
print("Деление:", calculator.divide())