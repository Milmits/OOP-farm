import random

class Critten(object):
    """Моя зверушка"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "Объект класса Critten\n"
        rep += "Имя: " + self.name + "\nГолод: " + str(self.hunger) + "\nСкука: " + str(self.boredom) + "\nНастроение: " + str(self.mood)
        return rep
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "Отличное"
        elif unhappines <=10:
            m = "Хорошее"
        elif unhappines <= 15:
            m = "Нормальное"
        else:
            m = "Плохое"
        return m
    def talk(self):
        print("Меня зовут:", self.name, "\nУровень голода:", self.hunger, "\nНастроение:", self.boredom)
        print("Настроение: ", self.mood, "\n")
        self.__pass_time()
    def eat(self):
        food = int(input("Сколько еды вы хотите дать?"))
        if food <= 0:
            print("ВОзможно вы сделали что-то не так!")
            return self.eat()
        elif food == "":
            print("ВОзможно вы сделали что-то не так!")
            return self.eat()
        print("Мррр, спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self):
        fun = int(input("Сколько часов вы хотите поигать?"))
        if fun <= 0:
            print("ВОзможно вы сделали что-то не так!")
            return self.play()
        elif fun == " ":
            print("ВОзможно вы сделали что-то не так!")
            return self.play()
        print("Уииии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

class ZooFarm:
    """Зооферма"""
    def __init__(self):
        self.critters = []

    def add_critter(self, critter):
        self.critters.append(critter)

    def feed_all(self):
        for critter in self.critters:
            critter.eat()

    def play_all(self):
        for critter in self.critters:
            critter.play()

    def check_all_mood(self):
        for critter in self.critters:
            critter.talk()



def main():
    zoo = ZooFarm()
    num_critters = int(input("Сколько зверей хотите создать?"))
    for i in range(num_critters):
        crit_name = input(f"Назовите зверушку {i + 1}: ")
        crit = Critten(crit_name)
        zoo.add_critter(crit)


    secret_code = "020179"
    choice = None
    while choice != "0":
        print \
            ("""
            Зооферма

            0 - Выйти
            1 - Узнать самочувствие всех зверюшек
            2 - Покормить всех зверюшек
            3 - Поиграть со всеми зверюшками
            """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            zoo.check_all_mood()

        # feed your critter
        elif choice == "2":
            zoo.feed_all()

        # play with your critter
        elif choice == "3":
            zoo.play_all()

        elif choice == "9":
            code = input("Введте секретный код: ")
            if code == secret_code:
                print(zoo)
            else:
                print("Неверный код")


        # some unknown choice
        else:
            print("\nИзвините, но", choice, "нет в меню выбора")

main()
