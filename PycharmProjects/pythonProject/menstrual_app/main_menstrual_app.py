from datetime import datetime, timedelta


class MainMenstrual:
    def __init__(self):
        self.period_start_dates = []

    def main(self):
        start_date = datetime.strptime("2023-09-22", "%Y-%m-%d")
        next_flow_date = start_date + timedelta(days=14)
        print(next_flow_date)
        self.welcome_page()

    def welcome_page(self):
        print("HELLO! WELCOME!!")
        print("You can check your:")
        print("1. Menstrual safe period")
        print("2. Ovulation")
        print("3. Menstrual flow")
        print("4. Circle Length")
        print("5. Exit")

        user_input = input("Enter your choice (1/2/3/4/5): ")

        if user_input == '1':
            self.safe_period()
        elif user_input == '2':
            self.ovulation()
        elif user_input == '3':
            self.menstrual_flow()
        elif user_input == '4':
            self.circle_length()
        elif user_input == '5':
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")
            self.welcome_page()

    def menstrual_flow(self):
        input_date = None

        while input_date is None:
            user_input = input("Enter the last day of your flow (yyyy-MM-dd): ")

            try:
                input_date = datetime.strptime(user_input, "%Y-%m-%d")
                next_flow_date = input_date + timedelta(days=28)  # Assuming a 28-day menstrual cycle
                print(f"Hi dear, you can expect your next flow on {next_flow_date.strftime('%Y-%m-%d')}")
                self.welcome_page()
            except ValueError:
                print("Invalid date format. Please use yyyy-MM-dd.")

    def ovulation(self):
        ovulation = None

        while ovulation is None:
            user_input = input("Enter the last day of your period (yyyy-MM-dd): ")

            try:
                last_period_date = datetime.strptime(user_input, "%Y-%m-%d")
                ovulation_date = last_period_date + timedelta(days=14)  # Assuming a 28-day menstrual cycle
                print(f"Hi dear, your ovulation starts on: {ovulation_date.strftime('%Y-%m-%d')}")
                self.welcome_page()
            except ValueError:
                print("Invalid date format. Please use yyyy-MM-dd.")

    def safe_period(self):
        start_period = None
        end_period = None

        while start_period is None or end_period is None:
            user_input = input("Enter the last day of your period (yyyy-MM-dd): ")

            try:
                last_period_date = datetime.strptime(user_input, "%Y-%m-%d")
                start_period = last_period_date + timedelta(days=1)
                end_period = last_period_date + timedelta(days=7)  # Assuming a 28-day menstrual cycle
                print(
                    f"Hi dear, your safe period starts on: {start_period.strftime('%Y-%m-%d')} and ends on {end_period.strftime('%Y-%m-%d')}")
                self.welcome_page()
            except ValueError:
                print("Invalid date format. Please use yyyy-MM-dd.")

    def circle_length(self):
        print("Function for circle length calculation is not implemented yet.")


if __name__ == "__main__":
    main_menstrual = MainMenstrual()
    main_menstrual.main()
