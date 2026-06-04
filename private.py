class Myclass:
    
    __privatevar = 27
    
    def __privMeth(self):
        print("I'm  inside class myClass")
        
    def hello(self):
        print("Private Variable value: ", Myclass.__privatevar)
        
        
foo = Myclass()
foo.hello()
foo.__privMeth()