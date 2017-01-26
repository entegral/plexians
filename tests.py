

import database, models, person_controller

name = input("New Person\nName:\n")
email = input("Email:\n")
user_pin = input("Pin:\n")
phone = input("Phone:\n")
relation = input("Family, Friend, or other:\n")

someone = models.Person(name, email, user_pin, phone, relation)
database.addPerson(someone)
print(database.getFirstPerson)
