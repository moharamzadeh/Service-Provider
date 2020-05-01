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
            if self.person[1].get(work) == None:
                self.person[1][work] = 0
        
        self.updateNWork()

    def changeSalary (self, work, change = 0):
        if self.person[1].get(work) != None:
            self.person[1][work] += change
            self.updateNWork()
        

    def updateNWork (self):
        for person in worker.nWork:
            if person[0] == self.person[0]:
                person[1].update(self.person[1])
                break