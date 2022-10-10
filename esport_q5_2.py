import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("esport.csv")
watching = data.iloc[:, 29:35]
watching_names = [x.split("*")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(watching.columns)]
watching.columns = watching_names
v = watching.iloc[:, 0].unique()[:-1]
watching = watching.apply(lambda x: x.fillna(np.random.choice(v)))
watching["Płeć"] = data.iloc[:, 38]

# man
watching_m = watching.loc[watching['Płeć'] == 'Mężczyzna'].iloc[:, :-1]
watching_m_counts = watching_m.apply(pd.Series.value_counts)
watching_m_counts = watching_m_counts.rename_axis("answer").reset_index()
watching_m_counts = watching_m_counts.melt('answer', var_name="reason", value_name="value").reset_index(drop=True)
watching_m_counts.fillna(0, inplace=True)
watching_m_counts['sex'] = 'Mężczyzna'
# print(watching_m_counts)

# woman
watching_w = watching.loc[watching['Płeć'] == 'Kobieta'].iloc[:, :-1]
watching_w_counts = watching_w.apply(pd.Series.value_counts)
watching_w_counts = watching_w_counts.rename_axis("answer").reset_index()
watching_w_counts = watching_w_counts.melt('answer', var_name="reason", value_name="value").reset_index(drop=True)
watching_w_counts.fillna(0, inplace=True)
watching_w_counts['sex'] = 'Kobieta'
# print(watching_w_counts)

# concat
dfs = [watching_m_counts, watching_w_counts]
final_df = pd.concat(dfs)
print(final_df)

fig = px.histogram(final_df, x="reason", y="value", color="answer", facet_row='sex',
                   barnorm="fraction",
                   text_auto='.2%',
                   title="Oglądam wydarzenia e-sportowe ponieważ: ",
                   color_discrete_sequence=px.colors.qualitative.G10,
                   template='seaborn')
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.update_yaxes(matches=None, showticklabels=True, visible=True)
for axis in fig.layout:
    if type(fig.layout[axis]) == go.layout.YAxis:
        fig.layout[axis].title.text = ''
        fig.layout[axis].tickformat = ".2%"
    if type(fig.layout[axis]) == go.layout.XAxis:
        fig.layout[axis].title.text = ''
# fig.update_layout(yaxis_tickformat=".2%")
fig.show()
