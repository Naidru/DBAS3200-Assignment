import errors as err
import utilities as util

def change_existing_dish_name(dishes, dish_name):
    new_name = input("Enter new dish name: ")
    dish = util.search_for_dish(dish_name, dishes)
    if dish is not False:
        dish["name"] = new_name
        print(f"Dish {dish_name} updated to {new_name}.")
        return
    err.error_handling(1,f"Tried searching for {dish_name} but could not find it?")

def update_dish_calorie_count(dishes, dish_name):
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
    dish = util.search_for_dish(dish_name, dishes)
    if dish is not False:
        old_calories = dish["calories"]
        dish["calories"] = calorie_count
        print(f"Dish {dish_name} calories updated from {old_calories} to {calorie_count}.")
        return
    err.error_handling(1,f"Tried searching for {dish_name} but could not find it?")

def add_ingredients_to_dish(dishes, dish_name):
    ingredients = input("Enter ingredients (Seperated by commas): ").lower().split(",")
    dish = util.search_for_dish(dish_name, dishes)
    if dish is not False:
        old_ingredients = dish["ingredients"]
        new_ingredients = ingredients + old_ingredients
        dish["ingredients"] = new_ingredients
        print(f"Added ingredients: {dish['ingredients']}.")
        return
    err.error_handling(1,f"Tried searching for {dish_name} but could not find it?")

def remove_ingredients_from_dish(dishes, dish_name):
    ingredients = input("Enter ingredients to remove (Seperated by commas): ").lower().split(",")
    dish = util.search_for_dish(dish_name, dishes)
    if dish is not False:
        ingredient_list = dish["ingredients"]
        for ingredient in ingredients:
            try:
                ingredient_list.remove(ingredient)
            except ValueError:
                print(f"Ingredient {ingredient} is not in this dish.")
        dish["ingredients"] = ingredient_list
        print(f"Removed ingredients.")
        return
    err.error_handling(1,f"Tried searching for {dish_name} but could not find it?")