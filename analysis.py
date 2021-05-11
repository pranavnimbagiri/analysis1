import csv
import pandas
import plotly.express as go
df=pandas.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=['level 1','level 2','level 3','level 4'],orientation='h'
))
#fig.show()
student_df=df.loc[df['student_id']=="TRL_987"]
fig=go.Figure(go.Bar(
    x=student_df.groupby("level")["attempt"].mean(),
    y=['level 1','level 2','level 3','level 4'],orientation='h'
))
fig.show()