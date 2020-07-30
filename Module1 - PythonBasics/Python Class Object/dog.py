class Dog:
    '''
    A simple attempt to model a dog
    '''
    
    def __init__(self, name = 'Billy', age = 10):
        '''initialize name and age attributes'''
        self.name = name
        self.age = age
    
    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        return '{} is sitting'.format(self.name)
    
    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        return '{} is rolling over'.format(self.name)