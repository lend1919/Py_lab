from math import gcd

class Func:
    def __init__(self, numer, denum):
        if denum == 0:
            raise ValueError("Denumy 0 chi kara lini")
        common = gcd(numer, denum)
        self.numer = numer // common
        self.denum = denum // common

    def __str__(self):
        return f"{self.numer}/{self.denum}"

    def __add__(self, other):
        new_numer= self.numer * other.denum + other.numer * self.denum
        new_denum = self.denum * other.denum
        return Func(new_numer, new_denum)

    def __sub__(self, other):
        new_numer = self.numer * other.denum - other.numer * self.denum
        new_denum = self.denum * other.denum
        return Func(new_numer, new_denum)

    def __mul__(self, other):
        new_numer= self.numer * other.numer
        new_denum = self.denum * other.denum
        return Func(new_numer, new_denum)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ValueError("Cannot divide by zero")
        new_numer = self.numer * other.denum
        new_denum = self.denum * other.numer
        return Func(new_numer, new_denum)

# Example usage
func1 = Func(1, 2)
func2 = Func(3, 4)

add = func1 + func2
sub = func1 - func2
mul = func1 * func2
div = func1 / func2

print(f"Add: {func1} + {func2} = {add}")
print(f"Sub {func1} - {func2} = {sub}")
print(f"Mul: {func1} * {func2} = {mul}")
print(f"Div: {func1} / {func2} = {div}")