#A program with different operations for the bank.
from random import randint
class BankAccount:
    def __init__(self, account_name):
        self.account_name=account_name
        self.account_number=randint(1000000, 10000000000)
        self.balance=0
        self.is_open = True
    def get_balance(self):
        if self.is_open==True :
             print("\t\tYour balance is  ***"+ str(self.balance) +"***")
             self.home()
        else:
            print("account is closed")
#This method enables user open an account by turning the is_open attribute to true on object instantiation.
    def open(self):
        self.is_open = True
#this is the deposite method.
    def deposit(self, amount):
        if self.is_open==True :
            amount =input("Please enter amount to deposit")
            depositi = int(amount)
            self.balance+=depositi
            print("\t\tYou have deposited  "+str(depositi)+ "  and your balance is  "+ str(self.balance))
            self.home()
        else:
            print("Account closed cant do any operation")
#This method only allows user to withdraw money if user has sufficient money on their account, and account status is open.
    def withdraw(self, amount):
        if self.is_open==True :
           amount=input("Please enter amount to withdraw:")
           withdrawal=int(amount)
           if self.balance>=withdrawal:
               self.balance-=withdrawal
               print("\t\tHey "+ self.account_name.title()+ "! thanks for banking with us.")
               print("\t\tYou have withdrawn shillings "+ str(withdrawal) + "! thanks for banking with us.")
               self.home()
           else:
                print("\t\tYou have insufficient amount "+ str(self.balance)+". The amount should be greater than withdraw.")
                self.home()
        else:
            print("account closed")
    def close(self):
        self.is_open = False   
        print("\t\tyour account has been closed")
#This methods displays the main menu that the user uses to interact with.
    def home(self):
        print("**Welcome to success Bank**")
        print("Hi "+ self.account_name.title())
        print("Your account number is  "+ str(self.account_number))
        print("Please choose a service of your choice.")
        print("1 Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. close account")
        inputt = input("Enter option:")
        innput2 = int(inputt)
        if innput2 == 1:
            self.deposit(4000)
        elif innput2 ==2:
            self.withdraw(100000)
        elif innput2 == 3:
            self.get_balance()
        elif innput2 == 4:
            self.close()
            self.home()
        else:
            print("invalid input")
#instantiating a classs
my_account = BankAccount("NAKAWEESI")
#calling a class method using an object
my_account.home()