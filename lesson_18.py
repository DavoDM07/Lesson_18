#Create a class called BankAccount to represent a basic bank account. The class should
#have the following attributes:
#   1. owner: The name of the account owner.
#   2. balance: The current balance of the account.
#Implement the following methods:
#   1. __init__(self, owner, balance): Initializes the BankAccount object with the
#   owner's name and initial balance. Ensure that the balance is a non-negative integer
#   2. get_balance(self): Returns the current balance of the account.
#   3. deposit(self, amount): Adds the specied amount to the account balance.
#   Ensure that the amount is a positive integer.
#   4. withdraw(self, amount): Subtracts the specied amount from the account
#   balance. Ensure that the amount is a positive integer and does not exceed the
#   current balance.
#Additionally, use @property and @attribute.setter to encapsulate the balance
#attribute and enforce validation rules.


class BankAccount:
    def __init__(self,owner,balance):
        self.__owner = owner
        self.__balance = balance
        if self.__balance < 0:
            raise Exception('the balance should not be negative')
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self,owner):
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,balance):
        if balance < 0:
            raise Exception('the balance should not be negative')
        else:
            self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise Exception('the deposit must be an integer')
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            raise Exception('the withdraw must be an integer')
        self.__balance -= amount

user1 = BankAccount('John', 10000)
user1.withdraw(1000)
user1.deposit(10000)
user1.owner = 'Davit'
print(user1.owner)
print(user1.balance)



















