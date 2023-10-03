import unittest
from datetime import datetime, timedelta
from menstrual_app import menstruation_Impl
from menstrual_app.menstruation_Impl import MenstruationRepositoryImpl


class TestMenstruationRepositoryImpl(unittest.TestCase):
    def test_menstrual_period_can_be_checked(self):
        menstruation_repository = MenstruationRepositoryImpl()
        check_date = datetime(2023, 9, 15)
        calculate = menstruation_repository.calculate_period(check_date)
        result = datetime(2023, 9, 29)
        self.assertEqual(result, calculate)

    def test_menstrual_safe_period_starting_can_be_checked(self):
        menstruation_repository = MenstruationRepositoryImpl()
        check_date = datetime(2023, 9, 15)
        calculate = menstruation_repository.find_safe_period_start(check_date)
        result = datetime(2023, 9, 5)
        self.assertEqual(result, calculate)

    def test_menstrual_safe_period_ending_can_be_checked(self):
        menstrual_period = MenstruationRepositoryImpl()
        check_date = datetime(2023, 9, 15)
        calculate = menstrual_period.find_safe_period_end(check_date)
        result = datetime(2023, 9, 25)
        self.assertEqual(result, calculate)

    def test_menstrual_ovulation_can_be_checked(self):
        menstrual_period = MenstruationRepositoryImpl()
        check_date = datetime(2023, 9, 25)
        calculate = menstrual_period.check_ovulation(check_date)
        result = datetime(2023, 10, 5)
        self.assertEqual(result, calculate)

    def test_menstrual_flow_start_can_be_calculated(self):
        menstrual_period = MenstruationRepositoryImpl()
        check_date = datetime(2023, 9, 25)
        calculate = menstrual_period.find_start_flow(check_date)
        result = datetime(2023, 10, 22)
        self.assertEqual(result, calculate)

if __name__ == "__main__":
    unittest.main()
