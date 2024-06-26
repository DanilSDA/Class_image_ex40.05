class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} ({self.species})"

class StaffMember:
    def __init__(self, name):
        self.name = name

    def perform_duty(self, animal):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def __str__(self):
        return f"Сотрудник: {self.name}"
class ZooKeeper(StaffMember):
    def perform_duty(self, animal):
        return self.feed_animal(animal)

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}"

    def __str__(self):
        return f"Смотритель зоопарка: {self.name}"

class Veterinarian(StaffMember):
    def perform_duty(self, animal):
        return self.heal_animal(animal)

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}"

    def __str__(self):
        return f"Ветеринар: {self.name}"


class Zoo:
        def __init__(self):


            self.animals = []
            self.staff = []

        def add_animal(self, animal):
            self.animals.append(animal)
            print(f"Добавлено животное: {animal}")

        def add_staff(self, staff_member):
            self.staff.append(staff_member)
            print(f"Добавлен сотрудник: {staff_member}")

        def show_animals(self):
            print('Животные в зоопарке:')
            for animal in self.animals:
                print(animal)

        def show_staff(self):
            print("Персонал:")
            for man in self.staff:
                print(man)



my_zoo = Zoo()
slon  = Animal('Лука','Слон')
baran = Animal('Кузя','baran')
ivan = ZooKeeper('Иван')
lesha = Veterinarian('Алекс')
my_zoo.add_animal(slon)
my_zoo.add_animal(baran)
my_zoo.show_animals()
my_zoo.add_staff(lesha)
my_zoo.add_staff(ivan)
my_zoo.show_staff()
print(ivan.perform_duty(slon))
print(lesha.perform_duty(baran))






