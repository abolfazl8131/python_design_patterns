from abc import ABC, abstractmethod

class AbstractSMSService(ABC):

    @abstractmethod
    def send(self) -> None:
       pass


class Service1(AbstractSMSService):
    
    
    def send(self) ->None:
        print('service 1 sms sent')
        


class Service2(AbstractSMSService):
    
    def send(self) -> None:
        print('service 2 sms sent')
        



class SMSFactory:

    def get_service(self , service_name) -> AbstractSMSService:
        if service_name == 'service1':
            return Service1()
        
        elif service_name == 'service2':
            return Service2()
        
        return None
       
        

        
factory = SMSFactory()

service1 = factory.get_service('service1')
print(service1.send())

service2 = factory.get_service('service2')
print(service2.send())
