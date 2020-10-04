import numpy as np
import pandas as pd
from maths import factorial as fact
#import maths


class Functions:

    def __init__(self, n, r):
        '''
        This method takes n and r

        n: integer
        r: integer
        '''
        self.n = n
        self.r = r
        assert self.n >= self.r, f'n must be greater than or equal to r'

    def Combination(self):
        '''
        This method performs formula

        returns:
            comb: int
        '''
        return self.Permutation() / fact(self.r)
        #return fact(self.n) / (fact(self.n - self.r) * fact(self.r))

    def Permutation(self):
        '''
        This method performs formula

        returns:
            perm: int
        '''
        return fact(self.n) / fact(self.n - self.r)


class Slice:

    def __init__(self, start, stop, steps, sent):
        self.sent = sent
        self.start = start
        self.stop = stop
        self.steps = steps

    def fit(self):
        self.cut = lambda sentence: sentence[self.start: self.stop: self.steps]

    def transform(self):
        return self.cut(self.sent)

    def fit_transform(self):
        self.fit()
        return self.transform()
    
