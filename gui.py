import PySimpleGUI as sg
import pandas as pd
from datetime import date, datetime
from functions import get_items


now = datetime.now()
curent_date = date.today()
current_time = now.strftime("%H:%M:%S")

label = sg.Text("Press Add button to enter item.")
add_button = sg.Button("Add", key='add')
toprow = ["ID","SERIAL_NUM","ITEM_DESC","DATE"]
item_table = sg.Table(values=get_items(), headings=toprow,
                      auto_size_columns=True, justification='left',
                      key='itemtable', enable_events=True, expand_x=True,
                      expand_y=True, enable_click_events=True,
                      selected_row_colors='black on yellow')

layout = [[label], [add_button], [item_table]]

window = sg.Window("Inventory - app", layout=layout, size=(600,400))

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
window.close()