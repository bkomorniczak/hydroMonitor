import pandas as pd

data = pd.read_csv('resources/codz_2022_01.csv', encoding='unicode_escape')


print(data.columns)

# print(data[data.contains('Daleszyce')])
