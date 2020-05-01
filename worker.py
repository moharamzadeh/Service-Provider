class worker:
    nWork = []

    def __init__ (self, name, work = None, workList = set()):
        self.name = name
        self.workList = workList
        self.workList.add (work)
        self.workList.discard (None)
        # worker.nWork.update (self.workList)
        personWork = [self.name, self.workList]
        worker.nWork.append(personWork)

    def addWork (self, work = None, workList = set()):
        self.workList.update (workList)
        self.workList.add (work)
        self.workList.discard (None)
        # worker.nWork.update (self.workList)
        for i in worker.nWork:
            if i[1] == self.name:
                i[2].update(self.workList)