import json

def generate_initial_dish_list():
    try:
        # Open the file using the `with` statement
        # The `open()` function is called with mode 'r' (read mode).
        with open("dish_list", "r") as file:
            # At this point, the file is open and can be read.
            # When the `with` block ends, the file is automatically closed.
            file_contents = file.read()
        try:
            list_of_dishes = json.loads(file_contents)
        except json.JSONDecodeError as e:
            print(f"Error: A JSON error occured: {e}")
            print("Do you want to regenerate the dish list? (y/n)")
            while True:
                regenerate_selection = input().lower().strip()
                if regenerate_selection == "y":
                    list_of_dishes = []
                    break
                elif regenerate_selection == "n":
                    exit()
                print("Invalid selection!")

        return list_of_dishes

            # No need to manually close the file here — `with` takes care of it!
    except FileNotFoundError:
        # This block is executed if the file does not exist
        print("Error: The file 'dish_list' does not exist. Creating a new one.")
        try:
            # Open the file in write mode
            with open("dish_list", "w") as file:
                # Writing content to the file
                file.write("[]")  # Writes a single line to the file
                print("Created dish_list data file successfully.")
                return  []

            # After the `with` block, the file is automatically closed.
        except IOError as e:
            # Handles any I/O-related errors (e.g., disk issues or permissions errors)
            print(f"Error: An I/O error occurred: {e}")
            exit()
    except IOError as e:
        # This block handles other input/output errors, such as permissions issues
        print(f"Error: An I/O error occurred: {e}")
        exit()

def save_dish_list(dishes):
    try:
        # Open the file in write mode
        with open("dish_list", "w") as file:
            # Writing content to the file
            file.write(str(dishes))
            print("Data successfully saved.")

        # After the `with` block, the file is automatically closed.
    except IOError as e:
        # Handles any I/O-related errors (e.g., disk issues or permissions errors)
        print(f"Error: An I/O error occurred: {e}")
        exit()
