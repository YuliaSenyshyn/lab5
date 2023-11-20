from enum import Enum
class CandyType(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4

class Candy:
    def __init__(self, name, mass, amount, price, candy_type):
        self.name = name
        self.mass = mass
        self.amount = amount
        self.price = price
        self.candy_type = candy_type

    def ate(self):
        if self.mass * self.amount > 2:
            return "You’re on a diet!"
        else:
            return "What delicious candies!"

class Dinner:
    def __init__(self, day, time, candies):
        self.day = day
        self.time = time
        self.candies = candies

    def findTheMostExpensiveCandies(self, name):
        filtered_candies = [candy for candy in self.candies if candy.name == name]
        sorted_candies = sorted(filtered_candies, key=lambda x: x.price, reverse=True)
        return sorted_candies[:3]

if __name__ == "__main__":
    candy1 = Candy("ChocoBar", 100, 2, 3.5, CandyType.BAR)
    candy2 = Candy("PopcornGum", 50, 5, 1.0, CandyType.POPCORN)
    candy3 = Candy("BubbleButtons", 30, 3, 3.0, CandyType.BUTTON)

    candies_for_dinner = [candy1, candy2, candy3]

    dinner = Dinner("Monday", "18:00", candies_for_dinner)

    for candy in dinner.candies:
        print(f"{candy.name}: {candy.ate()}")

    top_candies = dinner.findTheMostExpensiveCandies("ChocoBar")
    print("Top 3 most expensive ChocoBar:")
    for top_candy in top_candies:
        print(f"{top_candy.name}: {top_candy.price} dollars")
