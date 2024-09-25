import sqlite3

dff_db = sqlite3.connect("dynasty-db.db")

cursor = dff_db.cursor()

# cursor.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS league_members (
#             member_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             team_key VARCHAR(50) NOT NULL UNIQUE,
#             member_name VARCHAR(100) NOT NULL,
#             year INTEGER
#         )
#     '''
# )

# cursor.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS player (
#             player_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#             name VARCHAR(255),
#             position VARCHAR(20),
#             yahoo_player_id INTEGER UNIQUE
#         )
#     '''
# )

# cursor.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS weekly_rostered(
#             wk_rostered INTEGER PRIMARY KEY AUTOINCREMENT,
#             week INTEGER,
#             year INTEGER,
#             member_id INTEGER,
#             player_id INTEGER,
#             FOREIGN KEY(member_id)
#             REFERENCES league_members(member_id)
#                 ON UPDATE SET NULL
#                 ON DELETE SET NULL
#             FOREIGN KEY (player_id)
#             REFERENCES player(player_id)
#                 ON UPDATE SET NULL
#                 ON DELETE SET NULL
#         )
#     '''
# )

# cursor.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS rookie_draft(
#             draft_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             year INTEGER,
#             member_id INTEGER,
#             player_id INTEGER,
#             pick VARCHAR(20),
#             FOREIGN KEY(member_id)
#             REFERENCES league_members(member_id)
#                 ON UPDATE SET NULL
#                 ON DELETE SET NULL
#             FOREIGN KEY (player_id)
#             REFERENCES player(player_id)
#                 ON UPDATE SET NULL
#                 ON DELETE SET NULL
#         )
#     '''
# )



