# Variable Length Arguments **kwargs (keyword arguments)
import random


def time_activity(*args, **kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spend {min} for {kwargs[choice]}")


time_activity(10, 20, 10, hobby="Play", sport="Soccer", work="Developer")
