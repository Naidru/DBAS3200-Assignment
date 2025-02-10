import errors as err


def all_dish_names(dishes):
    for dish in dishes:
        print(dish["name"])

def search_for_dish(dish_name,dishes):
    for dish in dishes:
        if dish["name"].lower() == dish_name.lower():
            return dish
    return False

def dish_details_by_name(dishes):
    dish_name = input("Enter dish name: ").lower()
    dish = search_for_dish(dish_name,dishes)
    if dish is not False:
        print(f"Name: {dish['name']}")
        print(f"Calories: {dish['calories']}")
        print(f"Ingredients:")
        for ingredient in dish["ingredients"]:
            print(f"- {ingredient}")
    else:
        err.error_handling(404,dish_name)

def filter_dish_details_by_calorie_count(dishes):
    while True:
        try:
            min_calorie = int(input("Enter min calorie: "))
            max_calorie = int(input("Enter max calorie: "))
            if min_calorie > max_calorie:
                print("Maximum calories cannot be greater than minimum calories.")
                continue
            else:
                print(f"Minimum Calorie {min_calorie}")
                print(f"Maximum Calorie {max_calorie}")
                break
        except ValueError:
            print("Invalid input.")
    for dish in dishes:
        if min_calorie < dish["calories"] < max_calorie:
            print(f"Name: {dish['name']}")
            print(f"Calories: {dish['calories']}")
            print(f"Ingredients:")
            for ingredient in dish["ingredients"]:
                print(f"- {ingredient}")
            print("----")

def search_dish_by_ingredient(dishes):
    ingredient_to_search = input("Enter the ingredient you want to search by: ").lower().strip()
    if ingredient_to_search == "":
        return
    for dish in dishes:
        for ingredient in dish["ingredients"]:
            if ingredient == ingredient_to_search:
                print(f"{dish['name']}")