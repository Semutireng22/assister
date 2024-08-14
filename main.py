import requests
import time
from termcolor import colored

# Baca token dari file auth.txt
def read_auth_tokens(filename='auth.txt'):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

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
    tokens = read_auth_tokens()
    for token in tokens:
        headers = {"Authorization": f"Bearer {token}"}
        
        # Claim daily points
        print(colored("\n=== Processing Account ===", 'magenta'))
        claim_daily_points(headers)
        
        # Get and display account data
        account_data = get_account_data(headers)
        if account_data:
            display_account_data(account_data)
        
        print(colored("\nWaiting 24 hours before the next claim...\n", 'blue'))
        time.sleep(86400)  # Wait for 24 hours

if __name__ == "__main__":
    main()
