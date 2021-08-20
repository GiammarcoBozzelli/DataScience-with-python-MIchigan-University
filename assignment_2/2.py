'''
Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza
vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children
 we know received breastmilk as a child and those who know did not.
'''
import pandas as pd

def proportion_of_education():
    df = pd.read_csv('/home/big_g/Downloads/NISPUF17.csv')
    data = df.loc[:,['SEQNUMC','CBF_01','P_NUMFLU']]

    breast = data[data['CBF_01'] == 1]
    not_breast= data[data['CBF_01']== 2]
    y = breast['P_NUMFLU'].dropna().mean()
    n = not_breast['P_NUMFLU'].dropna().mean()
    return(y,n)


print(proportion_of_education())