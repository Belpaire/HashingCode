class Picture:
    # True for horizontal orientation, false otherwise
    # id = unique number
    #nbtags should be equal to length tags
    #tags is a list of tags
    def __init__(self,id,ishorizontal,nbtags,tags):
        self.id = id
        self.ishorizontal = ishorizontal
        self.nbtags = nbtags
        self.tags = tags

