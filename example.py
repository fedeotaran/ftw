from ftw import Condition, Action, Dispatcher


class HasCreditCardProgram(Condition):

    def execute(self, data):
        return "program" in data \
            and data.get("program") == "credit_card"


class HasCashpayProgram(Condition):

    def execute(self, data):
        return "program" in data \
               and data.get("program") == "cashpay"


class ShouldDiscountBeApplied(Condition):

    def execute(self, data):
        return "amount" in data and data.get('amount') > 1000


class ChargeWithCreditCard(Action):

    def execute(self, amount=None, **data):
        print("Charge %s with credit card" % amount)


class ChargeInCash(Action):

    def execute(self, amount=None, **data):
        print("Charge %s in cash" % amount)


class ChargeWithDiscount(Action):

    def execute(self, amount=None, **data):
        total_amount = self.apply_discount(amount)
        print("Charge %s in cash" % total_amount)

    def apply_discount(self, amount):
        return amount - (amount * 0.2)


class TransactionManager(Dispatcher): pass


if __name__ == '__main__':
    options = [
        {
            "conditions": [HasCreditCardProgram()],
            "method": ChargeWithCreditCard()
        },
        {
            "conditions": [HasCashpayProgram(), ShouldDiscountBeApplied()],
            "method": ChargeWithDiscount()
        }
    ]

    TransactionManager.options_from_dict(options)
    TransactionManager.add_option(**{"conditions": [HasCashpayProgram()], "method": ChargeInCash()})

    credit_cart_transaction = {"id": "1", "program": "credit_card", "amount": 1000}
    cashpay_transaction = {"id": "2", "program": "cashpay", "amount": 1000}
    cashpay_with_discount_transaction = {"id": "3", "program": "cashpay", "amount": 2000}

    TransactionManager.dispatch(credit_cart_transaction),
    TransactionManager.dispatch(cashpay_transaction),
    TransactionManager.dispatch(cashpay_with_discount_transaction),
