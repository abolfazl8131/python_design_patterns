#interface
class IMath:
    def add(self,x,y):pass
    def sub(self,x,y):pass
    def mul(self,x,y):pass
    def div(self,x,y):pass


class Math(IMath):
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


class MathProxy(IMath):

    math = Math()

    def add(self, x, y):
        return self.math.add(x, y)

    def sub(self, x, y):
        return self.math.sub(x, y)

    def mul(self, x, y):
        return self.math.mul(x,y)

    def div(self, x, y):
        return self.math.div(x,y)


proxy = MathProxy()

print(proxy.add(3,7))
print(proxy.sub(9,4))
print(proxy.mul(5,6))
print(proxy.div(12,4))