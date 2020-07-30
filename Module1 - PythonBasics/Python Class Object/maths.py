class Maths:
    def square(x):
        return x ** 2
    
    def Factorial(n):
        '''
        The function takes integer n and returns the factorial of n
        Example: 4 factorial is 4 * 3 * 2 * 1 = 24
        n can not be negative
        '''
        if n < 0:
            return 'factorial of negative number is impossible'
        elif n == 0 or n == 1:
            return 1
        else:
            return n * Factorial(n - 1)

class Ebony:
    def cube(x):
        return x ** 3