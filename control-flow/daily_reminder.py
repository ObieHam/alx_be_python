Task = input("What is the Task?")
Priority = input("What is the Task's priority? (high, medium, or low)").lower()
Time_bound = input("is the Task time-bound? (yes, no)?").lower()
match Priority:
    case _ if Time_bound == "yes":
        print(f"{Task} is a high priority task that requires immediate attention today!")
    case _:
        print(f"{Task} is a low priority task. Consider completing it when you have free time.")
