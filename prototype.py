from abc import abstractmethod , ABCMeta
import copy

class Product(metaclass = ABCMeta):
    def __init__(self) -> None:
        self.id = None
        self.name = None

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id
    
    def set_id(self , id):
        self.id = id


    @abstractmethod
    def product(self):
        pass


    def set_name(self , name):
        self.name = name

    def clone(self):
        return copy.copy(self)

    
class Laptop(Product):
    def __init__(self) -> None:
        
        super().__init__()
        
        

    def product(self):
        print('this is laptop')


class Lamp(Product):

    def __init__(self) -> None:
        
        super().__init__()
        

    def product(self):
        print('this is lamp')



class ProductCache:
    cache = {}

    @staticmethod
    def get_product(id):
        PRODUCT = ProductCache.cache.get(id , None)
        return PRODUCT.clone()

    @staticmethod
    def set_product(key , data):
        if key == 'lamp':
            l = Lamp()
            l.set_id(data['id'])
            l.set_name(data['name'])
            ProductCache.cache[l.get_id()] = l
            

        if key == 'laptop':
            l = Laptop()
            l.set_id(data['id'])
            l.set_name(data['name'])
            ProductCache.cache[l.get_id()] = l





    
