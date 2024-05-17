balance = 0
limit = 500
bank_statement = ""
number_withdrawals = 0
LIMIT_WITHDRAWALS = 3


def deposit(value):
    global balance, bank_statement
    if value > 0:
        balance += value
        bank_statement += f"Deposit : ${value:.2f}\n"
    else:
        print("The value provided is invalid")


def withdraw(value):
    global balance, bank_statement, number_withdrawals
    balance_exceeded = value > balance
    limit_exceeded = value > limit
    withdrawal_exceeded = number_withdrawals >= LIMIT_WITHDRAWALS

    if balance_exceeded:
        print("Operation failed! You do not have enough balance.")

    elif limit_exceeded:
        print("Operation failed! The withdrawal amount exceeds the limit.")

    elif withdrawal_exceeded:
        print("Operation failed! Maximum number of withdrawals exceeded.")

    elif value > 0:
        balance -= value
        bank_statement += f"Withdrawal: ${value:.2f}\n"
        number_withdrawals += 1

    else:
        print("Operation failed! The specified amount is invalid.")


def bankStatement():
    global balance, bank_statement
    print("BANK STATEMENT".center(20, "-"))
    if not bank_statement:
        print("No transactions were made.")
    else:
        print(bank_statement)
    print(f"\nBalance: ${balance:.2f}")


menu = """
[d] Deposit
[w] Withdraw
[b] Bank Statement
[e] Exit

=> """

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Enter a value: "))
        deposit(value)

    elif option == "w":
        value = float(input("Enter a value for the withdrawal: "))
        withdraw(value)

    elif option == "b":
        bankStatement()

    elif option == "e":
        break

    else:
        print("Option Invalid, Please select a valid option.")
