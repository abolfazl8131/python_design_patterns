from abc import abstractmethod , ABC


class AbstractFont(ABC):

    @abstractmethod
    def bold(self):pass




class VazirFont(AbstractFont):

    def bold(self):
        print('bold vazir')




class LalezarFont(AbstractFont):
    def bold(self):
        print('bold lalezar')



a = LalezarFont()
a.bold()

b = VazirFont()
b.bold()