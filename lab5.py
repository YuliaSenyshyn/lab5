from enum import Enum
class CandyType(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4

class Candy:
    def __init__(self, name, mass, amount, price, candy_type):
        self.__name = name
        self.__mass = mass
        self.__amount = amount
        self.__price = price
        self.__candy_type = candy_type

    def get_name(self):
        return self.__name

    def get_mass(self):
        return self.__mass

    def get_amount(self):
        return self.__amount

    def get_price(self):
        return self.__price

    def get_candy_type(self):
        return self.__candy_type

    def ate(self):
        return "You’re on a diet!" if self.__mass * self.__amount > 20 else \
            "What delicious candies!"

class Dinner:
    def __init__(self, day, time, candies):
        self.day = day
        self.time = time
        self.candies = candies

    def find_the_most_expensive_candies(self, name):
        filtered_candies = [candy for candy in self.candies if candy.get_name() == name]
        sorted_candies = sorted(filtered_candies, key=lambda x: x.get_price(), reverse=True)
        return sorted_candies[:3]

    def display_candies(self):
        print(f"Dinner on {self.day} at {self.time}:")
        for candy in self.candies:
            candy_info = f"{candy.get_name()} - Type: {candy.get_candy_type()}, Price: ${candy.get_price()}"
            print(candy_info)

if __name__ == "__main__":
    candy1 = Candy("ChocoBar", 100, 2, 3.5, CandyType.BAR)
    candy2 = Candy("ChocoBar", 200, 1, 4.6, CandyType.BAR)
    candy3 = Candy("ChocoBar", 10,  2, 1.4, CandyType.BAR)
    candy4 = Candy("PopcornGum", 50, 5, 1.0, CandyType.POPCORN)
    candy5 = Candy("BubbleButtons", 30, 3, 3.0, CandyType.BUTTON)

    candies_for_dinner = [candy1, candy2, candy3, candy4, candy5]

    dinner = Dinner("Monday", "18:00", candies_for_dinner)

    print("All candies:")
    dinner.display_candies()

    for candy in dinner.find_the_most_expensive_candies("ChocoBar"):
        print(f"{candy.get_name()}: {candy.ate()}, Price: ${candy.get_price()}")
