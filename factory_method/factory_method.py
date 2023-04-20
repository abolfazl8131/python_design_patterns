
class Product:
    id:int
    name:str
    code:str
    price:str

    def create(self):
        return "object created"


class Book(Product):
    print_no:str

    def create(self , id , name , code , price , print_no)->None:
        self.id = id
        self.name = name
        self.code = code
        self.price = price
        self.print_no = print_no
        print('book created')

class Laptop(Product):
    size:str
    def create(self , id , name , code , price , size)->None:
        self.id = id
        self.name = name
        self.code = code
        self.price = price
        self.size = size
        print('laptop created')


class ProductFactory:
    _instance = None

    def get_instance(self):

        if self._instance is None:

            self._instance = ProductFactory()
            
            return self._instance
        else:
            return self._instance

    def get_product(self,product)->Product:

        if product =='laptop':
            return Laptop()

        if product =='book':
            return Book()

        return None

     
pf = ProductFactory().get_instance()

lap1 = pf.get_product('laptop')
lap1.create(1 , 'acer' , 'ythy54' , '22000000', ' 16')

book1 = pf.get_product('book')
book1.create(2 , 'clrs' , '645677uth' , '500000' , '10')
