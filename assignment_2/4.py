def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    # this is just an example dataframe
    df = pd.read_csv('/home/big_g/Downloads/NISPUF17.csv')
    dat = df.loc[:, ['HAD_CPOX','P_NUMVRC']]
    data = dat[(dat['HAD_CPOX'] == 1) | (dat['HAD_CPOX'] == 2)].dropna()

    # here is some stub code to actually run the correlation
    corr, pval = stats.pearsonr(data["HAD_CPOX"], data["P_NUMVRC"])

    # just return the correlation
    return corr

print(corr_chickenpox())