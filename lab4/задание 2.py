class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def movement(self):
        return "Движение"


class Fish(Animal):
    def movement(self):
        return "Плавает"


class Bird(Animal):
    def movement(self):
        return "Летает"


class PetStore:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def most_expensive_animal(self):
        if not self.animals:
            print("В магазине отсутствуют животные!")
            return None
        return max(self.animals, key=lambda animal: animal.cost)

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for animal in self.animals:
                file.write(f"Порода: {animal.breed}, Стоимость: {animal.cost}, Способ передвижения: {animal.movement()}\n")


store = PetStore()

store.add_animal(Fish("Рыба-клоун", 150))
store.add_animal(Fish("Окунёк", 1000))
store.add_animal(Bird("Попугай", 200))
store.add_animal(Bird("Голубь", 500))

most_expensive = store.most_expensive_animal()
print(f"Самая дорогая порода: {most_expensive.breed}, Стоимость: {most_expensive.cost}")

store.save_to_file("animals_info.txt")