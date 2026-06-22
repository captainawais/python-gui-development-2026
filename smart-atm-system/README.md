# 🏦 TechFact Bank ATM System v3.0

A modern and feature-rich ATM Simulation System built with Python and Tkinter. This project simulates the real workflow of an ATM machine, including card insertion, PIN authentication, cash transactions, account management, transaction history, ATM sounds, and a professional banking interface.

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=captainawais.python-development-internship-2026)

---

## 📌 Overview

TechFact Bank ATM System is a desktop banking application designed to replicate the experience of using a real ATM machine.

The system provides secure user authentication, account management, balance inquiry, cash withdrawal, deposits, transfers, mini statements, transaction history, PIN management, and ATM-style user interactions.

---

## 🚀 Features

### 🔐 Authentication & Security

* ATM Card Insert Screen
* Secure 4-Digit PIN Verification
* Login Attempt Protection
* ATM Lock After Multiple Failed Attempts
* User Account Validation

### 💰 Banking Operations

* Balance Inquiry
* Cash Deposit
* Cash Withdrawal
* Fast Cash Options
* Fund Transfer Between Accounts
* Change ATM PIN

### 📄 Transaction Management

* Transaction History
* Mini Statement
* Last Transaction Tracking
* User-Specific History Records

### 🔊 ATM Experience

* ATM Button Sounds
* Login Sound Effects
* Deposit Sound Effects
* Withdrawal Sound Effects
* Transfer Sound Effects
* Card Insert Sound
* Processing / Loading Sound

### 🖥️ User Interface

* Modern Banking Dashboard
* Real-Time Clock
* Professional ATM Theme
* Dynamic Balance Updates
* ATM Workflow Design
* Responsive GUI Layout

---

## 🛠 Technologies Used

* Python 3
* Tkinter
* JSON Database
* Winsound
* Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
smart-atm-system/
│
├── assets/
│   ├── images/
│   └── sounds/
│
├── components/
│   ├── card_screen.py
│   ├── login.py
│   ├── dashboard.py
│   ├── deposit.py
│   ├── withdraw.py
│   ├── transfer.py
│   ├── history.py
│   ├── mini_statement.py
│   ├── change_pin.py
│   ├── loading.py
│   ├── fast_cash.py
│   └── sounds.py
│
├── data/
│   └── users.json
│
├── utils/
│   └── database.py
│
├── atm.py
├── requirements.txt
└── README.md
```

---

## 🔄 ATM Workflow

```text
Start Application
        │
        ▼
Insert ATM Card
        │
        ▼
Card Verification
        │
        ▼
Enter ATM PIN
        │
        ▼
Dashboard
        │
 ┌──────┼─────────┐
 ▼      ▼         ▼
Deposit Withdraw Transfer
 │        │         │
 ▼        ▼         ▼
Update Balance & History
        │
        ▼
Mini Statement / History
        │
        ▼
Exit ATM
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/captainawais/smart-atm-system.git
```

### Move Into Project

```bash
cd smart-atm-system
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python atm.py
```

---

## 🧪 Test Accounts

| Name         | Account No | PIN  |
| ------------ | ---------- | ---- |
| Awais Farooq | TFB1001    | 1234 |
| Ali          | TFB1002    | 5678 |

You can add more users inside:

```text
data/users.json
```

---

## 📈 Future Roadmap

### Version 3.1

* Enhanced ATM UI
* Improved Navigation
* Better Transaction Screens
* Receipt Generation

### Version 4.0

* Real ATM Card Reading System
* Card Image Upload
* Auto User Detection
* QR-Based Banking
* Account Search System
* ATM Receipt Printing
* Admin Panel

---

## 👨‍💻 Developer

**Engr. Awais Farooq**
Software Engineer

GitHub: https://github.com/captainawais

---

## ⭐ Support

If you found this project useful, please consider giving it a star ⭐ on GitHub.

Your support motivates future development and improvements.

---

### TechFact Bank ATM System v3.0

Built with ❤️ using Python & Tkinter.
