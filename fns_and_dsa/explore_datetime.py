import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

display_current_datetime()

def calculate_future_date():
    current_date = datetime.datetime.now()  # Keep current_date as a datetime object
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=number_of_days)  # Add timedelta directly
    print(f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")  # Format only for printing

calculate_future_date()
