import PySimpleGUI as sg
import pandas as pd
from datetime import date, datetime

now = datetime.now()
curent_date = date.today()
current_time = now.strftime("%H:%M:%S")
