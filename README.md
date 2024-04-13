# Звіт з лабораторної роботи №2. Довгий список параметрів. Надлишкові елементарні типи.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
### Мета: Аналіз та оптимізація методів з великою кількістю параметрів. Рефакторінг класів з надлишковими елементарними типами данних.

### Завдання 1: Наданий код

    def calculate_score(name, age, gender, height, weight, score1, score2, score3, score4, score5):
        # Бізнес-логіка для розрахунку загального рейтингу
        total_score = score1 + score2 + score3 + score4 + score5

        # Перевірка чи користувач є повнолітнім
        is_adult = True if age >= 18 else False

        # Виведення результатів
        print("Name:", name)
        print("Age:", age)
        print("Gender:", gender)
        print("Height:", height)
        print("Weight:", weight)
        print("Total Score:", total_score)
        print("Adult:", is_adult)

        # Приклад виклику функції
    calculate_score("John", 25, "Male", 175, 70, 85, 90, 75, 88, 92)

### 1.1 Аналіз

В коді присутньо багато параметрів, наприклад, функція "calculate_score" має велику кількість параметрів, що може зробити код важким для розуміння.

Частина бізнес-логіки, така як розрахунок загального рейтингу та перевірка на повноліття, змішана з кодом виведення результатів.

Та, можемо побачити, що функція очікує параметри у певному порядку, що може бути проблематичним при розширенні функціональності.

### 2.1 Рішення

Для оптимізації та полегшення розуміння коду можна використати об'єкт, щоб об'єднати пов'язані дані разом.

    class Person:
        def __init__(self, name, age, gender, height, weight):
            self.name = name
            self.age = age
            self.gender = gender
            self.height = height
            self.weight = weight

    def calculate_score(person, *scores):
        # Бізнес-логіка для розрахунку загального рейтингу
        total_score = sum(scores)

        # Перевірка чи користувач є повнолітнім
        is_adult = True if person.age >= 18 else False

        # Виведення результатів
        print("Name:", person.name)
        print("Age:", person.age)
        print("Gender:", person.gender)
        print("Height:", person.height)
        print("Weight:", person.weight)
        print("Total Score:", total_score)
        print("Adult:", is_adult)

    person_1 = Person("John", 25, "Male", 175, 70)
    calculate_score(john, 85, 90, 75, 88, 92)


Отже, ми створюємо клас Person, який зберігає інформацію про особу (ім'я, вік, стать, зріст та вага). Функція calculate_score приймає лише об'єкт Person та кортеж scores, який містить оцінки. Вона обчислює загальний бал та перевіряє, чи є особа повнолітньою, і виводить результати. Це дозволяє зменшити кількість параметрів функції та полегшити розуміння і подальше використання коду.


### Завдання 2: Наданий код 

    class User:
        type_engineer = 1
        type_manager = 2    

        def __init__(self, name, age, type, phone, phone_code):
            self.name = name
            self.age = age
            self.type = type
            self.phone = phone
            self.phone_code = phone_code

        def print_details(self):
            # Виведення інформації про користувача
            print("Name:", self.name)
            print("Age:", self.age)
            print("Type:", self.type)
            print("Phone:", self.phone_code + self.phone)

        # Приклад використання класу
        user = User("John", 25, User.type_engineer, "9379992", “050”)
        user.print_details()

### 1.2 Аналіз 

Тут можна замінити параметри об'єктом (name, age, type, phone та phone_code об'єктом), що передається конструктору.

Можна також застосувати заміну кодування типу класом: бо в нас є інженер та менеджер, можна їх замінити використовуючи підкласи.

Також, слід розділити клас User на два окремі класи для кожного типу користувачів.

### 2.2 Рішення

    class User:
        def __init__(self, name, age, phone, phone_code):
            self.name = name
            self.age = age
            self.phone = phone
            self.phone_code = phone_code

        def print_details(self):
            # Виведення інформації про користувача
            print("Name:", self.name)
            print("Age:", self.age)
            print("Phone:", self.phone_code + self.phone)

    class Engineer(User):
        def __init__(self, name, age, phone, phone_code):
            super().__init__(name, age, phone, phone_code)
            self.type = "Engineer"

    class Manager(User):
        def __init__(self, name, age, phone, phone_code):
            super().__init__(name, age, phone, phone_code)
            self.type = "Manager"

    engineer = Engineer("John", 25, "9379992", "050")
    manager = Manager("Aurora", 23, "1234567", "050")

    engineer.print_details()
    manager.print_details()

Тепер ми маємо два окремі класи - Engineer та Manager, які успадковують від класу User. Кожен з них має свій тип, інженер або менеджер, який визначається при створенні об'єкта. Такий підхід дозволяє легко визначати та використовувати різні типи користувачів та зберігати їх дані.
