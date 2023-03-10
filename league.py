from team import Team

class League:

    def __init__(self, teams):
        self.table = []
        #ensure a list has been passed in
        if isinstance(teams, list):
            for team in teams:
                #ensure list contains only teams
                if isinstance(team, Team):
                    self.table.append(team)
                else:
                    print("Error: item in list is not a team")
        else:
            print("Error, input a list of teams")

    def orderLeague(self):
        self.table.sort(key=lambda x: x.results["points"], reverse=True)

    def promoteTeam(self, team):
        #add a new team to a league
        if isinstance(team, Team):
            self.table.append(team)
        else:
            print("Enter valid team")

    def relegateTeam(self):
        #drop lowest ranking team
        self.orderLeague()
        self.table.pop()

    def drawTable(self):
        #output table headers
        print('{:^25} {:^5} {:^5} {:^5}{:^5}{:^5}{:^5}{:^5}{:^5}'.format('club', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'))
        print("--------------------------------------------------------------------")
        #output team results line by line
        for team in self.table:
            resultsList = list(team.results.values())
            print('{:^25} {:^5} {:^5} {:^5}{:^5}{:^5}{:^5}{:^5}{:^5}'.format(team.name, resultsList[0], resultsList[1], resultsList[2], resultsList[3], resultsList[5], resultsList[6], resultsList[7], resultsList[4]))

    def addGame(self):
        team1check = False
        team2check = False
        team1 = input("Input home team\n")
        team2 = input("Input away team\n")
        score1 = int(input("Input home team goals\n"))
        score2 = int(input("Input home team goals\n"))
        #check both teams are part of the league
        for team in self.table:
            if team1 == team.name:
                team1 = team
                team1check = True
            elif team2 == team.name:
                team2 = team
                team2check = True
        #update teams results
        if team1check & team2check:
            team1.updateResults(score1, score2)
            team2.updateResults(score2, score1)
        else:
            print("Error team is not part of this league")

