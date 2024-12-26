task = input("What is the task?")
priority = input("What is the task's priority? (high, medium, or low)").lower()
time_bound = input("is the task time-bound? (yes, no)?").lower()
match priority:
    case _ if time_bound == "yes":
        print(f"{task} is a high priority task that requires immediate attention today!")
    case _:
        print(f"{task} is a low priority task. Consider completing it when you have free time.")
