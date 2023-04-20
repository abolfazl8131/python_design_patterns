
class Redis:
    _instance = None

    def connect(self):
        self._instance = Redis()
        print('connected')

    def get_instance(cls):
        if cls._instance == None:
            cls.connect()
            return cls._instance
        return cls._instance



def cache_1():
    r = Redis().get_instance()
    print('cached 1')


def cache_2():
    r = Redis().get_instance()
    print('cached 2')


def cache_3():
    r = Redis().get_instance()
    print('cached 3')


cache_1()
cache_2()
cache_3()