'''
parse_sheets.py - Used to aggregate each team's roster history from /DFF Rosters sheets
'''

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import pandas as pd
from pandas import ExcelWriter

# iterate through every year's rosters on a week to week basis per team owner
# consolidate on a single sheet

output_file = 'dff word cloud.xlsx'

df_concat = pd.DataFrame()

with ExcelWriter(output_file) as output:
    for yr in range(2018, 2024):
        input_file = f"./DFF Rosters/dff {yr}.xlsx"
        for sheet_name, df in pd.read_excel(input_file, sheet_name = None).items():
            df['source_sheet'] = sheet_name
            df_concat = pd.concat([df_concat, df], ignore_index=True, sort=False)
        df_concat.to_excel(output, index=False)


