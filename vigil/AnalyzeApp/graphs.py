import plotly.express as px
import pandas as pd
import numpy as np
import os

class LineGraph:
    def __init__(self, csv_file, col_name) -> None:
        self.df = pd.read_csv(csv_file)
        self.col_name = col_name
        self.x_data = []
        self.y_data = []
        self.populate_data()

        self.fig = px.line(
            x=self.x_data, 
            y=self.y_data,
            title=self.col_name,
            labels={'x': "Timestamp", 'y': self.col_name}
        )
        self.fig.update_layout(
            title={
                "font_size": 30,
                "xanchor": 'center',
                'x': 0.5
            }
        )

        self._to_html = self.fig.to_html()
    
    def populate_data(self):
        for index, row in self.df.iterrows():
            self.x_data.append(row["timestamp"])
            self.y_data.append(row[self.col_name])

    def to_html(self):
        return self._to_html

def get_numeric_columns(path) -> list[str]:
    df = pd.read_csv(path)
    return [col for col in df.columns if col != "timestamp" and df[col].dtype in [np.float64, np.int64]]

def group_graphs(path, currconfig) -> dict:
    currconfig_subsystems = currconfig.SubsystemConfig.Subsystems.all()
    subsystems = [s.SubsystemName for s in currconfig_subsystems]

    numeric_columns = get_numeric_columns(path)
    grouping = {
        sub.casefold().capitalize(): 
            [LineGraph(path, col_name)
                for col_name in numeric_columns 
                if ((sub in col_name) or (sub[0:3] == col_name[0:3]) or (sub[0] == col_name[0]))
            ]
        for sub in subsystems
    }
    for sub, graphs in grouping.items():
        grouping[sub] = [graph.to_html() for graph in graphs]
    return grouping