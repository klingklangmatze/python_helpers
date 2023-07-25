import os

def rename_file(file_path, old_string, new_string):
    try:
        new_file_path = file_path.replace(old_string, new_string)
        os.rename(file_path, new_file_path)
        print(f"File '{file_path}' has been renamed to '{new_file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
folder_path = '/path/to/your/directory'
old_string = 'old_filename'
new_string = 'new_filename'
file_path = f"{folder_path}/{old_string}"

rename_file(file_path, old_string, new_string)
