import sys
import os
from api_key import get_api_key

ACTIONS = {1: "Create New Investment", 2: "Modify Current Investment", 3: "Add or Modify API key"}
CONTROLS = {}
loop = 1

print("Welcome to the Financial Strategy Manager \n")

while loop == 1:
    print("Please select an action (0 to exit): ")
    for key, value in ACTIONS.items():
        print(f"{key} - {value}")

    action = int(input("Action: "))

    if action == 0:
        sys.exit(0)
    else:
        input_functions = {1: "pass", 2: "pass", 3: get_api_key()}
        input_functions[action]