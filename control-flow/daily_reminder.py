task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match priority:
    case _ if time_bound == "yes":
        print(f"{task} is a high priority task that requires immediate attention today!")
    case _:
        print(f"{task} is a low priority task. Consider completing it when you have free time.")
