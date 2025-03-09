from pymongo import MongoClient

class DatabaseManager:
    def __init__(self):
        """
        Initialize the database connection and get the dishes collection.
        """
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["restaurant"]
        self.dishes_collection = self.db["dishes"]

    def check_if_dish_exists(self, dish_name):
        """
        Check if a dish with the given name exists in the database.
        :param dish_name:
        :return:
        """
        query = {"name": dish_name.lower()}
        return self.dishes_collection.find_one(query)

    def add_dish(self, dish):
        """
        Add a new dish to the database.
        :param dish:
        :return:
        """
        dish["name"] = dish["name"].lower()
        self.dishes_collection.insert_one(dish)

    def delete_dish(self, dish_name):
        """
        Delete a dish from the database.
        :param dish_name:
        :return:
        """
        query = {"name": dish_name.lower()}
        result = self.dishes_collection.delete_one(query)
        return result.deleted_count

    def update_dish(self, dish_name, update_data):
        """
        Update an existing dish in the database.
        :param dish_name:
        :param update_data:
        :return:
        """
        query = {"name": dish_name.lower()}
        update = {"$set": update_data}
        result = self.dishes_collection.update_one(query, update)
        return result.modified_count

    def search_dishes_by_ingredient(self, ingredient):
        """
        Search dishes by ingredient.
        :param ingredient:
        :return:
        """
        query = {"ingredients": {"$elemMatch": {"$regex": f"^{ingredient}$", "$options": "i"}}}
        return list(self.dishes_collection.find(query))

    def search_dishes_by_calorie(self, calorie, comparison):
        """
        Search dishes by calorie count.
        :param calorie:
        :param comparison:
        :return:
        """
        if comparison == "above":
            query = {"calories": {"$gt": calorie}}
        else:
            query = {"calories": {"$lt": calorie}}
        return list(self.dishes_collection.find(query))

    def list_unique_ingredients(self):
        """
        List unique ingredients in the database.
        :return:
        """
        return self.dishes_collection.distinct("ingredients")