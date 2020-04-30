class worker:
    nWork = set()

    def __init__ (self, name, work = None, workList = set()):
        self.name = name
        self.workList = workList
        self.workList.add (work)
        self.workList.discard (None)
        worker.nWork.update (self.workList)

    def addWork (self, work = None, workList = set()):
        self.workList.update (workList)
        self.workList.add (work)
        self.workList.discard (None)
        worker.nWork.update (self.workList)