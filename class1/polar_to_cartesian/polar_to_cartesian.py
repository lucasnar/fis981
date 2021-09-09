from math import cos, sin, radians

class PolarConverter:
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

    def convert(self):
        x = self.r * cos(radians(self.theta))
        y = self.r * sin(radians(self.theta))
        return (round(x, 10), round(y, 10))

# print('Vamos converter coordenadas polares para coordenadas cartesianas!')
# r = float(input('Digite o valor de r: '))
# theta = float(input('Digite o valor de theta: '))

# cartesian_coor = PolarConverter(r, theta).convert()
# print(f'A respectiva coordenada cartesiana é: {cartesian_coor}')
