import plotly.express as px
from palmerpenguins import load_penguins
from shiny.express import input, ui, render
from shinywidgets import render_widget  
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

penguins = load_penguins()

ui.page_opts(title="Penguins Dashboard", fillable=True)

ui.input_slider("n", "Number of bins", 1, 100, 20)

with ui.sidebar(position="right", bg="#f8f8f8", open="open"):
    ui.h2("Sidebar")
    ui.input_selectize(  
        "select_attribute",  
        "Name of the selectize",  
        choices=["Option 1","Option 2","Option 3"],
        selected=["Green"])
    ui.input_numeric("plotly_bin_count", "Plotly bin numeric",1,min=1,max=10)
    
    ui.input_slider("seaborn_bin_count", "Seaborn bin count", 10, 100, 20,
                    step=5, animate=True)
    ui.input_checkbox_group(
        "selected_species_list",
        "Selected species list",
        choices=["Option 1", "Option 2", "Option 3"],
        selected="Option 1", inline=True)
    ui.hr()
    ui.h2("Test")
    ui.a("My GitHub", href="https://github.com/bncodes19/cintel-02-data", target="_blank")
    # Use ui.hr() to add a horizontal rule to the sidebar


#with ui.layout_columns(): to display:
#   a DataTable (showing all data),
#   a Data Grid (showing all data), 

#with ui.layout_columns():
fig, ax = plt.subplots()
@render.plot(alt="A histogram")
def histogram():

#    a Seaborn Histogram (showing all species)
#and a Plotly Scatterplot (showing all species)
