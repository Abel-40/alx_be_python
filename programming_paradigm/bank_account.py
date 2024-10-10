class BankAccount:

  def __init__(self,inital_balance = 0):
    self.__account_balance = inital_balance

  def deposit(self,amount):
   if self.__account_balance > 0:
    self.__account_balance += amount
    return self.__account_balance
   else:
    return print("please enter non negative number")
  
  def withdraw(self, amount):
    if amount > self.__account_balance:
        print("Insufficient funds.")
        return False
    self.__account_balance -= amount
    return True


  def display_balance(self):
    print(f"Current Balance:{self.__account_balance:.2f}")