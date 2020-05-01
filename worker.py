class worker:
    nWork = []

    def __init__ (self, name, workList = {}):
        self.name = name
        self.workList = dict()
        for work in workList:
            self.workList[work] = 0
        
        person = [self.name, self.workList]
        worker.nWork.append(person)

    def addWork (self, workList = {}):
        for work in workList:
            self.workList[work] = 0
        
        for person in worker.nWork:
            if person[1] == self.name:
                person[2].update(self.workList)