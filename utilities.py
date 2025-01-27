def search_for_dish(dish_name,dishes):
    for dish in dishes:
        if dish["name"].lower() == dish_name.lower():
            return dish
    return False