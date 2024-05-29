from datetime import datetime
import time
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import json
from openpyxl import Workbook, load_workbook
from update_sheets import *
sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')

leagues = gm.league_ids(year = 2023)
dynasty = gm.to_league('423.l.202017')

end_date =dynasty.settings()['end_date']
end_date_as_dt = datetime.strptime(dynasty.settings()['end_date'], '%Y-%m-%d')

eta = dynasty.transactions("add", 20)
etd = dynasty.transactions("drop", 20) #same as ETA despite documentation

for drop in etd:
    print(drop)

# print(datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(eta[1]['timestamp']))), '%Y-%m-%d %H:%M:%S'))

post_17_transactions = [x for x in eta if 
                         end_date_as_dt < datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(x['timestamp']))), '%Y-%m-%d %H:%M:%S')]

extend = [x for x in eta if 
                         end_date_as_dt < datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(x['timestamp']))), '%Y-%m-%d %H:%M:%S')]

post_17_transactions.extend(extend)
# print(len(post_17_transactions))

# for x in post_17_transactions:
#     print(x['transaction_key'])




