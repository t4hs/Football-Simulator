from team import Team

def readTeamInfo(filename):
    teamInfo = []
    try:
        with open(filename, 'r') as file:
            #read file line by line
            for line in file:
                #split the name from the rest of the data
                parts = line.strip().split(': ')
                name = parts[0]
                #split the stadium and city
                stadium, city = parts[1].split(' - ')
                teamInfo.append([name, stadium, city])
    except:
        #check for error caused by empty lines
        if line == "\n":
            print("empty line skipped")
    return teamInfo

#create a list of Team objects
def createTeamObjects(teamList):
    teams = []
    for teamData in teamList:
        name, stadium, city = teamData
        team = Team(name, stadium, city)
        teams.append(team)
    return teams
