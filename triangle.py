class Triangle:
    def __init__(self,a, b, z):
        self.a = a
        self.b = b
        self.z = z
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getZ(self):
        return self.z
class Circle:
    def __init__(self,r):
        self.r = r
    def getR(self):
        return self.r

class Rectangle:
    def __init__(self,width , height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


