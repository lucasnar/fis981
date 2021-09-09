class ParityChecker:
    def __init__(self, number):
        self.number = number

    def check(self):
        print(f'O número {self.number} é {self.parity_name()}')

    def is_even(self):
        return self.number % 2 == 0

    def parity_name(self):
        return 'par' if self.is_even() else 'ímpar'

# number = int(input('Digite um número para saber se é par ou ímpar: '))
# ParityChecker(number).check()

# Um programa mais simples seria
# number = int(input('Digite um número para saber se é par ou ímpar: '))
# print(f'O número {number} é {'par' if number % 2 == 0 else 'ímpar'}')
