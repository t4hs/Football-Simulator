class Team:

    def __init__(self, name, stadium, city):
        self.name = name
        self.stadium = stadium
        self.city = city
        self.results = dict(played=0, wins=0, draws=0, losses=0, points=0, goalsScored=0, goalsConceded=0,
                            goalDifference=0)
        self.manager = ""
        self.topGoalScorer = ""

    def setManager(self, managerName):
        if isinstance(managerName, str):
            self.manager = managerName

    def setTopGoalscorer(self, topGoalScorer):
        if isinstance(topGoalScorer, str):
            self.topGoalScorer = topGoalScorer

    def updateResults(self, goalsScored, goalsConceded):
        #ensure two integers wer passed in
        if isinstance(goalsScored, int) * isinstance(goalsConceded, int):
            self.results["played"] += 1
            #check if team won
            if goalsScored > goalsConceded:
                self.results["wins"] += 1
            #check if team lost
            elif goalsScored < goalsConceded:
                self.results["losses"] += 1
            #if they neither won nor lost they must have drew
            else:
                self.results["draws"] += 1
            self.results["goalsScored"] += goalsScored
            self.results["goalsConceded"] += goalsConceded
            self.results["goalDifference"] += goalsScored - goalsConceded
            self.results["points"] = self.results["wins"]*3 + self.results["draws"]
        else:
            print("Error: team scores must be numbers")