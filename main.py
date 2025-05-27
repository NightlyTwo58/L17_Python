from garden import Garden
from garden import ZeroException

gardentype = input("Square or rectangle garden: ")
if gardentype == "square":
    width = int(input("Enter the side length of your garden: "))
    height = width
else:
    width = int(input("Enter the width of your garden: "))
    height = int(input("Enter the height of your garden: "))

try:
    garden = Garden(width, height)
    while garden.age < 10:
        garden.age_up()
        for i, plant in enumerate(garden.plants):
            print(plant)
        print(str(garden.age) + "th cycle complete!")
except ZeroException:
    print("Please give nonnegative side lengths.")