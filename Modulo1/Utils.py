import os

def get_test_file_names(path):
    if os.path.isdir(path):
        return os.listdir(path)
    else:
        print("Error: The provided path is not a directory.")
        return []
    
    