"""
    HAS-A relationship

    Show Restaurant alongwith its dishes :)
    Refer : https://www.zomato.com/ludhiana/the-table-by-basant-gurdev-nagar/order

    1. Think of an Object
       Restaurant
        name, description, address, operating_hours, ratings, menu

       Menu
        title, num_of_dishes , dishes

       Dish
        name, price, discount, description, ratings

      Restaurant HAS-A Menu | 1 to 1
      Menu HAS Dishes       | 1 to many
"""


class Dish:

    def __init__(self, name=None, price=None,
                 discount=None, description=None, ratings=None):
        self.name = name
        self.price = price
        self.discount = discount
        self.description = description
        self.ratings = ratings

    def show_dish(self):
        print("~~~~~~~~DISH~~~~~~~~~~")
        print("{} | {} | {}".format(self.name, self.price, self.discount))
        print(self.description)
        print(self.ratings)
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print()


class Menu:

    def __init__(self, title=None, num_of_dishes=None, dishes=None):
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show_menu(self):
        print("^^^^^^^^^MENU^^^^^^^^^")
        print("{} | {} ".format(self.title, self.num_of_dishes))

        print()
        # display the dishes
        for dish in self.dishes:
            dish.show_dish()

        print()
        print("^^^^^^^^^^^^^^^^^^^^^^")


class Restaurant:

    def __init__(self, name=None, description=None, address=None,
                 operating_hours=None, ratings=None, menu=None):
        self.name = name
        self.description = description
        self.address = address
        self.operating_hours = operating_hours
        self.ratings = ratings
        self.menu = menu

    def show_restaurant(self):
        print("***********RESTAURANT***********")
        print("{} | {} | {}".format(self.name, self.ratings, self.address))
        print(self.description)
        print(self.operating_hours)

        print()
        # display the menu
        self.menu.show_menu()

        print()
        print("********************************")


def main():

    """
    dish1 = Dish(name="Gajrela", price=300, discount=0.50, description="indian sweet", ratings=4.5)
    dish2 = Dish(name="Noodles", price=200, discount=0.20, description="chinese", ratings=4.3)
    dish3 = Dish(name="Burger", price=100, discount=0.40, description="western", ratings=5.0)
    dish4 = Dish(name="Pizza", price=500, discount=0.10, description="italian", ratings=4.8)
    dish5 = Dish(name="Samosa", price=30, discount=0.0, description="indian snacks", ratings=5.0)

    # List of Dishes (List of Objects)
    dishes = [dish1, dish2, dish3, dish4, dish5]

    menu = Menu(title="Delights", num_of_dishes=len(dishes), dishes=dishes)

    restaurant = Restaurant(name="Table By Basant",
                            description="North India, Italian, Chinese", address="Redwood Shores",
                            operating_hours="11AM to 11PM",
                            ratings=4.8,
                            menu=menu)
    """

    restaurant = Restaurant(
        name="Table By Basant",
        description="North India, Italian, Chinese",
        address="Redwood Shores",
        operating_hours="11AM to 11PM",
        ratings=4.8,
        menu=Menu(
            title="Delights",
            num_of_dishes=5,
            dishes=[
                Dish(name="Gajrela", price=300, discount=0.50, description="indian sweet", ratings=4.5),
                Dish(name="Noodles", price=200, discount=0.20, description="chinese", ratings=4.3),
                Dish(name="Burger", price=100, discount=0.40, description="western", ratings=5.0),
                Dish(name="Pizza", price=500, discount=0.10, description="italian", ratings=4.8),
                Dish(name="Samosa", price=30, discount=0.0, description="indian snacks", ratings=5.0)
            ]
        )

    )

    restaurant.show_restaurant()

if __name__ == '__main__':
    main()

# assignment: Try Representing newsapi.org JSON details as OOPS Has-A Relations
#             Sort the dishes in restaurant as per the filters provided by User
#               i.e. sort by price, sort by ratings (ascending or descending)