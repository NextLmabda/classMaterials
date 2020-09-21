import numpy as np

class StandardScaler(object):
    '''Implement standard scaling ((x - mean) / std) scaling.'''
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, x):
        self.mean = x.mean()
        self.std = x.std()
    
    def transform(self, x):
        result = x.astype(float)
        result -= self.mean
        result /= self.std
        return result

    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)

class NormalizationScaler(object):
    '''Implement normalization scaling ((x - minValue) / (maxValue - minValue)) scaling.'''
    def __init__(self):
        self.minValue = None
        self.maxValue = None 

    def fit(self, x):
        self.maxValue = max(x)
        self.minValue = min(x)

    def transform(self, x):
        range = self.maxValue - self.minValue
        result = x.astype(float)
        result -= self.minValue
        result /= range
        return result


class make_model:
    '''Create a column for the make and model and return a new dataframe'''
    
    def __init__(self, dataframe):
        self.df = dataframe

    def fit(self, row):
        self.ls = row['CarName'].split()
        self.make = self.ls[0]

        def model(x):
            x.pop(0)
            modelName = ' '.join(x)
            return modelName
        self.model = model(self.ls)
        return self.make, self.model

    def transform(self):
        self.df.apply(self.fit)        

        return self.df