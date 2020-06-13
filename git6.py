class iostring():
    def __init__ (self):
        pass
    def getstriing (self):
        self.s = input('enter a string: ')
        print(self.s)
    def upperstring (self):
        self.a = self.s.upper()
        print(self.a)

b = iostring()
b.getstriing()
b.upperstring()