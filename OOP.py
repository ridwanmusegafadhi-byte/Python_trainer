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

#withdraw
    def withdraw(self,amount):
        if amount > 0:
            #return "not valid funds"
            self._balance -= amount
        return f"Withdrawed €{amount}. New Balance: € {self._balance}"



if __name__ == "__main__":
    account = BankAccount("Josef", 100)

#print(account.deposit(10))
print(account.withdraw(20))













