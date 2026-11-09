class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1 
        
    
        
my_car = Car("Toyota" , "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata" , "Safari")
print(my_new_car.model)

tesla = Car("Test" , "test")

print(Car.total_car)