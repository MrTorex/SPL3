import pandas as pd # type: ignore
import numpy as np # type: ignore

#1
df = pd.read_csv('Housing.csv')

#2
df_sample = df.head(1000)

#3
missing_data = df_sample.isnull().sum()
print("Пропуски в данных:\n", missing_data)

#4
df_sample = df_sample.fillna(df_sample.median(numeric_only=True))
df_sample = df_sample[df_sample['area'] < 9000]

#5
room_counts = df_sample['bedrooms'].value_counts()
print("Количество квартир с разным количеством комнат:\n", room_counts)

#6
df_sample.to_csv('surname.csv', index=False)
print("Обработанный массив сохранен в файл surname.csv")
