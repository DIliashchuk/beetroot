import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common_factor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_factor
        self.denominator = denominator // common_factor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for +")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for -")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for *")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for /")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for ==")
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for <")
        return self.numerator * other.denominator < other.numerator * self.denominator

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    result = x + y
    print(result)
    print(x == y)
    print(x < y)
