class musteriler:
    def __init__(self,id,numara,referans_no,ad,soyad,email,ulke_id,ulke_il_id,ulke_ilce_id,kayit_tarihi):
        if id is None:
            self.id=0
        else:
            self.id=id
        
        self.numara=numara
        self.referans_no=referans_no
        self.ad=ad
        self.soyad=soyad
        self.email=email
        self.ulke_id=ulke_id
        self.ulke_il_id=ulke_il_id
        self.ulke_ilce_id=ulke_ilce_id
        self.kayit_tarihi=kayit_tarihi
        
        
        
        
        
        
        