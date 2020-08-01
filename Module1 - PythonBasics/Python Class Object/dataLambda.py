class DataLambda:
    # Class attribute
    primate = 'Human'
    
    def __init__(self, fname = 'Omolewa', lname = 'Davids', gender = 'Male'):
        self.firstName = fname
        self.lastName = lname
        self.fullName = fname + ' ' + lname
        self.gender = gender
        print('I am executing the init method')
        
    def jump(self):
        print('{} is jumping now'.format(self.fullName))
        
    def play(self, game):
        return '{1} is playing {0}'.format(self.fullName, game)
    
    def square(self, num):
        return self.firstName * num