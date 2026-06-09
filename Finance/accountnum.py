import random

def numbergeneration():
    number_combo_first = random.randint(111, 999)
    number_combo_second = random.randint(111, 999)
    final = f"300{number_combo_first}600{number_combo_second}"
    finaloutput = int(final)
    return finaloutput

if __name__ == "__main__":
    generated = numbergeneration()
    print("Test generation:", generated)
