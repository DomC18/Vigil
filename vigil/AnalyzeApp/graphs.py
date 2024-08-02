import plotly.express as px
import pandas as pd
import numpy as np
import os

class Graph:
    def __init__(self, csv_file, col_name) -> None:
        self.df = pd.read_csv(csv_file)
        self.col_name = col_name
        self.x_data = []
        self.y_data = []
        self.populate_data()
        self.fig = px.line(
            x=self.x_data, 
            y=self.y_data
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