import json

def generate_initial_dish_list():
    try:
        # Open the file using the `with` statement
        # The `open()` function is called with mode 'r' (read mode).
        with open("dish_list", "r") as file:
            # At this point, the file is open and can be read.
            # When the `with` block ends, the file is automatically closed.
            file_contents = file.read()
        list_of_dishes = json.loads(file_contents)
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