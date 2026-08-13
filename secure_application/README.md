# Cryptocurrency Wallet Management System

## Secure Application Development (SAST) Assignment

### Group Details

**Group Number:** 16

**Team Members:**
- Darshil Saini
- Abhishek Saini

---

# Project Overview

This project is a console-based Cryptocurrency Wallet Management System developed in Python as part of the Secure Application Development assignment.

The application allows users to:

- User Login
- Create Wallet
- Deposit Money
- Withdraw Money
- Check Balance
- View Transaction History
- Search Wallet
- Update Wallet Details
- Delete Wallet
- Display All Wallets
- Transfer Money Between Wallets

The project intentionally contains a few security vulnerabilities so that Static Application Security Testing (SAST) tools can detect and report them.

---

# Project Structure

```
secure_application/
│
├── src/
│   ├── main.py
│   ├── menu.py
│   ├── login.py
│   ├── wallet.py
│   ├── wallet_service.py
│   ├── wallet_manager.py
│   ├── transaction.py
│   └── transaction_request.py
│
├── reports/
├── screenshots/
├── sast/
├── outputs/
├── testcases/
└── README.md
```

---

# Technologies Used

- Python 3
- Git
- GitHub
- Static Application Security Testing (SAST)

---

# Modules

## login.py

Handles user authentication using hardcoded credentials.

---

## wallet.py

Represents a cryptocurrency wallet.

Stores:

- Wallet ID
- Owner Name
- Email
- Balance
- Transaction History

---

## transaction.py

Stores transaction details such as:

- Transaction Type
- Amount
- Timestamp
- Sender Wallet
- Receiver Wallet

---

## wallet_service.py

Contains all business logic including:

- Create Wallet
- Deposit
- Withdraw
- Balance Inquiry
- Transaction History

---

## wallet_manager.py

Provides wallet management features:

- Search Wallet
- Update Wallet
- Delete Wallet
- Display All Wallets

---

## transaction_request.py

Implements wallet-to-wallet money transfer.

---

## menu.py

Provides the console-based user interface.

---

## main.py

Entry point of the application.

---

# Features

- User Authentication
- Wallet Creation
- Deposit Funds
- Withdraw Funds
- Balance Inquiry
- Transaction History
- Wallet Search
- Wallet Update
- Wallet Deletion
- Display All Wallets
- Money Transfer

---

# Vulnerabilities Introduced

## 1. Hardcoded Credentials

Location:

```
login.py
```

Example:

```python
username = "admin"
password = "admin123"
```

Risk:

Anyone with source code access can view the credentials.

Recommended Fix:

- Store credentials securely
- Hash passwords
- Use environment variables or a database

---

## 2. Broken Access Control

Location:

```
wallet_manager.py
```

Example:

Users can update or delete any wallet without verifying ownership.

Risk:

Unauthorized users can modify or delete other users' wallets.

Recommended Fix:

- Verify wallet ownership
- Implement authorization checks
- Apply role-based access control

---

## 3. Weak Authentication

The login system uses a simple username/password without:

- Password hashing
- Multi-factor authentication
- Login attempt limits

Risk:

Easy brute-force attacks.

Recommended Fix:

- Hash passwords
- Enforce strong password policies
- Implement account lockout and MFA

---

# How to Run

Navigate to the source directory:

```bash
cd secure_application/src
```

Run the application:

```bash
python3 main.py
```

---

# Sample Login Credentials

Username:

```
admin
```

Password:

```
admin123
```

---

# Team Contribution

### Person A

- wallet.py
- transaction.py
- wallet_service.py
- main.py

### Person B

- login.py
- wallet_manager.py
- transaction_request.py
- menu.py

---

# Future Improvements

- Secure password storage using hashing
- Database integration
- Multi-factor authentication
- Role-based access control
- Encryption of sensitive data
- Improved input validation
- REST API support
- Graphical User Interface (GUI)

---

# License

This project was developed solely for academic purposes as part of the Secure Application Development laboratory assignment.