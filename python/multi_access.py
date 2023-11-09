R"""
A few tests to see how inheritance/composition/duck-typing/... work together.

For instance, image we have a class named Car that does not have the color property.
If we define a function paint_object that was supposed to paint houses, boats, (other objects but cars) and yet decide to use it to paint a car, we will end up with a car with a color property.
Now let's imagine that this car object was also being accessed by different objects (that need to read or write its properties). Will they too have access to the new color property?
"""


class CarWithoutColor:
    def __init__(self, model: str):
        self.model = model

    def change_model(self, new_model: str):
        self.model = new_model

    def __repr__(self):
        return self.model


def paint_object(target, color):
    target.color = color


car = CarWithoutColor('simple car')
ford = car
if(hasattr(CarWithoutColor, 'color')):
    print('Before painting the ford, CarWithoutColor has attribute color')
else:
    print('Before painting the ford, CarWithoutColor has no attribute color')

paint_object(car, 'blue')
print(ford.color)
print(car.color)

if(hasattr(CarWithoutColor, 'color')):
    print('After painting the ford, CarWithoutColor has attribute color')
else:
    print('After painting the ford, CarWithoutColor still has no attribute color')



R"""
By running the code, we can see that although the objects have a color attribute, the class does not. 
We can create new objects to verify that.
"""

new_car = CarWithoutColor('Any car')

print(new_car.color)