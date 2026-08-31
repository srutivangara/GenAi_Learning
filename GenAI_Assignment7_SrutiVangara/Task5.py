from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"Credit Card Payment of {amount} Successful.")


class UPIPayment(Payment):

    def process_payment(self, amount):
        print(f"UPI Payment of {amount} Successful.")


credit = CreditCardPayment()
upi = UPIPayment()

credit.process_payment(2500)
upi.process_payment(1200)