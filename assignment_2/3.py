'''It would be interesting to see if there is any evidence of a link
between vaccine effectiveness and sex of the child.
Calculate the ratio of the number of children who contracted chickenpox but
were vaccinated against it (at least one varicella dose) versus those who were
vaccinated but did not contract chicken pox. Return results by sex.

*This function should return a dictionary in the form of (use the correct numbers):*
```
    {"male":0.2,
    "female":0.4}
```

Note: To aid in verification, the `chickenpox_by_sex()['female']`
value the autograder is looking for starts with the digits `0.0077`.'''
import pandas as pd
def chickenpox_by_sex():
    df = pd.read_csv('/home/big_g/Downloads/NISPUF17.csv')
    data = df.loc[:, ['SEQNUMC', 'HAD_CPOX', 'SEX', 'P_NUMVRC']]

    male_vac = data[(data['P_NUMVRC'] > 0) & (data['HAD_CPOX'] == 1) & (data['SEX'] == 1)]
    male_not = data[(data['P_NUMVRC'] > 0) & (data['HAD_CPOX'] == 2) & (data['SEX'] == 1)]
    female_vac = data[(data['P_NUMVRC'] > 0) & (data['HAD_CPOX'] == 1) & (data['SEX'] == 2)]
    female_not = data[(data['P_NUMVRC'] > 0) & (data['HAD_CPOX'] == 2) & (data['SEX'] == 2)]
    return({'male':len(male_vac)/len(male_not),'female':len(female_vac)/len(female_not)})


print(chickenpox_by_sex())