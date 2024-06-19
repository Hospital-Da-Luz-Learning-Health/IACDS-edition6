import numpy as np
import pandas as pd

def preprocess_data(df):
    # for an explanation on why we cleaned/preprocessed the data in this way
    # please refer to the notebook data cleaning explained.ipynb

    column_mapping = {0:'Id',
                  1: "Clump Thickness", 
                  2: "Uniformity of Cell Size", 
                  3: "Uniformity of Cell Shape",
                  4: "Clump Marginal Adhesion",
                  5: "Single Epithelial Cell Size",
                  6: "Bare Nuclei",
                  7: "Bland Chromatin",
                  8: "Normal Nucleoli",
                  9: "Mitoses",
                  10: "Class"}
    
    df = df.rename(columns=column_mapping)
    df = df.set_index('Id')

    positions_with_interrogation_mark = df['Bare Nuclei'] == '?'
    df.loc[positions_with_interrogation_mark,'Bare Nuclei'] = np.nan
    df['Bare Nuclei'] = df['Bare Nuclei'].astype(float) # floats are numbers in python

    average_value = df['Bare Nuclei'].mean()
    df['Bare Nuclei'] = df['Bare Nuclei'].fillna(average_value) # fill nan values with the average value of Bare Nuclei from the whole dataset
    

    df["Class"] = df["Class"].replace({2:0, 4:1})

    return df