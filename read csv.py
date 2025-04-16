import pandas as pd

data = pd.read_csv("students.csv")
print(data) #read csv data
print(' ') #one line space
print(data['Name']) #read csv name
print(' ')
print(data['Marks']) #read csv marks
print(' ')

high_scores = data[data['Marks'] > 80] #show marks greater than 80 )
print(high_scores)