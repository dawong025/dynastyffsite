class Roster:
    def __init__(self, name, team_key, roster):
        self.name = name
        self.team_key = team_key
        self.roster = roster

    def __str__(self):
        return f"{self.name} - {self.team_key}\n {self.roster}"
    