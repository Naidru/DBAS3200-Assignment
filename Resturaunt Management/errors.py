# ERROR 404:
# This error indicates that the input was not found in any data source

# ERROR 403:
# This error indicates that the input is not unique in a data source

# ERROR 1:
# Malformed Data List [Fatal]
# This error indicates that when doing a search, data was not found when it should have been found. This indicates that
# the data source used to pull information from was unsuccessful.

def error_handling(error_code,error_plain_text):
    if error_code == 404:
        print(f"The dish entered ({error_plain_text}) does not exist")
    elif error_code == 403:
        print(f"The dish entered ({error_plain_text}) already exists")
    elif error_code == 1:
        print(f"Fatal error!")
        print(f"Malformed data list - Please refer to the errors.py file")
        print({error_plain_text})
        exit()