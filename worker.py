class worker:
    workList = {}
    
    def __init__ (self, name, work = None, workList = set()):
        self.name = name
        self.workList = workList
        self.workList.discard (None)
        workList.update (self.workList)

    def addWork (self, work = None, workList = set()):
        self.workList.update (workList)
        self.workList.add (work)
        self.workList.discard (None)