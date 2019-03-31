#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-



import car


a1 = car.Car('奥迪', 'A4', 2016)
print(a1.get_descriptive_name())
a1.read_odometer()
a1.odometer_reading = 23
a1.read_odometer()

a2 = car.ElectricCar('tesla', 'model s', 2016)
print(a2.get_descriptive_name())
a2.battery.describe_battery()
a2.battery.get_range()

