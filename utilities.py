def search_for_dish(dish_name,dishes):
    for dish in dishes:
        if dish["name"].lower() == dish_name.lower():
            return dish
    return False

if __name__ == "__main__":
    print("Woah there!")
    print("This file shouldn't be ran directly as this is a helper/module for main.py")