import dish_list_get_functions as get
import dish_list_modify_functions as modify
import dish_list

dishes = dish_list.generate_initial_dish_list()

def main():
    while True:
        print()
        print()
        print("Restaurant Backend Manager")
        print("Please select an option")
        print("1 - View All Dish Names")
        print("2 - View Dish Details by Name")
        print("3 - Filter Dishes by Calorie Count")
        print("4 - Add a New Dish")
        print("5 - Remove a Dish by Name")
        print("6 - Modify a Dish by Name")
        print("7 - Search Dishes by Ingredient")
        print("8 - Save and Exit")
        print("9 - Exit without Saving")
        menu_selection = input("Select an option: ")
        if menu_selection == "1":
            get.all_dish_names(dishes)
        elif menu_selection == "2":
            get.dish_details_by_name(dishes)
        elif menu_selection == "3":
            get.filter_dish_details_by_calorie_count(dishes)
        elif menu_selection == "4":
            modify.add_new_dish(dishes)
        elif menu_selection == "5":
            modify.remove_existing_dish(dishes)
        elif menu_selection == "6":
            modify.modify_existing_dish(dishes)
        elif menu_selection == "7":
            get.search_dish_by_ingredient(dishes)
        elif menu_selection == "8":
            dish_list.save_dish_list(dishes)
            exit()
        elif menu_selection == "9":
            print("Are you sure you want to exit without saving? (y/n)")
            confirm_selection = input().lower().strip()
            if confirm_selection == "y":
                exit()



if __name__ == "__main__":
    main()