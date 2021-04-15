# coding:UTF-8
class Car(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = "{} {} {}".format(self.year,self.model,self.make)
        return long_name.title()

    def read_odometer(self):
        print "这辆车已经跑了{}公里".format(self.odometer_reading)

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print '里程不能减少'

    def increment_odometer(self,miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            raise Exception,"里程不能减少"

class ElectricCar(Car):
    def __init__(self,make,model,year):
        Car.__init__(self,make,model,year)

my_tesla = ElectricCar('tesla','model s','2021')
print my_tesla.get_descriptive_name()