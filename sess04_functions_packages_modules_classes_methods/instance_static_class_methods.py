# Python script to demonstrate the use of instance, static and class methods
# in a real-world scenario

# Import the regular expressions module
import re

class BankAccount:
    """Represents a simple bank account."""

    # Class attribute (shared across all instances)
    interest_rate = 0.05  # 5% annual interest rate

    # Constructor
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    # ---------------------------------------------------------
    # Instance Methods
    # ---------------------------------------------------------
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"[{self.account_holder}] deposited Kes. {amount:.2f}."
                f"\nNew balance is : Kes. {self.balance:.2f}")
        else:
            print("Kindly note that the deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print("Invalid withdrawal: insufficient funds!")
        else:
            self.balance -= amount
            print(f"[{self.account_holder}] withdrew Kes. {amount:.2f}."
                f"\nNew balance is : Kes. {self.balance:.2f}")

    # -------------------------------------------------------
    # Class Methods
    # -------------------------------------------------------
    @classmethod
    def set_interest_rate(cls, new_rate):
        """Set a new annual interest rate for all accounts."""
        if 0 <= new_rate <= 0.2:
            cls.interest_rate = new_rate
            print(f"The annual interest rate has been set to "
                f"{new_rate * 100:.2f}% for all accounts!")
        else:
            print("The annual interest rate must be between 0% and 20%.")

    # ----------------------------------------------------------
    # Static Methods
    # ----------------------------------------------------------
    @staticmethod
    def validate_account_number(account_number):
        """
        Validate an account number.
        Format: ACC followed by exactly 6 digits.
        """
        pattern = r"ACC\d{6}"
        return bool(re.fullmatch(pattern, account_number))


# -----------------------------------------------------------------------------
# Demonstrate the BankAccount class and its instance, class and static methods
# -----------------------------------------------------------------------------

# Create two bank account objects
abigail_acc = BankAccount("ABIGAIL", 55000.00)
brian_acc = BankAccount("BRIAN", 15000.00)

# Deposit and withdraw money
abigail_acc.deposit(1500)
brian_acc.withdraw(700)

# Update the annual interest rate from 5% to 8% (class method)
BankAccount.set_interest_rate(0.08)

# Validate account numbers (static method)
print("\nValidating new account numbers...")
print("ACC123754 is valid? ", BankAccount.validate_account_number("ACC123754"))
print("Account123457 is valid? ", BankAccount.validate_account_number("Account123457"))
