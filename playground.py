# playground.py - A file to test various commands

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

