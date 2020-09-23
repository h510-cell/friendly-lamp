import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("data3.csv")

student_df = df.loc[df['student_id'] == "TRL_987"]

print(student_df.groupby("level")["attempt"].mean())

fig = px.scatter(student_df.groupby("level")["attempt"].mean()
                ,x=student_df
                ,y=['level1','level2','level3','level4'],
                color="attempt")

fig.show()
