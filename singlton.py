

class DB:
    _instance = None

    def connection(self ):
        return "connected!"

    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.connection()
            return cls._instance
        return cls._instance

DB().get_instance()