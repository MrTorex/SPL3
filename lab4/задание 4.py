class Factory:
    total_factories = 0
    total_production_capacity = 0

    def __init__(self, name, location, production_capacity):
        self.name = name
        self.location = location
        self.production_capacity = production_capacity
        self.orders = []

        Factory.total_factories += 1
        Factory.total_production_capacity += production_capacity

    def add_order(self, product_name, quantity):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным.")
        self.orders.append({'product_name': product_name, 'quantity': quantity})
        print(f"Заказ на {quantity} единиц(ы) '{product_name}' добавлен на завод '{self.name}'.")

    def produce(self):
        if not self.orders:
            print(f"На заводе '{self.name}' нет текущих заказов.")
            return
        
        print(f"Начато производство на заводе '{self.name}':")
        for order in self.orders:
            if order['quantity'] <= self.production_capacity:
                print(f"Производится {order['quantity']} единиц(ы) '{order['product_name']}'.")
            else:
                print(f"Не хватает производственной мощности для {order['product_name']}, требуется {order['quantity']} единиц(ы), доступно только {self.production_capacity}.")
        self.orders = []

    @classmethod
    def average_production_capacity(cls):
        if cls.total_factories == 0:
            return 0
        return cls.total_production_capacity / cls.total_factories

    @classmethod
    def get_total_factories(cls):
        return cls.total_factories

    @staticmethod
    def validate_product_name(product_name):
        if not isinstance(product_name, str) or len(product_name) < 3:
            return False
        return True

    @staticmethod
    def calculate_production_time(quantity, production_capacity):
        if production_capacity <= 0:
            raise ValueError("Производственная мощность должна быть больше нуля.")
        time_required = quantity / production_capacity
        return round(time_required, 2)

factory1 = Factory("МАЗ", "Минск", 1000)
factory2 = Factory("БелАЗ", "Жодино", 1500)

factory1.add_order("Подшипник", 500)
factory2.add_order("Двигатель", 1200)

factory1.produce()
factory2.produce()

is_valid = Factory.validate_product_name("Болт")
print(f"Имя продукта валидно: {is_valid}")

time_needed = Factory.calculate_production_time(1200, 1500)
print(f"Необходимое время для производства: {time_needed} дней")

average_capacity = Factory.average_production_capacity()
print(f"Средняя производственная мощность всех заводов: {average_capacity} единиц")

total_factories = Factory.get_total_factories()
print(f"Общее количество заводов: {total_factories}")