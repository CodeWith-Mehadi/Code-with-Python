import os

file_path = "test.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' successfully deleted.")
else:
    print(f"File '{file_path}' can't find.")
