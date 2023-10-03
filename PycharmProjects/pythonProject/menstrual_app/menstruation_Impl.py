from datetime import datetime, timedelta


class MenstruationRepositoryImpl:
    def __init__(self):
        self.period_start_dates = []

    def find_safe_period_start(self, check_date):
        check_start = check_date - timedelta(days=4)
        return check_start

    def calculate_period(self, check_date):
        check_period = check_date + timedelta(days=14)
        return check_period

    def find_safe_period_end(self, check_date):
        check_end = check_date + timedelta(days=8)
        return check_end

    def check_ovulation(self, cycle_length):
        if cycle_length.total_seconds() < 0:
            raise ValueError("Date does not align")
        else:
            check_ovulation = cycle_length + timedelta(days=14)
            return check_ovulation

    def find_start_flow(self, check_flow):
        check_end = check_flow + timedelta(days=28)
        return check_end

    def find_end_flow(self, check_flow):
        check_end = check_flow + timedelta(days=28)
        return check_end


if __name__ == "__main__":
    # You can create an instance of MenstruationRepositoryImpl and use its methods here
    menstruation_repository = MenstruationRepositoryImpl()
    check_date = datetime.now()  # Replace with your desired date
    safe_period_start = menstruation_repository.find_safe_period_start(check_date)
    safe_period_end = menstruation_repository.find_safe_period_end(check_date)
    print(
        f"Safe period starts on {safe_period_start.strftime('%Y-%m-%d')} and ends on {safe_period_end.strftime('%Y-%m-%d')}")
