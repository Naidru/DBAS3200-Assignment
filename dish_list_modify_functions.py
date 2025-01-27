import errors as err
import utilities as util
import dish_individual_modification as ind

def add_new_dish(dishes):
    dish_name = input("Enter dish name: ")
    dish = util.search_for_dish(dish_name, dishes)
    if dish is not False:
            print("Dish name already exists.")
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
    ingredients = input("Enter ingredients (Seperated by commas): ").lower().split(",")
    dishes.append({"name": dish_name, "calories": calorie_count, "ingredients": ingredients})
    print(f"Dish {dish_name} added.")
    return dishes

def remove_existing_dish(dishes):
    dish_name = input("Enter the name of the dish to remove: ")
    dish = util.search_for_dish(dish_name, dishes)
    if dish is not False:
        dishes.remove(dish)
        print(f"Dish {dish_name} removed.")
        return
    else:
        err.error_handling(404,dish_name)

def modify_existing_dish(dishes):
    dish_name = input("Enter the name of the dish to modify: ")
    dish = util.search_for_dish(dish_name, dishes)
    if dish is False:
        err.error_handling(404,dish_name)
        return
    print(f"Modifying {dish_name} dish.")
    print("1 - Change dish name.")
    print("2 - Update calorie count.")
    print("3 - Add ingredients.")
    print("4 - Remove ingredients.")
    print("5 - Return")
    modify_menu_selection = input("Select an option: ")
    if modify_menu_selection == "1":
        ind.change_existing_dish_name(dishes, dish_name)
    elif modify_menu_selection == "2":
        ind.update_dish_calorie_count(dishes, dish_name)
    elif modify_menu_selection == "3":
        ind.add_ingredients_to_dish(dishes, dish_name)
    elif modify_menu_selection == "4":
        ind.remove_ingredients_from_dish(dishes, dish_name)
    elif modify_menu_selection == "5":
        return