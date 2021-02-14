import numpy as np
import pandas as pd

df = pd.read_csv('user_movie_rating.csv',header = None,index_col = False)
A = np.array(df).T

def split_data(i):
    start = int((i) * len(A)/5)
    end = int((i+1) * len(A)/5)

    train = np.concatenate((A[:start],A[end:]),axis = 0)
    test = A[start:end]

    return train,test