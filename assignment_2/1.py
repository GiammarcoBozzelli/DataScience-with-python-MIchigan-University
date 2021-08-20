
# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a
# mother with the education levels equal to less than high school (<12), high school (12), more than high school but
# not a college graduate (>12) and college degree.
import pandas as pd

def proportion_of_education():
    df = pd.read_csv('/home/big_g/Downloads/NISPUF17.csv')
    data = df.loc[:,['SEQNUMC','EDUC1']]
    number = len(df)
    less = len(data[(data['EDUC1'] == 1)].dropna())/number
    high = len(data[(data['EDUC1'] == 2)].dropna())/number
    not_college = len(data[(data['EDUC1'] == 3)].dropna())/number
    college = len(data[(data['EDUC1'] == 4)].dropna())/number
    dictionary = {"less than high school": less,
              "high school": high,
              "more than high school but not college":not_college,
              "college":college}
    return(dictionary)

print(proportion_of_education())

assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
