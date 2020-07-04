
class urunler:
    def __init__(self,id,ad,barkod,fiyat,puan):
        if id is None:
            self.id=0
        else:
            self.id=id

        self.ad=ad
        self.barkod=barkod
        self.fiyat=fiyat
        self.puan=puan

