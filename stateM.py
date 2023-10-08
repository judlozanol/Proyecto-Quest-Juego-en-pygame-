class StateM:
    def __init__(self,currentState):
        self.currentState=currentState
    def get_status(self):
        return self.currentState
    def set_status(self,status):
        self.currentState = status