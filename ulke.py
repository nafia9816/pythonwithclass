class ulke:
    
    def __init__(self,id,sortname,name,phonecode):
         if id is None:
            self.id=0
        else:
            self.id=id

        self.sortname=sortname
        self.name=name
        self.phonecode=phonecode

