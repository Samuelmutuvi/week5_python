# file_handling_assignment.py
def create_and_write_file():
    """Creates a new file and writes initial content to it."""
    try:
        # Creating and opening the file in write mode ('w')
        with open("my_file.txt", 'w') as file:
            # Writing three lines to the file
            file.write("Hello, this is the first line.\n")
            file.write("Here is the number 12345.\n")
            file.write("Third line with some random text.\n")
        print("File created and written successfully.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")

def read_and_display_file():
    """Reads the content of the file and displays it."""
    try:
        # Opening the file in read mode ('r')
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("File content:\n", content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    """Appends additional content to the existing file."""
    try:
        # Opening the file in append mode ('a')
        with open("my_file.txt", 'a') as file:
            # Appending three additional lines to the file
            file.write("Appending a fourth line.\n")
            file.write("Another line with number 67890.\n")
            file.write("This is the final line in the file.\n")
        print("File appended successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

if __name__ == "__main__":
    try:
        # Creating and writing to the file
        create_and_write_file()

        # Reading and displaying the file content
        read_and_display_file()

        # Appending additional lines to the file
        append_to_file()

        # Reading the file again to display the appended content
        read_and_display_file()

    except Exception as e:
        print(f"An unexpected error occurred in the main program: {e}")
    finally:
        print("File handling operations complete.")
