class Car:
    """   
        This is a Car class
    """ # This is a Docstring
    def __init__(self, name, color):
        self.name = name
        self.color = color   


    def accel(self):
        print(f'{self.name} accelerate at 1000mpn while the cal color is {self.color}')
   
car_1 = Car('Mercedes', 'silver')
car_2 = Car('BMA', 'Blue')
# car_1.name = 'Mercedes'
# CAR_2.name = 'Benz'
# print(car_1.name)
# print(CAR_2.name)
# car_1.accel()
# car_2.accel()
# print(car_1.name,car_2.name)
# print(car_1.color)
print(help(Car))