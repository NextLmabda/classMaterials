import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


class PreProcessing(pd.DataFrame):
    ''' Write the docstring '''

    def __init__(self, df):
        super(PreProcessing, self).__init__()
        ''' Write the docstring'''
        self.df = df
        #self.cat = pd.Categorical(self.df)

    def get_categorical(self):
        '''Doc string'''
        target_col = ['Churn']
        self.cat_cols = self.df.nunique()[self.df.nunique() < 6].keys().tolist() # getting
        self.cat_cols = [x for x in self.cat_cols if x not in target_col]
        self.num_cols = [x for x in self.df.columns if x not in self.cat_cols + target_col]
        self.bin_cols = self.df.nunique()[self.df.nunique() == 2].keys().tolist()
        self.multi_cols = [x for x in self.cat_cols if x not in self.bin_cols]


    def Label_Encoder(self):
        le = LabelEncoder()
        #print(le.fit_transform(self.df['Gender']))
        for col in self.multi_cols:
            self.df[col] = le.fit_transform(self.df[col])

    def OHE(self):
        ''' Docstring'''
        self.df = pd.get_dummies(self.df, columns = self.bin_cols)

    def return_df(self):
        return self.df

    def LabelEncode_OHE(self):
        '''Doc string'''
        self.get_categorical()
        self.Label_Encoder()
        self.OHE()
        return self.return_df()



