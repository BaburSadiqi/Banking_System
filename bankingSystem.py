import csv  # for CSV file handling
import hashlib  # for password hashing

#main class
class Bank:
    bank_name = "BSI"
    branch_address = "L-Street, MZR-AFG"

    # Account creation
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self._email = email
        self._password = self._hash_password(password)  # Store hashed password
        self._balance = 0.0
        print(f"\nHello {self.user_name}, your account has been created successfully!")

        
        try:
            with open("bank_info.csv", mode="r", newline="") as file:
                existing_data = file.readlines()
        except FileNotFoundError:
            existing_data = []

        
        with open("bank_info.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if not existing_data:  # If file is empty, add headers
                writer.writerow(["Username", "Email", "Password", "Balance"])
            writer.writerow([self.user_name, self._email, self._password, self._balance])

    @staticmethod
    def _hash_password(password):
        """Hash password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    #login method
    def login(self, user_name, password):
        """Login function to authenticate a user."""
        try:
            with open("bank_info.csv", mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header

                hashed_password = self._hash_password(password)  # Hash input password

                for row in reader:
                    if row and row[0] == user_name and row[2] == hashed_password:
                        print(f"\nLogin successful! Welcome, {user_name}.")
                        return True

                print("\nInvalid username or password.")
                return False

        except FileNotFoundError:
            print("\nError: bank_info.csv not found.")
            return False
        
    #depositing method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"\n{amount} deposited successfully. Your new balance is {self._balance}")
        else:
            print("\nDeposit amount must be positive!")
            
    #withdraw method
    def withdraw(self, amount):
        if amount > self._balance:
            print("\nInsufficient funds! Withdrawal failed.")
        elif amount <= 0:
            print("\nInvalid withdrawal amount.")
        else:
            self._balance -= amount
            print(f"\n{amount} withdrawn successfully. Remaining balance: {self._balance}")


print(f"Welcome to {Bank.bank_name}, {Bank.branch_address}")
user_name = input("\nPlease enter your name: ")
email = input("\nPlease enter your Email address: ")
password = input("\nPlease enter your password: ")

bank = Bank(user_name, email, password)

while True:
    print("\nPlease Select an option:")
    print("1: Login\n2: Deposit\n3: Withdraw\n4: Quit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        print("\nLogin Required")
        ask_user = input("Enter your username: ")
        ask_password = input("Enter your password: ")

        if bank.login(ask_user, ask_password):  # Check login
            while True:
                print("\nSelect an option:")
                print("1: Deposit\n2: Withdraw\n3: Logout")

                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 1:
                    amount = float(input("Enter deposit amount: "))
                    bank.deposit(amount)
                elif sub_choice == 2:
                    amount = float(input("Enter withdrawal amount: "))
                    bank.withdraw(amount)
                elif sub_choice == 3:
                    print("\nLogging out...")
                    break
                else:
                    print("\nInvalid option, try again.")

    elif user_choice == 2:
        amount = float(input("\nEnter deposit amount: "))
        bank.deposit(amount)

    elif user_choice == 3:
        amount = float(input("\nEnter withdrawal amount: "))
        bank.withdraw(amount)

    elif user_choice == 4:
        print("\nThanks for using BSI Bank! Have a great day.")
        break

    else:
        print("\nInvalid choice, please try again.")
