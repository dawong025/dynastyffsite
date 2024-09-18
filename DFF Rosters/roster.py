'''
roster.py - Classes relevant to roster sheet management

Roster -
    owner_name - String
    team_key - String
    roster - [Player]

Player - Only name and position are needed, position for future reference/usage
    name - String
    position - String
    player_id - Int
'''
class Roster:
    def __init__(self, owner_name, team_key, roster):
        self.owner_name = owner_name
        self.team_key = team_key
        self.roster = roster

    def __str__(self):
        return f"{self.owner_name} - {self.team_key}\n {self.roster}"
    
    # Team key sorter
    def __lt__(self, other):
        return int(self.team_key[self.team_key.rindex('.')+1:]) < int(other.team_key[other.team_key.rindex('.')+1:])

# TODO: Find a way to get team at current state, e.g. Melvin Gordon's team in 2021
class Player:
    def __init__(self, name, position, player_id):
        self.name = name
        self.position = position
        self.player_id = player_id
        # self.team = team

    def __str__(self):
        return f"[{self.player_id}] {self.name}, {self.position}"
    