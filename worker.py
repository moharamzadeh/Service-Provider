class worker:
    nWork = []

    def __init__ (self, name, workList = {}):
        tempWork = dict()
        for work in workList:
            tempWork[work] = 0
        
        self.person = [name, tempWork]
        worker.nWork.append(self.person)

    def addWork (self, workList = {}):
        for work in workList:
            self.person[1][work] = 0
        
        for person in worker.nWork:
            if person[0] == self.person[0]:
                person[1].update(self.person[1])

    def changeSalary (self, work, change = 0):
        pass

    def updateNWork (self):
        pass