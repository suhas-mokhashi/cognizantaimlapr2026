"""aplication entry point"""

import random


def generate_otp():
    """this function will generate otp"""

    otp = random.randint(100000, 999999)
    print(f"Your OTP is: {otp}")


if __name__ == "__main__":
    otp = generate_otp()
    print(otp)
