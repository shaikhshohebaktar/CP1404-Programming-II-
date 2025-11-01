"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use the Car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "Limo" with 100 units of fuel
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in the limo: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"The limo drove {distance_driven}km.")
    print(limo)


if __name__ == "__main__":
    main()
