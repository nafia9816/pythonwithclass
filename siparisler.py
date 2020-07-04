class siparisler:
    
    def __init__(self,id,musteri_id,sepet_id,urun_id,birim_fiyat,kdv,toplam_tutar,odeme_tipi):
         if id is None:
            self.id=0
        else:
            self.id=id

        self.musteri_id=musteri_id
        self.sepet_id=sepet_id
        self.urun_id=urun_id
        self.birim_fiyat=birim_fiyat
        self.kdv=kdv
        self.toplam_tutar=toplam_tutar
        self.odeme_tipi=odeme_tipi



