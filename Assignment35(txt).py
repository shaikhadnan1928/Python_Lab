#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_and_display_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the file name
read_and_display_file("ABC.txt")

"""
OUTPUT
hi adnan
abc file
python assignment

"""
