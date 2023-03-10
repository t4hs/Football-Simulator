from team import Team
from fileReader import *
from league import League


teamList = readTeamInfo("epl.txt")
teamObjects = createTeamObjects(teamList)
epl = League(teamObjects)
epl.addGame()
epl.orderLeague()
epl.drawTable()

