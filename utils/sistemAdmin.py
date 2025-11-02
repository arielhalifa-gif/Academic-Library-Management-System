class SystemAdmin:
    total_transactions = 0
    @classmethod
    def update_transactions_count(cls, amount: int = 1) -> None:
        cls.total_transactions += amount

    @classmethod
    def report_stats(cls):
        from modules.library import Library
        print("total transactions: ", cls.total_transactions)
        print("max borrow days: ", Library.max_borrow_days)