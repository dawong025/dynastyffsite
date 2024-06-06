class Roster:
    def __init__(self, owner_name, team_key, roster):
        self.owner_name = owner_name
        self.team_key = team_key
        self.roster = roster

    def __str__(self):
        return f"{self.owner_name} - {self.team_key}\n {self.roster}"
    
    def __lt__(self, other):
        return int(self.team_key[self.team_key.rindex('.')+1:]) < int(other.team_key[other.team_key.rindex('.')+1:])
        
class Player:
    def __init__(self, name, position, player_id):
        self.name = name
        self.position = position
        self.player_id = player_id
        # self.team = team

    def __str__(self):
        return f"[{self.player_id}] {self.name}, {self.position}"