# UserDefined Exception
class BankingException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class BankAccount:

    def __init__(self):
        self.balance = 10000
        self.min_balance = 2000
        self.attempts = 0

    def withdraw(self, amount):
        self.balance -= amount

        if self.balance <= self.min_balance:
            self.balance += amount
            print("withdraw failed as balance is low:", self.balance)
            self.attempts += 1
        else:
            print("withdraw success and new balance is:", self.balance)

        if self.attempts == 3:
            error = BankingException("Illegal Access to Transaction")
            raise error


def main():
    print("Banking Started")

    account = BankAccount()

    for i in range(500):
        account.withdraw(3000)

    print("Banking Finished")


if __name__ == '__main__':
    main()