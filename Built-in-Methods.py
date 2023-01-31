# String Build in Methods/Functions
message = "corona vaccine is ready to use, most of them are more than 90% effective."
print(message)
print(message.capitalize())

# dir() function
print(dir(message))

print(message.upper())
print(message.islower())
print(message.isupper())
print(message.find("ready"))
print(message[18:24])

seq1 = ("192", "168", "40", "90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))

mountains = ["Everest", "Himalaya", "Sahyadri"]
print(mountains)

mountains.append("Oregon mount")
print(mountains)

mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)

mountains.insert(2, "Mt Abu")
print(mountains)

mountains.pop()
print(mountains)
mountains.pop(3)
print(mountains)

cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)
