from Library import Library

class SystemAdmin:

    total_transactions = 0

    @classmethod
    def update_transactions_count(cls, amount: int = 1) -> None:
         cls.total_transactions += amount

    @classmethod
    def report_stats(cls) -> None:
        print("Total Transactions : " , cls.total_transactions)
        print("Borrow Days : ", Library.max_borrow_days)