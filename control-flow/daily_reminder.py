Task = input("Enter your task:")
Priority = input("Priority (high/medium/low:)")
Time_bound = input("Is it time-bound?(yes/no):")

match Priority:
  case "high":
    if Time_bound == "yes":
        print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
    else:
         print(f"Note: '{Task}' is a high priority task. Consider completing it when you have free time.")
  case "low":
    if Time_bound == "yes":
        print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
    else:
         print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
  case "medium":
    if Time_bound == "yes":
        print(f"Reminder: '{Task}' is a medium priority task that requires immediate attention today!")
    else:
         print(f"Note: '{Task}' is a medium priority task. Consider completing it when you have free time.")
    
