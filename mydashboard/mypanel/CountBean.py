class CountBean:
    """
    CountBean class represents the count data
    """
 
    def __init__(self, id , sig_priority  , timestamp):
        self.id = id
        self.sig_priority = sig_priority
        self.timestamp = timestamp 


class CountBean2:
    """
    CountBean2 class represents the count data
    """

    def __init__(self,id ,ip_src, count):
        self.id = id
        self.ip_src = ip_src
        self.count = count

class CountBean3:
    """
    CountBean2 class represents the count data
    """

    def __init__(self, id , TCount):
        self.id = id
        self.TCount = TCount
