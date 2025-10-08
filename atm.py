class atm():
    def balance(self,initial_value,checkbalance,depositamount,depitamount,exit):
        self.initial_value = 10000
class pin(atm):
    print("welcome to atm")
    pin = 1234
    initial_value = 10000
    pin = int(input("enter the pin:"))
    if pin == 1234:
        print("crt pin")
    else:
        print("wrong pin,enter crt pin")
    choice = ("1.checkbalance, 2.depositamount, 3.debitamount, 4.exit")
    choice = [1,2,3,4]
    choice = int(input("enter the choice:"))
    if choice == 1:
       print("checkbalance")
       print(initial_value)
    elif choice == 2:
        print("depositamount")
        depositamount = int(input("enter the amount to be deposited"))
        initial_value+=depositamount
        print("new balance:",initial_value)
    elif choice == 3:
        print("debitamount")
        print(debitamount = initialvalue-debitamount)
    elif choice == 4:
        print("exit")
    else:
        print("invalid attempts")
