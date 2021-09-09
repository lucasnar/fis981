from math import sin, radians

class ProjectileMotion:
    def __init__(self, r, theta):
        self.v = r
        self.theta = theta
        self.g = 10

    def params(self):
        params = {
            "max_height": self.max_height(),
            "horizontal_reach": self.horizontal_reach()
        }
        return params

    def max_height(self):
        max_height = pow(self.v * sin(radians(self.theta)), 2)/(2 * self.g)
        return round(max_height, 2)

    def horizontal_reach(self):
        horizontal_reach = pow(self.v, 2) * sin(radians(self.theta * 2)) / self.g
        return round(horizontal_reach, 2)

# print('Vamos obter alguns parâmetros do lançamento oblíquo!')
# v = float(input('Digite o valor do módulo da velocidade: '))
# theta = float(input('Digite o valor do ângulo do lançamento: '))
#
# params = ProjectileMotion(v, theta).params()
# print(f'A altura máxima do lançamento é: {params["max_height"]}')
# print(f'O alcance máximo do lançamento é: {params["horizontal_reach"]}')
