import pandas as pd 

grades_dict = {'Wally': [87,96,70], 'Eva':[100,87,90], 'Sam':[94,77,90], 'Katie':[100,81,82],'Bob':[83,65,85]}

grades= pd.DataFrame(grades_dict)
 
print(grades)

grades.index = ['Test1', 'Test2', 'Test3']
print(grades)

# print(grades['Eva'])
# print(grades.Sam) #gets value of object 'Sam'

# print(grades.loc['Test1']) # at the row level (so gives scores for everyone's first test')

# print(grades.iloc[1]) ### 0-based, so it gives all the scores for Test 2

# print(grades.loc['Test1' : 'Test3']) # slicing for 3 tests

#print(grades.iloc[0:2]) ## gives tests from [0] to [2] (so Test 1-2)

### These give only test 1 and 3:
#print(grades.iloc[[0,2]])
#print(grades.iloc[0::2])

#print(grades.loc['Test1':'Test2', ['Eva','Katie']])

#print(grades.iloc[[0,2],0:3]) ## only shows Test 1 and 3 for Wally,Eva,Sam

#print(grades[grades >= 90])  ### NaN means not a number, so it measn it failed the boolean check

#print(grades[[grades>=80],[grades<=90]])

#print(grades[(grades>=80) & (grades<=90)])  # shows grades between 90 and 80
#print(grades[(grades>=80) | (grades<=90)])  # | means 'or' --> shows grades that are EITHER greater than 80 OR less than 90 

# print(grades.at['Test2','Eva']) ## results in '87' because it gives the value at the position of Test 2 and Eva

# print(grades.iat[0,2])  # shows value in row 1 [0], and column 3 [2]

# grades.at['Test2','Eva'] = 100  ## changes it for the value in the dataframe 
# print(grades.at['Test2','Eva'])


# pd.set_option('precision',2) ## narrows decritpion values down to two devimal places
# print(grades.describe())

# grades.T ### T means transpose --> this switches column and rows
# print(grades.T) 

#print(grades.sort_index(ascending=False)) ### this sorts descending based on the indexes (not the values in there)
#print(grades.sort_index(axis=1))  # the defualt is axis=0, meaning it sorts by rows. If axis is set to 1, it sorts by column value.
## The result is the column names sorted ascendingly by oclumn name (alphabetically)

print(grades.sort_values(by='Test1', axis=1, ascending=False))  ## only sorts values in Test1, ascendingly by column value
print(grades.T.sort_values(by='Test1', ascending=False)) 

print(grades.loc['Test1'].sort_values(ascending=False)) # only displays Test1, but sorts it like in the command above

