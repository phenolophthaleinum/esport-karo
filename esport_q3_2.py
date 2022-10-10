import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("esport.csv")
statement = data.iloc[:, 16:28]
statement_names = [x.split(":")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(statement.columns)]
statement.columns = statement_names
v = statement.iloc[:, 0].unique()[:-1]
statement = statement.apply(lambda x: x.fillna(np.random.choice(v)))
statement["Płeć"] = data.iloc[:, 38]

# man
statement_m = statement.loc[statement['Płeć'] == 'Mężczyzna'].iloc[:, :-1]
statement_m_counts = statement_m.apply(pd.Series.value_counts)
statement_m_counts = statement_m_counts.rename_axis("answer").reset_index()
statement_m_counts = statement_m_counts.melt('answer', var_name="statement", value_name="value").reset_index(drop=True)
statement_m_counts.fillna(0, inplace=True)
statement_m_counts['sex'] = 'Mężczyzna'

# woman
statement_w = statement.loc[statement['Płeć'] == 'Kobieta'].iloc[:, :-1]
statement_w_counts = statement_w.apply(pd.Series.value_counts)
statement_w_counts = statement_w_counts.rename_axis("answer").reset_index()
statement_w_counts = statement_w_counts.melt('answer', var_name="statement", value_name="value").reset_index(drop=True)
statement_w_counts.fillna(0, inplace=True)
statement_w_counts['sex'] = 'Kobieta'

# concat
dfs = [statement_m_counts, statement_w_counts]
final_df = pd.concat(dfs)
print(final_df)

# print(statement)
# values_map = {
#     "Zdecydowanie się nie zgadzam": 1,
#     "Raczej się nie zgadzam": 2,
#     "Nie mam zdania": 3,
#     "Raczej się zgadzam": 4,
#     "Zdecydowanie się zgadzam": 5,
# }
# mapped_statement = statement.apply(lambda x: pd.Series.map(x, values_map))
# # mapped_statement = mapped_statement.rename_axis("answer").reset_index()
# print(mapped_statement.describe().T)

fig = px.histogram(final_df, x="statement", y="value", color="answer", facet_row='sex',
                   barnorm="fraction",
                   text_auto='.2%',
                   title="Proszę stwierdzić na ile zgadzasz się ze stwierdzeniem: Bardzo często spędzam czas wolny:",
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
fig.show()
