with open("data.txt", "r") as file:
    lines = file.readlines()

print("All emails:")
for line in lines:
    print(line.strip()) #print all data

unique_emails = list(set([line.strip() for line in lines])) #remove duplicate

print("\nUnique emails:")
for email in unique_emails:
    print(email)
