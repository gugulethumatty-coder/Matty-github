CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3

def input_strip(prompt):
    return input(prompt).strip()

def authenticate():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        pin = input_strip("Enter 4-digit PIN: ")
        if not pin.isdigit():
            print("PIN must contain digits only.")
        elif pin == CORRECT_PIN:
            return True
        else:
            print("Incorrect PIN.")
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining:
            print(f"{remaining} attempt(s) remaining.")
    print("Too many failed attempts. Exiting.")
    return False

def get_menu_choice():
    print("\nOptions:")
    print("1) Check balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Exit")
    while True:
        choice = input_strip("Choose an option (1-4): ")
        if choice in ("1","2","3","4"):
            return int(choice)
        print("Invalid choice. Enter 1, 2, 3 or 4.")

def get_amount(prompt):
    while True:
        s = input_strip(prompt)
        try:
            amt = float(s)
        except ValueError:
            print("Enter a numeric amount.")
            continue
        if amt <= 0:
            print("Amount must be greater than 0.")
            continue
        return amt

def main():
    balance = 1000.00
    print("Simple ATM Simulator")
    if not authenticate():
        return
    while True:
        choice = get_menu_choice()
        if choice == 1:
            print(f"Current balance: {balance:.2f}")
        elif choice == 2:
            amt = get_amount("Enter amount to deposit: ")
            balance += amt
            print(f"Deposited {amt:.2f}. New balance: {balance:.2f}")
        elif choice == 3:
            amt = get_amount("Enter amount to withdraw: ")
            if amt > balance:
                print("Insufficient funds.")
            else:
                balance -= amt
                print(f"Withdrew {amt:.2f}. New balance: {balance:.2f}")
        else:  # Exit
            print("Thank you. Goodbye.")
            break

if __name__ == "__main__":
    main()
