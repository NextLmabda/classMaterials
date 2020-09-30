class Square:
    '''This Class .........'''

    def __init__(self):
        print('I will execute the init method first')

    def Square(self, num = None):
        self.num = num
        return self.num ** 2

class Cube:
       
    def __Kunle__(self):
        print('My name is Kunle')

    def CUbe(self):
        self.num = num
        return self.num ** 3
    
class Jump:
    
    def __init__(self, name = None):
        self.name = name
        
    def fit(self):
        self.reverse = lambda name: name[: : -1]
    
    def transform(self):
        return self.reverse(self.name)
    
    def fit_transform(self):
        self.fit()
        return self.transform()