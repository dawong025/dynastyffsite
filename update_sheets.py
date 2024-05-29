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
    
    names = [sub['name'] for sub in roster if sub["position"] == position]
    
    for row, text in enumerate(names, start=positions[position][0]):
        ws.cell(column=owner_column, row=row, value=text)

    wb.save('dff.xlsx')


def load_team(owner, roster):
    print('DEBUG-' + owner)
    load_position("QB", roster, owner)
    load_position("WR", roster, owner)
    load_position("RB", roster, owner)
    load_position("TE", roster, owner)
    load_position("K", roster, owner)
    load_position("LB", roster, owner)
    load_position("DB", roster, owner)
    load_position("DL", roster, owner)

def update_rosters_post_17():
    print()