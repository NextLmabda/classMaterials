'''Writing a Function'''

def factorial(num = None):
    '''
    This function returns the factorial of a number
    '''
    #assert num >= 0, 'Can not find factorial of a negative number {}'.format(num)
    assert type(num) == int, f'{num} is not an integer'

    if num == 0 or num == 1:
        return 1
        
    elif num < 0:
        return 'Can not find factorial of a negative number {}'.format(num)
    else: 
        fact = num * factorial(num - 1)

    return fact


def square(num = 10):
    ''' 
    This function returns the square of a number
    '''
    return num ** 2
    
def Say(name):
    '''
    This function say the name of a person
    '''
    print(f'My name is {name}')


