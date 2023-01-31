# Keywords arguments
def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy}% efficacy.")
    if (efficacy > 50) and (efficacy < 75):
        print("Seems not so effective, needs more trial.")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy > 90:
        print("Sure, will take the shot.")
    else:
        print("Needs many more trials.")


vac_feedback("Pfizer", 95)
vac_feedback("Unknown", 45)
vac_feedback(vac="Unknown", efficacy=45)


def time_activity(*args, **kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spend {min} for {kwargs[choice]}")
