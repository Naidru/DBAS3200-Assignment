from DatabaseManager import DatabaseManager

database = DatabaseManager()

def add_new_dish():
    """
    Adds a new dish to the database.
    Input a unique name, calorie count and list of ingredients.
    :return:
    """
    dish_name = input("Enter dish name (or type 'back' to return): ").strip()
    if dish_name.lower() == "back" or dish_name == "":
        return
    if database.check_if_dish_exists(dish_name):
        print("This dish already exists!")
        return
    try:
        calorie_count = int(input("Enter calorie count: "))
        if calorie_count < 0:
            print("Calories count cannot be negative.")
            return
    except ValueError:
        print("Invalid calorie input.")
        return
    ingredients_input = input("Enter ingredients (separated by commas): ").strip()
    if ingredients_input == "":
        print("Ingredient list cannot be empty.")
        return
    ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(",") if ingredient.strip() != ""]
    dish = {"name": dish_name, "calories": calorie_count, "ingredients": ingredients}
    database.add_dish(dish)
    print("Dish added successfully!")

def update_dish():
    """
    Update a already existing dish in the database.
    :return:
    """
    dish_name = input("Enter the dish name you wish to update (or type 'back' to return): ").strip()
    if dish_name.lower() == "back" or dish_name == "":
        return
    existing = database.check_if_dish_exists(dish_name)
    if not existing:
        print("Dish does not exist!")
        return
    print("What do you want to update?")
    print("1 - Update calorie count")
    print("2 - Update ingredients list")
    choice = input("Select an option: ").strip()
    if choice == "1":
        try:
            calorie_count = int(input("Enter new calorie count: "))
            if calorie_count < 0:
                print("Calories count cannot be negative.")
                return
        except ValueError:
            print("Invalid calorie input.")
            return
        modified = database.update_dish(dish_name, {"calories": calorie_count})
        if modified:
            print("Calories updated successfully!")
        else:
            print("No changes made.")
    elif choice == "2":
        ingredients_input = input("Enter new ingredients (separated by commas): ").strip()
        if ingredients_input == "":
            print("Ingredient list cannot be empty.")
            return
        ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(",") if ingredient.strip() != ""]
        modified = database.update_dish(dish_name, {"ingredients": ingredients})
        if modified:
            print("Ingredients updated successfully!")
        else:
            print("No changes made.")
    else:
        print("Invalid option.")

def delete_dish():
    """
    Delete a dish from the database.
    :return:
    """
    dish_name = input("Enter the dish name you wish to delete (or type 'back' to return): ").strip()
    if dish_name.lower() == "back" or dish_name == "":
        return
    deleted_count = database.delete_dish(dish_name)
    if deleted_count > 0:
        print("Dish removed successfully!")
    else:
        print("Dish not found.")

def search_dishes_by_ingredient():
    """
    Input an ingredient to search for the dish(es) containing it.
    :return:
    """
    ingredient = input("Enter an ingredient to search: ").strip().lower()
    if ingredient == "":
        print("Ingredient cannot be empty.")
        return
    dishes = database.search_dishes_by_ingredient(ingredient)
    if dishes:
        print("Dishes containing", ingredient, ":")
        for dish in dishes:
            print(f"Name: {dish.get('name')}, Calories: {dish.get('calories')}, Ingredients: {dish.get('ingredients')}")
    else:
        print("No matching dishes found.")

def search_dishes_by_calorie():
    """
    Input a calorie threshold and a condition to search for dishes above or below the threshold.
    :return:
    """
    try:
        calorie = int(input("Enter a calorie threshold: "))
    except ValueError:
        print("Invalid input.")
        return
    condition = input("Type 'above' to search for dishes above the threshold, or 'below' for dishes below: ").strip().lower()
    if condition not in ("above", "below"):
        print("Invalid condition.")
        return
    dishes = database.search_dishes_by_calorie(calorie, condition)
    if dishes:
        print("Dishes matching the criteria:")
        for dish in dishes:
            print(f"Name: {dish.get('name')}, Calories: {dish.get('calories')}, Ingredients: {dish.get('ingredients')}")
    else:
        print("No matching dishes found.")

def show_unique_ingredients():
    """
    Show all unique ingredients in the database.
    :return:
    """
    ingredients = database.list_unique_ingredients()
    if ingredients:
        print("Unique ingredients in the restaurant:")
        for ingredient in ingredients:
            print(ingredient)
    else:
        print("No ingredients found.")

def main():
    """
    Main menu for the program.
    :return:
    """
    while True:
        print("\nRestaurant Management Program")
        print("1 - Add New Dish")
        print("2 - Update Dish")
        print("3 - Delete Dish")
        print("4 - Search Dishes by Ingredient")
        print("5 - Search Dishes by Calorie Threshold")
        print("6 - Show All Unique Ingredients")
        print("7 - Exit")
        selection = input("Select an option: ").strip()
        if selection == "1":
            add_new_dish()
        elif selection == "2":
            update_dish()
        elif selection == "3":
            delete_dish()
        elif selection == "4":
            search_dishes_by_ingredient()
        elif selection == "5":
            search_dishes_by_calorie()
        elif selection == "6":
            show_unique_ingredients()
        elif selection == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid menu selection.")

if __name__ == "__main__":
    main()