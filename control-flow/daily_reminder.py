task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        if time_bound == "no":
            print(f"{task} is a high priority task that doesn't require immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires immediate attention today!")
        if time_bound == "no":
            print(f"{task} is a medium priority task that doesn't require immediate attention today!")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task that requires immediate attention today!")
        if time_bound == "no":
            print(f"{task} is a low priority task that doesn't require immediate attention today!")
    case _:
        print("Invalid response!")
