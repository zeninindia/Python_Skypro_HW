from calculator import Calculator

calculator = Calculator()

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-9, -5)
assert res == -14

res = calculator.sum(-4, 5)
assert res == 1

res = calculator.sum(4.5, 5.5)
assert res == 10

