import json
from datetime import datetime
import sys

"""
"Add_Strategy: {
    "Strategy_Name": user_input,
    "Frequency":     user_select_from_list,
    "Start_Date":    user_input,
    "Period_Amount": user_input}

"""
class accumulation_strategy:
    def __init__(self, name, frequency, amount, start_date):
        self.name = name
        self.frequency = frequency
        self.amount = amount
        self.start_date = start_date

    def add_strategy(self):
        with open('configurations.json', 'r') as file:
            data = json.load(file)
        
        accumulation = {
            self.name: {
                "frequency": self.frequency,
                "amount": self.amount,
                "start_date": self.start_date
            }
        }

        data["Accumulation_Strategy"] = accumulation

        with open('strategies.json', 'w') as file:
            json.dump(data, file, indent=2)

def validate_date_input(user_input):
    try:
        datetime.strptime(user_input, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def choose_frequency():
    frequencies_list = ["Daily", "Weekly", "Bi-weekly", "Bi-Monthly", "Monthly", "Quarterly"]
    for i, frequency in enumerate(frequencies_list, start=1):
        print(f"{i}, {frequency}")

    while True:
        try:
            frequency_choice = int(input("Enter the number cooresponding to the period of your accumulation strategy: "))
            if 1 <= frequency_choice <= len(frequencies_list):
                return frequencies_list[frequency_choice - 1]
            else:
                print("Invalid input. Please enter a number within the provided range.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



def add_investment_accumlation_strategy():
    name = input("Enter the name of the strategy: ")

    frequency_choice = choose_frequency()
    
    # add validation that this can be turned into an integer here
    amount = input("Enter the $ amount to be invested per period: ")

    # should add additional validation that the start date isn't in the past
    start_date = input("Enter a date in the format YYYY-MM-DD: ") 
    while validate_date_input(start_date) is False:
        start_date = input("Enter a date in the format YYYY-MM-DD: ")
        if start_date == "0":
            sys.exit()

    # validate the details of the new accumulation strategy we want to setup
    print(f"""A new accumulation strategy will be setup as follows: 
          
        Name of Strategy: {name}
        Frequency: {frequency_choice}
        Amount per Period: {amount}
        Start Date: {start_date}
    """)
    
    accept_strategy = input("Do you want to setup this new strategy? Only y or n will be accepted: ")
    if accept_strategy == "y":
        new_strategy = accumulation_strategy(name, frequency_choice, amount, start_date)
        new_strategy.add_strategy()
