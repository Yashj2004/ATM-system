class ATM:
  def __init__(self):
    self.pin=""
    self.balance=0
    self.menu()
  def menu(self):
    user_input=input("""
    hello how can i help you
    press 1 to create pin
    press 2 to change pin
    press 3 to check balance
    press 4 to withdraw cash
    anything else to exit
    """)
    if user_input=='1':
       self.create_pin()
    elif user_input=='2':
        self.change_pin()
    elif user_input=='3':
        self.check_balance()
    elif user_input== '4':
        self.withdraw()
    else:
        pass

  def create_pin(self):
    user_pin=input("enter your pin:\t")
    self.pin=user_pin
    user_balance=int(input("enter the balance:\t"))
    self.balance=user_balance
    print("pin is created succesfully")
    self.menu()

  def change_pin(self):
    old_pin=input("enter your old pin")
    if old_pin==self.pin:
      new_pin=input("enter the new pin")
      self.pin=new_pin
      print("print changed succesfully")
      self.menu()
    else:
      print("wrong pin")
      self.menu()

  def check_balance(self):
    user_pin=input("enter the pin")
    if user_pin==self.pin:
      print("your balance :\t",self.balance)
      self.menu()
    else:
      print("wrong pin")
      self.menu()

  def withdraw(self):
    user_pin=input("enter the pin")
    if user_pin==self.pin:
      amount=int(input("enter the amount:\t"))
      if amount<=self.balance:
        self.balance=self.balance- amount
        print("amount withdraw succesfully")
        print("balance:\t",self.balance)
        self.menu()
      else:
        print("you don't have this much amount")
        self.menu()
    else:
      print("wrong pin")
      self.menu()
