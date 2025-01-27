def generate_initial_dish_list():
    dishes = [
        {"name": "Pizza", "calories": 800, "ingredients": ["cheese", "tomato", "dough"]},
        {"name": "Salad", "calories": 150, "ingredients": ["lettuce", "tomato", "cucumber"]},
        {"name": "Burger", "calories": 600, "ingredients": ["bun", "beef", "cheese"]}
    ]
    return dishes

if __name__ == "__main__":
    print("Woah there!")
    print("This file shouldn't be ran directly as this is a helper/module for main.py")