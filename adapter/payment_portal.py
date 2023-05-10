
class PaymentAdapter:
    def pay(self):
        pass



class SamanPortal:
    def do_payment(self , amount):
        print(str(amount)+" paid! (saman)")

class ShaparakPortal:
    def payment(self , amount):
        print(str(amount)+" paid! (shaparak)")



class SamanPortalAdapter(PaymentAdapter):

    def __init__(self,  saman:SamanPortal) -> None:
        self.portal = saman
        
    def pay(self , amount):
        self.portal.do_payment(amount)



class ShaparakPortalAdapter(PaymentAdapter):

    def __init__(self,  shaparak:ShaparakPortal) -> None:
        self.portal = shaparak
        
    def pay(self , amount):
        self.portal.payment(amount)



SamanPortalAdapter(SamanPortal()).pay(120000000)

ShaparakPortalAdapter(ShaparakPortal()).pay(15000)