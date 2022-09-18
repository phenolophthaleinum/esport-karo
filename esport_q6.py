import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
social = data.iloc[:, 35]
social = social.to_frame()
social.columns = ["value"]
social["value"] = social["value"].apply(lambda x: x.replace("bierząco", "bieżąco"))
social_counts = social.apply(pd.Series.value_counts)
social_counts = social_counts.rename_axis("answer").reset_index()

fig = px.pie(social_counts, values="value", names="answer",
             title="W jakim stopniu obserwujesz Swoje ulubione drużyny e-sportowe w mediach społecznościowych (np. Twitter, Instagram)?",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn'
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
