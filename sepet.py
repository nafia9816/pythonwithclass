class sepet:
    
    def __init__(self,id,musteri_id,durum,tutar):
         if id is None:
            self.id=0
        else:
            self.id=id

        self.musteri_id=musteri_id
        self.durum=durum
        self.tutar=tutar

#modeller içinde eklenecek verilerin konreolu yapılabilir. kac karakter olması gerektini mesela
