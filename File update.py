with open ("test.text", "a") as file :
    file.write("Add a new line.")
print("Add new line done")

with open("test.text", "r") as file :
    content = file.read()
    print("Update file content",content)