'''
get_transactions.py - Used to get the default draft position per owner pre-trades.

'''

from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import operator

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')
leagues = gm.league_ids(year = 2023)
dynasty = gm.to_league('423.l.202017')

team_names = []
owner_names = []

# iterate through initial dictionary to get team_key
list_team_keys = list(dynasty.teams().keys())
# Get list of team names

for key in list_team_keys:
    # print(dynasty.teams()[key])
    if "\'" in dynasty.teams()[key]["name"]:
        continue
    else:
        team_names.append(dynasty.teams()[key]["name"])
        owner_names.append(dynasty.teams()[key]["managers"][0]["manager"]["nickname"])


league = dict(zip(owner_names, team_names))

raw_transactions = []
add_transactions = dynasty.transactions("add", 15)
drop_transactions = dynasty.transactions("drop", 15)
print(drop_transactions[0]["players"]["0"]["player"][0][1]["player_id"])
print(drop_transactions[0]["players"]["0"]["player"][0][2]["name"]["full"])
print(drop_transactions[0]["players"]["0"]["player"][0][4]["display_position"])
print(drop_transactions[2])
# for drop in drop_transactions:
#     flag = 'n'
#     for at in add_transactions:
#         if drop['transaction_id'] == at['transaction_id']:
#             flag = 'y'
#             break
#     if flag == 'n':
#         raw_transactions.extend(drop_transactions)
#     flag = 'n'
'''
'add/drop':
    Added player:
        x["players"]["0"]['player'][0][2]['name']['full'], 
        x["players"]["0"]['player'][0][4]['display_position'] 
        int(x["players"]["0"]['player'][0][1]["player_id"])
                
        roster_index = strip_team_key(x["players"]["0"]['player'][1]['transaction_data'][0]['destination_team_key']) - 1
        roster = rosters[roster_index].roster

    Dropped player:           
        dropped_player_id = x["players"]["1"]["player"][0][1]["player_id"]
                
'add':
    x["players"]["0"]['player'][0][2]['name']['full'], 
    x["players"]["0"]['player'][0][4]['display_position'], 
    int(x["players"]["0"]['player'][0][1]["player_id"])
        
    roster_index = strip_team_key(x["players"]["0"]['player'][1]['transaction_data'][0]['destination_team_key']) - 1
    roster = rosters[roster_index].roster

'drop':
    dropped_player_id = x["players"]["0"]['player'][0][1]["player_id"]
'''




