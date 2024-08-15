import requests
import time
from termcolor import colored

# Baca token dari file auth.txt
def read_auth_tokens(filename='auth.txt'):
    try:
        with open(filename, 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]
            if not tokens:
                print(colored("No tokens found in auth.txt!", 'red'))
            return tokens
    except FileNotFoundError:
        print(colored(f"File {filename} not found!", 'red'))
        return []

# Function to make the POST request to claim daily points
def claim_daily_points(headers):
    url = "https://api.assisterr.ai/incentive/users/me/daily_points/"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(colored("Claim successful:", 'green'), response.json())
    else:
        print(colored("Claim failed:", 'red'), response.status_code, response.text)

# Function to get account data
def get_account_data(headers):
    url = "https://api.assisterr.ai/incentive/users/me/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(colored("Failed to fetch account data:", 'red'), response.status_code, response.text)
        return None

# Function to display account data with color and manual formatting
def display_account_data(data):
    print(colored("\n=== https://t.me/ugdairdrop ===", 'cyan'))
    print(f"{colored('ID:', 'yellow')} {data['id']}")
    print(f"{colored('Username:', 'yellow')} {data['username']}")
    print(f"{colored('Wallet ID:', 'yellow')} {data['wallet_id']}")

# Main execution loop for multiple accounts
def main():
    while True:
        tokens = read_auth_tokens()
        if not tokens:
            return  # Exit if no tokens are found
        
        for token in tokens:
            headers = {"Authorization": f"Bearer {token}"}
            
            # Claim daily points
            print(colored("\n=== Processing Account ===", 'magenta'))
            claim_daily_points(headers)
            
            # Get and display account data
            account_data = get_account_data(headers)
            if account_data:
                display_account_data(account_data)
            
            # Pause before processing the next token
            print(colored("\nPausing for 10 seconds before processing the next account...\n", 'blue'))
            time.sleep(10)

        # Pause for 13 hours before repeating the process
        print(colored("\nAll accounts processed. Pausing for 13 hours before starting again...\n", 'blue'))
        time.sleep(46800)  # 13 hours in seconds

if __name__ == "__main__":
    main()
