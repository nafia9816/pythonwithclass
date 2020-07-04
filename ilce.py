class ilce:
    
    def __init__(self,id,name,state_id):
         if id is None:
            self.id=0
        else:
            self.id=id

        self.name=name
        self.state_id=state_id

