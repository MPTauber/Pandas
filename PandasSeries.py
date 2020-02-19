##### virtual environemtn: py -3 -m venv pandas_venv
##### pandas_venv/scripts/activate
##### pip install pandas

import pandas as pd 

grades = pd.Series([87,100,94])

print(grades)

print(pd.Series(98.6, range(3)))

'''print(grades[0])
print(grades.count())
print(grades.mean())
print(grades.min())
print(grades.max())
print(grades.std())'''

print(grades.describe()) ## this does in one line what the above does

grades = pd.Series([87,100,94], index = ['Wally','Eva','Sam'])

grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

print(grades['Eva'])

print(grades.Wally) ## you can do this, because with the dot method it became an object 

print(grades.dtype) ## what kind of object it is (data type)

print(grades.values) ## look at all the values 

hardware = pd.Series(['Hammer', 'Saw','Wrench'])
print(hardware)
print(hardware.str.contains('a')) ## show wether each of these contains an 'a' --> produces logical series (TRUE/FALSE)

print(hardware.str.upper())
print(hardware)