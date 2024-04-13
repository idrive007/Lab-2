#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[ ]:




