# Banking System

## Overview
This is a simple banking system implemented in Python using CSV file handling for data storage and SHA-256 hashing for password security. Users can **create an account, log in, deposit, and withdraw money**.

## Features
- **Account Creation**: Users can create an account by providing a username, email, and password.
- **Secure Login**: Passwords are hashed for security.
- **Deposit Money**: Users can deposit a valid amount into their account.
- **Withdraw Money**: Users can withdraw money if they have sufficient balance.
- **CSV File Storage**: Stores user data in `bank_info.csv`.

## Technologies Used
- Python
- CSV for data storage
- hashlib for password hashing

## Installation & Setup
### Prerequisites
- Python 3 installed on your system

### Clone the Repository
```bash
git clone https://github.com/BaburSadiqi/Banking_System.git
cd Banking_System
```

### Run the Program
```bash
python banking_system.py
```

## How to Use
1. **Account Creation**:
   - Run the program and enter your name, email, and password.
   - Your account will be created, and details will be stored securely.

2. **Login**:
   - Select `1` for login.
   - Enter your username and password.

3. **Deposit Money**:
   - Select `2` and enter the amount to deposit.

4. **Withdraw Money**:
   - Select `3` and enter the amount to withdraw.

5. **Quit the Program**:
   - Select `4` to exit the application.

## File Structure
```
Banking_System/
│── banking_system.py  # Main Python file
│── bank_info.csv      # User data storage
│── README.md          # Project documentation
```

## Author
**Babur Sadiqi**


