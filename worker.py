class worker:
    nWork = []

    def __init__ (self, name, work = None, workList = set()):
        self.name = name
        self.workList = workList
        self.workList.add (work)
        self.workList.discard (None)
        personWork = [self.name, self.workList]
        worker.nWork.append(personWork)

    def addWork (self, work = None, workList = set()):
        self.workList.update (workList)
        self.workList.add (work)
        self.workList.discard (None)
        for person in worker.nWork:
            if person[1] == self.name:
                person[2].update(self.workList)