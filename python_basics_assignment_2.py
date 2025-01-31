import pandas as pd
df = pd.read_csv("gym_members_exercise_tracking.csv")
pd.set_option("display.max_rows",None)
print(df.head())
print(df)

col_names = df.columns
print(col_names)

col_based_data = df["BMI"]
print(col_based_data)

col_based_data = df[["Fat_Percentage","BMI"]]
print(col_based_data)

null_data_finding = df.isnull().sum()
print(null_data_finding)

data_shape = df.shape
print(data_shape)

data_info = df.info
print(data_info())

data_description = df.describe
print(data_description())