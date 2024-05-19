users = {
    "deepu": {"password": "deepud7", "balance": 1800, "pin": "1111"},
    "isha": {"password": "ishad8", "balance": 2000, "pin": "2222"},
    "kavya":{"password": "kavyag1", "balance": 2500, "pin": "3333"},
    "kallu":{"password": "kallug2", "balance": 2800, "pin": "4444"}
}
def main():
    username = input("Enter username: ")

    if username not in users:
        print("User does not exist")
        return
    for attempt in range(3, 0, -1):
        password = input("Enter password: ")
        if password == users[username]["password"]:
            break
        else:
            if attempt > 1:
                print(f"Incorrect password, {attempt-1} more attempts are left")
            else:
                print("Incorrect password, account blocked")
                return
    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Change Password")
        choice = input("Enter your choice: ")
        if choice == "1":
            handle_withdraw(username)
        elif choice == "2":
            handle_deposit(username)
        elif choice == "3":
            handle_balance(username)
        elif choice == "4":
            handle_change_password(username)
        else:
            print("Invalid choice, try again.")
        break
def handle_withdraw(username):
    amount = float(input("Enter amount to withdraw: "))
    pin = input("Enter PIN: ")
    if pin != users[username]["pin"]:
        print("Incorrect PIN, ending transaction.")
        return
    if amount > users[username]["balance"]:
        print("Insufficient balance")
    else:
        users[username]["balance"] -= amount
        print(f"Amount withdrawn: {amount}")
        print(f"New balance: {users[username]['balance']}")
def handle_deposit(username):
    amount = float(input("Enter amount to deposit: "))
    pin = input("Enter PIN: ")
    if pin != users[username]["pin"]:
        print("Incorrect PIN, ending transaction.")
        return
    users[username]["balance"] += amount
    print(f"Amount deposited: {amount}")
    print(f"New balance: {users[username]['balance']}")
def handle_balance(username):
    pin = input("Enter PIN: ")
    if pin != users[username]["pin"]:
        print("Incorrect PIN, ending transaction.")
        return
    print(f"Current balance: {users[username]['balance']}")
def handle_change_password(username):
    current_password = input("Enter current password: ")
    if current_password != users[username]["password"]:
        print("Incorrect password, ending process.")
        return
    while True:
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password == confirm_password:
            users[username]["password"] = new_password
            print("Password changed successfully")
            break
        else:
            print("Passwords do not match, try again.")
if __name__ == "__main__":
    main()
