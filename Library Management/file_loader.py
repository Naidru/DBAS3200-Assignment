import json
import main
data = "libraries"


def get_data():
    try:
        # Open the file using the `with` statement
        # The `open()` function is called with mode 'r' (read mode).
        with open(data, "r") as file:
            # At this point, the file is open and can be read.
            # When the `with` block ends, the file is automatically closed.
            file_contents = file.read()
        try:
            data_list = json.loads(file_contents)
        except json.JSONDecodeError as e:
            print(f"Error: A JSON error occurred: {e}")
            print("Do you want to regenerate the data file? (y/n)")
            while True:
                regenerate_selection = input().lower().strip()
                if regenerate_selection == "y":
                    data_list = []
                    break
                elif regenerate_selection == "n":
                    exit()
                print("Invalid selection!")

        return data_list

        # No need to manually close the file here — `with` takes care of it!
    except FileNotFoundError:
        # This block is executed if the file does not exist
        print(f"Error: The file {data} does not exist. Creating a new one.")
        try:
            # Open the file in write mode
            with open(data, "w") as file:
                # Writing content to the file
                file.write("[]")  # Writes a single line to the file
                print("Created data file successfully.")
                return []

            # After the `with` block, the file is automatically closed.
        except IOError as e:
            # Handles any I/O-related errors (e.g., disk issues or permissions errors)
            print(f"Error: An I/O error occurred: {e}")
            exit()
    except IOError as e:
        # This block handles other input/output errors, such as permissions issues
        print(f"Error: An I/O error occurred: {e}")
        exit()


def save_data(data_to_save):
    try:
        # Open the file in write mode
        with open(data, "w") as file:
            # Writing content to the file
            file.write(str(data_to_save))
            print("Data successfully saved.")

        # After the `with` block, the file is automatically closed.
    except IOError as e:
        # Handles any I/O-related errors (e.g., disk issues or permissions errors)
        print(f"Error: An I/O error occurred: {e}")
        exit()
