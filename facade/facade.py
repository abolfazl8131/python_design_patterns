
class Product:
    id:int
    name:str
    code:str
    price:str

    def create(self):
        pass


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


class ProductMaker:
   
    laptop = None
    book = None

    def __init__(self) -> None:
       self.laptop = Laptop()
       self.book = Book()

    def create_laptop(self , id , name , code , price , size):
        self.laptop.create(id , name, code, price, size)

    def create_book(self , id , name , code , price , print_no):
        self.book.create(id , name, code, price, print_no)
    


     
pm = ProductMaker()


pm.create_laptop(1 , 'acer' , 'ythy54' , '22000000', ' 16')


pm.create_book(2 , 'clrs' , '645677uth' , '500000' , '10')
