import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import *
import pandas as pd
import numpy as np
import constants

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
        for _, row in self.df.iterrows():
            self.x_data.append(row["timestamp"])
            self.y_data.append(row[self.col_name])

    def to_html(self):
        return self._to_html

class DoubleLineGraph:
    def __init__(self, csv_file, col_names) -> None:
        self.df = pd.read_csv(csv_file)
        self.col_names = col_names
        self.x_data = []
        self.y_data = {}

        self.populate_data()

        self.fig = px.line(
            self.df,
            x='timestamp',
            y=self.col_names,
            title=" vs. ".join(self.col_names),
            labels={'value': 'Value', 'variable': 'Line', 'timestamp': 'Timestamp'}
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
        self.x_data = self.df["timestamp"].tolist()
        for col in self.col_names:
            self.y_data[col] = self.df[col].tolist()

    def to_html(self):
        return self._to_html

class LineGroup:
    def __init__(self, graphs:list):
        if len(graphs) == 0:
            self._to_html = None
            return
        
        self.graphs = graphs
        layout = Layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        self.fig = go.Figure(layout=layout)
        for graph in graphs:
            for trace in graph.fig.data:
                self.fig.add_trace(trace)

        self.fig.update_layout(
            autosize=False,
            width=1000,
            updatemenus=[
                {
                    'buttons': [
                        {
                            'label': self.get_label(graph),
                            'method': 'update',
                            'args': [
                                {'visible': self.visibles(graph)},
                                {'title': self.get_title(graph)}
                            ]
                        } for graph in graphs
                    ],
                    'direction': 'down',
                    'showactive': True
                }
            ]
        )

        self.fig.update_traces(visible=False)
        try:
            for trace in range(len(graphs[0].fig.data)):
                self.fig.data[trace].visible = True
        except IndexError:
            pass
        
        self._to_html = self.fig.to_html()

    def get_label(self, graph):
        try:
            return graph.col_name
        except AttributeError:
            return self.getattribute(graph.col_names[0])
    
    def get_title(self, graph):
        try:
            return graph.col_name
        except AttributeError:
            return f"actual vs desired {self.getattribute(graph.col_names[0])}"

    def getattribute(self, col_name:str):
        for arg in constants.args:
            if arg in col_name:
                return arg

    def visibles(self, curr_graph):
        visible = []
        for graph in self.graphs:
            if graph == curr_graph:
                visible.extend([True]*len(graph.fig.data))
            else:
                visible.extend([False]*len(graph.fig.data))
        return visible

    def to_html(self):
        return self._to_html

class Fault:
    def __init__(self, title:str, isactive:bool, freq:int, timestamps:list) -> None:
        self.title = title
        self.freq = freq
        self.timestamps = timestamps
        self.isactive = isactive
    
    def fill_timestamps(self, path):
        df = pd.read_csv(path)

        for _, row in df.iterrows():
            if row[self.title] == True:
                self.timestamps.append(round(row["timestamp"], 3))

        self.freq = len(self.timestamps)

def get_numeric_columns(path) -> list[str]:
    df = pd.read_csv(path)
    return [col for col in df.columns if col != "timestamp" and df[col].dtype in [np.float64, np.int64]]

def get_fault_columns(path) -> list[str]:
    df = pd.read_csv(path)
    return [col for col in df.columns if df[col].dtype == np.bool and ('fault' in col or 'error' in col or 'err' in col)]

def belongs_to(column, sub) -> bool:
    try: return ((sub.lower() in column.lower()) or (sub[0:6].lower() == column[0:6].lower()) or (sub[0:5].lower() == column[0:5].lower()) or (sub[0:4].lower() == column[0:4].lower()) or (sub[0:3].lower() == column[0:3].lower()) or (sub[0:2].lower() == column[0:2].lower()))
    except: return False

def find_versus(curr_column, columns, normalized_columns):
    if "desired" in curr_column.lower():
        for idx, col in enumerate(normalized_columns):
            if col == curr_column.lower().replace("desired", "actual"):
                return (True, columns[idx])
            elif col == curr_column.lower().replace("desired", "act"):
                return (True, columns[idx])
    elif "des" in curr_column.lower():
        for idx, col in enumerate(normalized_columns):
            if col == curr_column.lower().replace("des", "actual"):
                return (True, columns[idx])
            elif col == curr_column.lower().replace("des", "act"):
                return (True, columns[idx])
    elif "actual" in curr_column.lower():
        for idx, col in enumerate(normalized_columns):
            if col == curr_column.lower().replace("actual", "desired"):
                return (True, columns[idx])
            elif col == curr_column.lower().replace("actual", "des"):
                return (True, columns[idx])
    elif "act" in curr_column.lower():
        for idx, col in enumerate(normalized_columns):
            if col == curr_column.lower().replace("act", "desired"):
                return (True, columns[idx])
            elif col == curr_column.lower().replace("act", "des"):
                return (True, columns[idx])
    else:
        return (False, None)

def find_complement(curr_column:str, columns:list):
    normalized_columns = [column.lower() for column in columns]
    for arg in constants.args:
        if arg in curr_column.lower():
            return find_versus(curr_column, columns, normalized_columns)
        else:
            continue
    return (False, None)

def adv_groups(path, currconfig) -> dict:
    currconfig_subsystems = currconfig.SubsystemConfig.Subsystems.all()
    subsystems = [s.SubsystemName for s in currconfig_subsystems]
    numeric_columns = get_numeric_columns(path)
    fault_columns = get_fault_columns(path)
    grouping = {}

    for sub in subsystems:
        graphs = []
        faults = []
        past_complements = []
        for col_name in numeric_columns:
            if belongs_to(col_name, sub):
                complement = find_complement(col_name, numeric_columns)
                past_complements.append(complement[1])
                if col_name in past_complements:
                    continue
                elif complement[0]:
                    graphs.append(DoubleLineGraph(path, [col_name, complement[1]]))
                else:
                    graphs.append(LineGraph(path, col_name))
        curr_group = LineGroup(graphs)
        if len(graphs) == 0:
            curr_group = None
        
        for col_name in fault_columns:
            if belongs_to(col_name, sub):
                if len(faults) == 0:
                    fault = Fault(col_name, True, 0, [])
                else:
                    fault = Fault(col_name, False, 0, [])
                fault.fill_timestamps(path)
                faults.append(fault)

        perf = get_performance_rating(curr_group, faults)
        health = get_health_rating(curr_group, faults)

        grouping[sub.casefold().capitalize()] = [curr_group, faults, perf, health]
    
    for sub, graph in grouping.items():
        try: grouping[sub][0] = graph[0].to_html()
        except AttributeError: continue
    
    return grouping

def get_performance_rating(grouping, faults) -> int:
    if grouping == None:
        return None
    return 96

def get_health_rating(grouping, faults) -> int:
    if grouping == None:
        return None
    return 90