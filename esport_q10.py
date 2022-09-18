import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
edu = data.iloc[:, 40]
edu = edu.to_frame()
edu.columns = ["value"]
edu_counts = edu.apply(pd.Series.value_counts)
edu_counts = edu_counts.rename_axis("answer").reset_index()

fig = px.pie(edu_counts, values="value", names="answer",
             title="Wykształcenie",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn',
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
