#!/usr/bin/env python
# coding: utf-8

# In[6]:


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


# In[ ]:




