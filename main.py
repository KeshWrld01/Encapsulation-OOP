class point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
p1 = point(2,3)
print(p1)


class myclass:
    __privateattribute = 25

    def __privatemeth(self):
        print("I am inside the class myclass")
    
    def hello(self):
        print("Private variable is: ", myclass.__privateattribute)

ob1  = myclass()
ob1.hello()
ob1.__privatemeth

