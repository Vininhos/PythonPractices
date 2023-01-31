import random

vaccines = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

random.shuffle(vaccines)
print(vaccines)

lucky = random.choice(vaccines)
print(lucky)

for vac in vaccines:
    print(f"*********TESTING VACCINE {vac}*********")
    if vac == lucky:
        print(f"{lucky} vaccine, test successful")
        print()
        continue
    print("XXXXXXXXXXXXX")
    print("Test failed.")
    print("XXXXXXXXXXXXX")
