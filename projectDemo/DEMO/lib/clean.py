import pandas as pd
import numpy as np

def clean_dataframe(df):
    '''
    This function changes the column name of a dataframe
    :param df:DataFrame to manipulate
    :return: DataFrame
    '''
    changedCol = []
    
    for col in df.columns:
        changedCol.append(col.capitalize())

    df.columns = changedCol

    # Remove the missing values from Totalcharges column
    #df['Totalcharges'] = df['Totalcharges'].replace(" ", np.nan)
    df = df.replace(" ", np.nan)
    #df = df[df['Totalcharges'].notnull()]
    df = df[df.notnull()]
    

    # Change the Totalcharges column to float type
    df = df.reset_index()[df.columns]
    df['Totalcharges'] = df['Totalcharges'].astype(float)

    # Replace the 'No Internet Service' to No
    column_to_replace = ['Onlinesecurity', 'Onlinebackup', 'Deviceprotection', 'Techsupport',
                         'Streamingtv', 'Streamingmovies']
    for col in column_to_replace:
        df[col] = df[col].replace({'No internet service': 'No'})

    # Convert 'SeniorCitizen' from o, 1 to Yes and No
    df['Seniorcitizen'] = df['Seniorcitizen'].replace({1: 'Yes', 0: 'No'})

    # Convert Churn from 'Yes/ NO' to 'Churn/Not Churn'
    # df['Churn'] = df['Churn'].replace({'No': 'Not Churn', 'Yes': 'Churn'})
    
    return df

def group_tenure(df):

    def transform(inp):
        if inp <= 12:
            return 'One_Year'
        elif inp <= 24:
            return 'Two_Year'
        elif inp <= 48:
            return 'Three_Year'
        elif inp <= 60:
            return 'Four_Year'
        else:
            return 'Five_Year'
    df['CreatedTenure'] = df['Tenure'].apply(transform)
    return df

