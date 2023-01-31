vaccines = ("Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca")

for v in vaccines:
    print("")
    print("I would like to take a shot of")
    for i in v:
        print(i)

import time
x = 2
while True:
    print("Value of X is:", x)
    print("Looping...")
    x *= 2
    time.sleep(1)
