import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


class PreProcessing(pd.DataFrame):
    ''' Write the docstring '''

    def __init__(self, df):
        super(PreProcessing, self).__init__()
        ''' Write the docstring'''
        self.df = df.copy()
        #self.cat = pd.Categorical(self.df)

    def get_categorical(self):
        '''Doc string'''
        #target_col = ['Churn']
        self.cat_cols = self.df.nunique()[self.df.nunique() < 6].keys().tolist() # getting
        #self.cat_cols = [x for x in self.cat_cols if x not in target_col]
        self.num_cols = [x for x in self.df.columns if x not in self.cat_cols]
        self.bin_cols = self.df.nunique()[self.df.nunique() == 2].keys().tolist()
        self.multi_cols = [x for x in self.cat_cols if x not in self.bin_cols]
        return self.multi_cols, self.bin_cols


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

    def Encode_OHE(self):
        '''Doc string'''
        self.get_categorical()
        self.Label_Encoder()
        self.OHE()
        return self.return_df()
    
    
class Embedding:
    
    def __init__(self, lis, n_dim, column_name):
        self.lis = lis
        self.n_dim = n_dim
        self.le = LabelEncoder()
        self.column_name = column_name
        self.sc = StandardScaler()
        
    def create(self):
        encode = self.le.fit(self.lis)
        keys = encode.classes_.tolist()
        values = sorted(encode.transform(keys).tolist())
        lis_dict = dict(zip(keys, values))
        embeds = nn.Embedding(len(keys), self.n_dim)
        
        columns = []
        for i in range(self.n_dim):
            columns.append('{}{}{}'.format(self.column_name,'_', str(i)))
            
        df = pd.DataFrame()  
        df_dict = {}
        for key in self.lis:
            x = embeds(torch.tensor([lis_dict[key]], dtype=torch.long)).detach().numpy().tolist()
            for i in range(self.n_dim):
                df_dict[columns[i]] = x[0][i]
            df = df.append(df_dict, ignore_index = True)
            #df = self.sc.fit_transform(df)

        return df