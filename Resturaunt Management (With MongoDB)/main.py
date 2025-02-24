from pymongo import MongoClient

class DatabaseManager:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["restaurant"]
    dishes_collection = db["dishes"]
    ingredients_collection = db["ingredients"]

    def check_if_item_exist(self, query):
        query = {"name": query.lower()}
        documents = list(self.dishes_collection.find(query))
        if len(documents) == 0:
            return False
        else:
            return True


def add_new_dish():
    dish_name = input("Please input a dish name or type 'back' to go back: ")
    if dish_name.lower().strip() == "back":
        return()
    if database.check_if_item_exist(dish_name):
        print("This dish already exists.")
        print()
        return
    while True:
        try:
            calorie_count = int(input("Enter calories count: "))
            if calorie_count < 0:
                print("Calories count cannot be negative.")
                return
            else:
                break
        except ValueError:
            print("Invalid input.")


global database
database = DatabaseManager()

def main():
    while True:
        print("Restaurant Management Program")
        print("1 - Create new Dish")
        print("2 - Update Dish")
        print("3 - Delete Dish")
        print("4 - Search Dish by Ingredient")
        print("5 - Search dish by calorie threshold")
        print("6 - Show all unique ingredients")
        print("7 - Exit")
        menu_select = input().lower().strip()
        if menu_select == "1":
            add_new_dish()
        elif menu_select == "2":
            print()
        elif menu_select == "3":
            print()
        elif menu_select == "4":
            print()
        elif menu_select == "5":
            print()
        elif menu_select == "6":
            print()
        elif menu_select == "7":
            break
        else:
            print("Invalid menu selection")
            print()

if __name__ == "__main__":
    main()


