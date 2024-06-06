from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

def load_position(position, roster, owner):
    positions = { #end row + 1 for inclusivity
        "QB": [6, 16],
        "WR": [17, 34],
        "RB": [35, 47],
        "TE": [49, 58],
        "K": [59, 62],
        "LB": [63, 72],
        "DB": [73, 79],
        "DL": [80, 86]
    }

    wb = load_workbook('dff.xlsx')
    ws = wb['S8 End Roster']
    owner_column = -1
    for col in range (1, 18):
        char = get_column_letter(col)
        if (ws[char + str(2)].value == owner):
            owner_column = col
    
    # Create a list of names to load onto spreadsheet where position matches via list comprehension
    names = [sub.name for sub in roster if sub.position == position]
    
    # Append to spreadsheet at start row
    for row, text in enumerate(names, start=positions[position][0]):
        ws.cell(column=owner_column, row=row, value=text)

    wb.save('dff.xlsx')

def load_team(owner, roster):
    print('DEBUG-' + owner)
    position_types = ["QB", "RB", "WR", "TE", "K", "LB", "DB", "DL"]

    for position in position_types:
        load_position(position, roster, owner)
    
def strip_team_key(team_key):
    return int(team_key[team_key.rindex('.')+1:])