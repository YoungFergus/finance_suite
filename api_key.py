import os 
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()

    existing_api_key = os.getenv("API_KEY")

    api_key = input("Please enter your API key: ")

    # Check if the API key is empty, return if it is
    if api_key == "":
        print("API key cannot be empty. Returning to main menu.")
        return
    
    if existing_api_key is not None:
        print("API key found")
        with open('.env', 'r') as file:
            lines = file.readlines()

        with open('.env', 'w') as file:
            for line in lines:
                if line.startswith("API_KEY="):
                    file.write(f"API_KEY={api_key}\n")
                else:
                    file.write(line)        
    else:
        print("API key not found")
        with open('.env', 'a') as file:
            file.write(f'\nAPI_KEY={api_key}')
    

def load_api_key():
    load_dotenv()

    api_key = os.getenv("API_KEY")
    return api_key
