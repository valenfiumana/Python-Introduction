# Pandas :panda_face: :panda_face:

Pandas is a Python library used for working with data sets.

Pandas allows us to analyze big data and make conclusions based on statistical theories. It has functions for analyzing, cleaning, exploring, and manipulating data.


## Importing Panda

```python
import pandas as pd
```

## Reading and exporting files

```python
import pandas as pd

arboles = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
# pd.read_json()
# pd.read_excel()
# pd.read_html()
# pd.read_xlm()
# pd.read_sql()
# etc.

arboles.to_csv('filename.csv')
# arboles.to_json('filename.json')
# arboles.to_sql('filename.sql')
# etc.
```

## DataFrames

A DataFrame is a 2-dimensional data structure that can store data of different types (including characters, integers, floating point values, categorical data and more) in columns. It is similar to a spreadsheet, a SQL table or the data.frame in R.

Each column in a DataFrame is a Series.

![img](./img/pandas_dataframe.svg)
![img](./img/pandas_series.svg)

```python
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)
#                        Name   Age    Sex
# 0   Braund, Mr. Owen Harris   22    male
# 1  Allen, Mr. William Henry   35    male
# 2  Bonnell, Miss. Elizabeth   58  female
```

#### Accessing data
* df.series_name
* df.head(number_of_lines) --> prints lines from top to bottom
* df.tail(number_of_lines) --> prints lines from bottom to top

```python
df["Age"]
df.Age
# 0    22
# 1    35
# 2    58

df.loc[127] # access through index
df.iloc[124] #access through possition

df.iloc[300:-10]

df['Age'].unique() # [22 35 58]

df['Age'].value_counts() 
# 22    1
# 35    1
# 58    1

df['Sex'] == "female"
# 0    False
# 1    False
# 2     True

print(df.isin(["Allen, Mr. William Henry", 35, "female"]))
#     Name    Age    Sex
# 0  False  False  False
# 1   True   True  False
# 2  False  False   True

print(df.isin({"Sex": ["male"]}))
#     Name    Age    Sex
# 0  False  False   True
# 1  False  False   True
# 2  False  False  False

females = df[df['Sex'] == "female"]
#                        Name  Age     Sex
# 2  Bonnell, Miss. Elizabeth   58  female

df.head(1) # --> df.head() == df.head(5)
#                       Name  Age   Sex
# 0  Braund, Mr. Owen Harris   22  male

df.tail(2) # --> df.tail() == df.tail(5)
#                        Name  Age     Sex
# 1  Allen, Mr. William Henry   35    male
# 2  Bonnell, Miss. Elizabeth   58  female

df.columns
# Index(['Name', 'Age', 'Sex'], dtype='object')

df.index
# RangeIndex(start=0, stop=3, step=1)

df.shape
# (3, 3)

```

### Getting info from dataframe

```python
df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64 
#  2   Sex     3 non-null      object
# dtypes: int64(1), object(2)
# memory usage: 200.0+ bytes
# None
```

```python
df.describe()

#              Age
# count   3.000000
# mean   38.333333
# std    18.230012
# min    22.000000
# 25%    28.500000
# 50%    35.000000
# 75%    46.500000
# max    58.000000
```

### Max, min, ...
```python
df['Age'].max() # 48
df['Age'].min() # 22

df['Age'].idxmax() # 2
df['Age'].idxmin() # 0
```

### Creating DataFrames

```python
import pandas as pd

# From dictionary
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

# With numpy
import numpy as np
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

# From lists
alumnos = ['Carla', 'Daniel', 'Fernan', 'Ivan']
notas = [np.random.randint(10)+1 for i in range(4)]
df_alumnos = pd.DataFrame({'Calificacion': notas}, index=alumnos)
df_alumnos2 = pd.DataFrame({'Alumno':alumnos, 'Calificacion': notas})
```

### Adding and removing items
```python
df_alumnos = df_alumnos.drop(columns='Aprobado')

aprobado = [nota>6 for nota in notas] # Creating a list
df_alumnos['Aprobado'] = aprobado # Adding to dataframe
```

### Map y Lambda
#### Map()
With map() you can apply a function to every element of a Serie or Dataframe. 

```python
def lowerCase(str):
  return str.lower()

df['Sex'] = df['Sex'].map(lowerCase)
```

#### Lambda
```python
lambda argument(s) : expression
```
1. lambda is a keyword in Python for defining the anonymous function.
2. argument(s) is a placeholder, that is a variable that will be used to hold the value you want to pass into the function expression. A lambda function can have multiple variables depending on what you want to achieve.
3. expression is the code you want to execute in the lambda function.

```python
f1 = lambda x: x**2

# == def f2(x):
#       return x**2
```

### Duplicates and missing data

```python
# duplicates
df.drop_duplicates()

# count missing data (null)
df.isnull().sum()

# drop rows with missing data
df.dropna()
df.dropna(inplace=True)

# drop cols with missing data
nf.dropna(axis=1)

# write sth if is null
df.fillna("No data")
```

### Time series
* pd.date_range(start_date, end_date, number_periods, frequency)
* pd.Timestamp(year, month, day) --> point in time
* pd.Timedelta --> difference between dates
* pd.to_datetime(Serie, format='%d/%m/%Y')
```python
pd.date_range('2022-04-01', periods = 8, freq='D') # frequency: month (M), day (D), hour (H), etc
pd.date_range('2022-04-01 18:00', periods = 7, freq='H')
pd.date_range(start='2022-04-24', end='2022-04-27', periods=3)

pd.Timestamp(2012, 5, 1)

pd.Timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
difT = pd.Timestamp(2022, 5, 11) - pd.Timestamp(2012, 5, 1)

s = pd.Series(['3/11/2000', '3/12/2000', '13/8/2000'] * 1000)
s_date = pd.to_datetime(s, format='%d/%m/%Y')
```
### Plot
```python
import matplotlib.pyplot as plt

df.plot.scatter(x='time', y='km')
df[-500:].plot.line(x='time', y='km')

plt.show()
```
```python

```
```python

```
```python

```

