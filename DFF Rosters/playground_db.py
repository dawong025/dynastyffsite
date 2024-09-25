import sqlite3
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
from update_sheets import *
from roster import *
sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')
import time

dff_db= sqlite3.connect("dynasty-db.db")

cursor = dff_db.cursor()

league_years = {
    2018: '380.l.76665',
    2019: '390.l.33135',
    2020: '399.l.20675',
    2021: '406.l.78372',
    2022: '414.l.105716',
    2023: '423.l.202017',
    2024: '449.l.35107'
}
league_year = 2023
league_week = 1

'''
Clear off current data in db
'''
# cursor.execute('DELETE FROM league_members')
# cursor.execute('DELETE FROM player')
# cursor.execute('DELETE FROM weekly_rostered where year = 2024 and week > 0')
cursor.execute('DELETE FROM picks')

dff_db.commit()
