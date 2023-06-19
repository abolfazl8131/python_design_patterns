from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

#we use this pattern to calulate each laptop tax 
class Handler(ABC):

    @abstractmethod
    def set_next(self , next : Handler) -> Handler:pass

    @abstractmethod
    def handle(self , request : Any) -> Optional[str] : pass


class AbstractHandler(Handler):
    _next_handler:Handler = None

    def set_next(self, next: Handler) -> Handler:
        self._next_handler = next

        return next


    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# we difine each brand
class AsusHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == 'ROG':
            return f"{request}: tax = 20 %"
        elif request == 'Vivo':
            return f"{request} : tax = 10 %"
        else:
            return super().handle(request)


class AcerHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == 'Nitro5':
            return f"{request} : tax = 12 %"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
   

    for laptop_type in ["Nitro5" , "Imac" , "ROG" , "ZenBook"]:
        print(f"\n give me a tax of {laptop_type}?")
        result = handler.handle(laptop_type)
        if result:
            print(f" {result}", end="")
        else:
            print(f"  {laptop_type} doesnt have tax in our system.", end="")



if __name__ == "__main__":
    asus = AsusHandler()
    acer = AcerHandler()

    asus.set_next(acer)

    print("Chain: Asus > Acer")
    client_code(asus)
    print("\n")

   