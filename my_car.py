from car import Car

my_new_car = Car('audio', 'a4', 2016)
my_new_car.update_odometer(24)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print('\n' + my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()