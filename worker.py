class worker:
    def __init__ (self, name, work = None, workList = {}):
        self.name = name
        self.workList = workList
        self.workList.discard(None)

    def addWork (self, work = None, workList = {}):
        self.workList.update(workList)
        self.workList.add(work)
        self.workList.discard(None)