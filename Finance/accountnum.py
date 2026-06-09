import random

class AccountGenerator:
    @staticmethod
    def generate_number():
        number_combo_first = random.randint(111, 999)
        number_combo_second = random.randint(111, 999)
        final = f"300{number_combo_first}600{number_combo_second}"
        return int(final)


if __name__ == "__main__":
    test_number = AccountGenerator.generate_number()
    print(f"Test generation: {test_number}")
