import PySimpleGUI as sg
import pandas as pd
from datetime import date, datetime
from functions import get_items
import openpyxl
import sqlite3


now = datetime.now()
curent_date = date.today()
current_time = now.strftime("%H:%M:%S")
df_csv = pd.read_csv("data.csv")
date_time = f"{curent_date} {current_time}"
#add window
label_add = sg.Text("Enter a parameters of item")
text_id = sg.Text("Enter ID: ")
input_id = sg.Input("", key='id')
text_s_num = sg.Text("Enter serial number: ")
input_s_num = sg.Input("", key='serial')
text_description = sg.Text("Enter description: ")
input_description = sg.Input("", key='description')
text_data = sg.Text("Date")
input_data = sg.Input(f"{date_time}", key='date')
button_accept = sg.Button("Accept", key='accept')
button_cancel = sg.Button("Cancel", key="cancel")

#Add a params for input to make them shorter
add_layout = [[label_add],[text_id, input_id, text_s_num, input_s_num],
              [text_description, input_description, text_data, input_data],
              [button_accept, button_cancel]]

# Main Window
label = sg.Text("Press Add button to enter item.")
add_button = sg.Button("Add", key='add')
toprow = ["ID","SERIAL_NUM","ITEM_DESC","DATE"]
item_table = sg.Table(values=get_items(), headings=toprow,
                      auto_size_columns=True, justification='left',
                      key='itemtable', enable_events=True, expand_x=True,
                      expand_y=True, enable_click_events=True,
                      selected_row_colors='black on yellow')
edit_button = sg.Button("Edit", key='edit')
remove_button = sg.Button("Remove", key='remove')
exit_button = sg.Button("EXIT", key='exit')
export_csv = sg.Button("Export to csv", key='ecsv')
export_xlsx = sg.Button("Export to excel", key='exlsx')

# Layout for main window
layout = [[label], [add_button],
          [item_table],
          [edit_button, remove_button, export_csv, export_xlsx],
          [exit_button]]

window = sg.Window("Inventory - app", layout=layout, size=(600,400))
window_add = sg.Window("Adding Item", layout=add_layout)

while True:
    event, values = window.read()
    match event:
        case 'add':
            window_add.read()
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break
        case 'ecsv':
            df_csv.to_csv("exproted_data.csv", index=False)
            sg.popup("Data has been exported to csv.",title="Inventory Export")
        case 'exlsx':
            df_csv.to_excel("exported_data.xlsx", index=False)
            sg.popup("Data has been exported to xlsx.",title="Inventory Export")

window.close()