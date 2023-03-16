class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance is ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your balance is ${self.balance}")
        else:
            print("Insufficient funds")

    def transfer(self, target, amount):
        if self.balance >= amount:
            self.balance -= amount
            target.balance += amount
            if self.balance < 0:
                target.owed[self.name] = abs(self.balance)
                print(f"Owed ${abs(self.balance)} to {target.name}")
            print(f"Transferred ${amount} to {target.name}")
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"{self.name}: ${self.balance}"


class Bank:
    def __init__(self):
        self.customers = {}
        self.current_customer = None

    def login(self, name):
        if name in self.customers:
            self.current_customer = self.customers[name]
        else:
            self.current_customer = Customer(name)
            self.customers[name] = self.current_customer
        print(f"Hello, {name}!\n{self.current_customer}")

    def logout(self):
        print(f"Goodbye, {self.current_customer.name}!")
        self.current_customer = None

    def deposit(self, amount):
        self.current_customer.deposit(amount)

    def withdraw(self, amount):
        self.current_customer.withdraw(amount)

    def transfer(self, target_name, amount):
        target = self.customers.get(target_name)
        if target is None:
            print(f"No customer with name {target_name}")
            return
        sender = self.current_customer
        sender.transfer(target, amount)
        if sender.balance == 0:
            print(f"Your balance is ${sender.balance}\nOwed ${amount} to {target_name}")
        else:
            print(f"Your balance is ${sender.balance}")

    def __str__(self):
        return "\n".join(str(customer) for customer in self.customers.values())



bank = Bank()

while True:
    command = input("> ").split()
    def process_command(bank, command):
        command = command.split()
    if len(command) == 0:
        print("Error: Empty command")

    if command[0] == "login":
        if len(command) != 2:
            print("Error: login command requires a single argument")
        else:
            bank.login(command[1])

    elif command[0] == "logout":
        bank.logout()

    elif command[0] == "deposit":
        if len(command) != 2:
            print("Error: deposit command requires a single argument")
        else:
            try:
                amount = float(command[1])
                bank.deposit(amount)
            except ValueError:
                print("Error: Invalid amount")

    elif command[0] == "withdraw":
        if len(command) != 2:
            print("Error: withdraw command requires a single argument")
        else:
            try:
                amount = float(command[1])
                bank.withdraw(amount)
            except ValueError:
                print("Error: Invalid amount")

    elif command[0] == "transfer":
        if len(command) != 3:
            print("Error: transfer command requires two arguments")
        else:
            try:
                amount = float(command[2])
                bank.transfer(command[1], amount)
            except ValueError:
                print("Error: Invalid amount or target customer")

    else:
        print("Error: Invalid command")


