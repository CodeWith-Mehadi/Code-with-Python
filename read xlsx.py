import pandas as pd
data = pd.read_excel("students.xlsx")
print(data) #show all data
print(' ') #space
print(data[["Name","Marks"]]) #show name and marks
print(' ')

passed_students = data[data['Passed'] == 'Yes'] #show students who passed
print(passed_students)
print(' ')

sci_top = data[(data['Subject'] == 'Science') & (data['Marks'] > 85)] #Show only Science students with marks above 85
print(sci_top)
print(' ')

passe_count = data[(data['Passed'] == 'Yes')] #Count how many students passed
print(passed_students)