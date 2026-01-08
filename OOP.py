class RemoteControl:

    def change_volume(self, volume):
        return f"Setting volume, to {volume}"
    def change_channel(self,channel):
        return f"Change channel, to {channel}"


if __name__ == "__main__":
    remote = RemoteControl()
    print(remote.change_volume(15))


    print(remote.change_channel("SVT"))

    print("-----------------")

class BankAccount:

    def __init__(self,owner, balance=0):
        self.owner=owner
        self._balance =balance

#deposit
    def deposit(self,amount):
        if(amount > 0):
            self._balance += amount
        return f"Deposited €{amount}. New Balance: € {self._balance}"
        return "deposit amount must be positive"

#withdraw
    def withdraw(self,amount):
        if amount > self._balance:
            return "not valid funds"

        self._balance -= amount
        return f"Withdrawed €{amount}. New Balance: € {self._balance}"

    def get_balance(self):
        return f"{self.owner}'s balance: € {self._balance}"



if __name__ == "__main__":
    account = BankAccount("Josef", 100)

print(account.deposit(10))
print(account.withdraw(10))

print("---------------------")

#superclass



class Car:

    def __init__(self, make,model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.make}{self.model}' engine is on"

    def stop_engine(self):
        return f"{self.make}{self.model}' engine has stopped"

    #subclass
class ElectricCar(Car):
    def __init__(self,make,model,year, battery_capacity):
            super().__init__(make, model, year)
            self.battery_capacity = battery_capacity

    def charge(self):
            return (f"Charging {self.make} {self.model} with a "
                    f"{self.battery_capacity} kwh battery")


if __name__ == "__main__":
        my_car = Car("Toyata", "Yaris", 2009 )
        print(my_car.start_engine())
        print(my_car.stop_engine())

        my_tesla = ElectricCar("Tesla", "Y",2024,75)
        print(my_tesla.charge())

        print("-------------")

#polymorphism

class Payment:
    def process_payment (self, amount):
        raise NotImplementedError("Subclass must implament this method.")


class CreditCard (Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of £ {amount}"

class DebitCard (Payment):
    def process_payment(self, amount):
        return f"Processing debit card payment of £ {amount}"

class PayPal (Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of £ {amount}"

def make_payment(payment_method, amount):

        print(payment_method.process_payment(amount))

if __name__ == "__main__":
        #credit = CreditCard()
        #debit = DebitCard()
        #paypal = PayPal()

        #payments = [CreditCard(),DebitCard(),PayPal()]

        #make_payment(credit,10)
        #make_payment(debit, 20)
        #make_payment(paypal, 30)
        #amounts = [10, 20, 30]
        #for method, amount in zip(payments, amounts):
           # make_payment(method,amount)
        for method, amount in [(CreditCard(), 10),(DebitCard(), 20), (PayPal(), 30)]:
            print(method.process_payment(amount))

#1




























