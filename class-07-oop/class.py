# OOP

class Car:
    def __init__(self, brand, model, year, fipe, offer):
        self.brand = brand
        self.model = model
        self.year = year
        self.fipe = fipe 
        self.offer = offer
      

    def info(self):
        return (self.brand, self.model, self.year, )
    
    def sale(self):
        if self.offer >= self.fipe:
            return "Carro vendido!"
        else:
            return "Sai pra lá caloteiro"
        
MyCar1 = Car("Toyota", "SW4", "2024", "345000", "350000")
MyCar2 = Car("Chevrolet", "Celta", "2006", "16500", "17000")

print(MyCar1.brand)
print(MyCar1.model)
print(MyCar1.year)

print(MyCar2.brand)
print(MyCar2.info())
print(MyCar2.sale())



