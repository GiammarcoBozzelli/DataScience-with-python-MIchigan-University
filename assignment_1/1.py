import pandas
import pandas as pd
import numpy as np


def answer_one():
    Energy = pd.read_excel(r'C:\Users\giamm\PycharmProjects\pythonProject1\Energy Indicators.xls',
                           skiprows = 18,header=None,na_values=["..."], usecols=[2,3,4,5], skipfooter=38)
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","",regex = True)
    Energy['Country'] = Energy['Country'].str.replace(r"\d*","",regex = True)
    Energy['Country'].replace({'Republic of Korea': 'South Korea',
                               "United States of America": "United States",
                               "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                               "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace=True)

    Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000

    GDP = pd.read_csv(r'C:\Users\giamm\PycharmProjects\pythonProject1\world_bank.csv',
                      skiprows=4,
                      usecols=['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
                               '2015'])
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    GDP['Country'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}, inplace=True)

    ScimEn = pd.read_excel(r'C:\Users\giamm\PycharmProjects\pythonProject1\scimagojr-3.xlsx')

    merge1 = pd.merge(ScimEn, Energy, how="inner", left_on="Country", right_on="Country")
    merge1 = merge1[merge1["Rank"] <= 15]
    merged_data = pd.merge(merge1, GDP, how="inner", left_on="Country", right_on="Country").set_index("Country")

    return merged_data

ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}


def answer_ten():
    merged_data = answer_one()

    merged_data.sort_values('% Renewable', ascending=False, inplace=True)
    median = merged_data.iloc[:15, ]['% Renewable'].median()
    merged_data['new'] = np.where(merged_data['% Renewable'] < median, 0, 1)
    merged_data.sort_values('Rank', ascending=True, inplace=True)
    HighRenew = merged_data['new'].copy()

    return HighRenew


def answer_nine():
    merged_data = answer_one()

    merged_data['population'] = merged_data['Energy Supply'] / merged_data['Energy Supply per Capita']
    merged_data.sort_values('population', ascending=False, inplace=True)
    merged_data['cit per person'] = merged_data['Citable documents'] / merged_data['population']

    x = merged_data['cit per person'].corr(merged_data['Energy Supply per Capita'], method='pearson')

    return x

def answer_eight():
    merged_data= answer_one()
    merged_data['population'] = merged_data['Energy Supply'] / merged_data['Energy Supply per Capita']
    merged_data.sort_values('population',ascending = False, inplace = True)
    return merged_data.index[2]


def answer_seven():
    merged_data = answer_one()
    merged_data['ratio'] = merged_data["Self-citations"] / merged_data['Citations']
    merged_data.sort_values('ratio', ascending=False, inplace=True)

    return (merged_data.index[0], merged_data['ratio'].max())

def answer_six():
    merged_data= answer_one()
    merged_data.sort_values('% Renewable', ascending = False, inplace = True)
    return (merged_data.index[0], merged_data['% Renewable'].max())
def answer_five():
    merged_data= answer_one()

    return merged_data['Energy Supply per Capita'].mean()

def answer_four():
    merged_data= answer_one()
    merged_data['avgGDP'] = (merged_data.loc[: , "2006":"2015"]).mean(axis=1)
    merged_data.sort_values('avgGDP', ascending=False, inplace = True)
    return abs(merged_data['2006'][5]-merged_data['2015'][5])
def answer_three():
    merged_data= answer_one()
    col = merged_data.loc[: , "2006":"2015"]
    avgGDP = pd.Series(col.mean(axis=1).sort_values(ascending=False)[:15])
    return avgGDP
def answer_two():
    Energy = pd.read_excel(r'C:\Users\giamm\PycharmProjects\pythonProject1\Energy Indicators.xls',
                           skiprows = 18,header=None,na_values=["..."], usecols=[2,3,4,5], skipfooter=38)
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","",regex = True)
    Energy['Country'] = Energy['Country'].str.replace(r"\d*","",regex = True)
    Energy['Country'].replace({'Republic of Korea': 'South Korea',
                               "United States of America": "United States",
                               "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                               "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace=True)

    Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000

    GDP = pd.read_csv(r'C:\Users\giamm\PycharmProjects\pythonProject1\world_bank.csv',
                      skiprows=4,
                      usecols=['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014','2015'])
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    GDP['Country'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}, inplace=True)

    ScimEn = pd.read_excel(r'C:\Users\giamm\PycharmProjects\pythonProject1\scimagojr-3.xlsx')

    inner1 = pd.merge(ScimEn,Energy,how="inner",left_on="Country",right_on="Country")
    inner2 = pd.merge(inner1,GDP,how="inner",left_on="Country",right_on="Country").set_index("Country")

    outer1 = pd.merge(ScimEn,Energy,how="outer",left_on="Country",right_on="Country")
    outer2 = pd.merge(outer1,GDP,how="outer",left_on="Country",right_on="Country").set_index("Country")

    return len(outer2)-len(inner2)
def answer_two_c():
    # YOUR CODE HERE
    # raise NotImplementedError()
    Energy = pd.read_excel(r'C:\Users\giamm\PycharmProjects\pythonProject1\Energy Indicators.xls',na_values=["..."],header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x*1000000)

    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
    Energy['Country'] = Energy['Country'].str.replace(r"\d*","")
    Energy['Country'] = Energy['Country'].replace({'Republic of Korea' : 'South Korea',
                                               'United States of America' : 'United States',
                                               'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                               'China, Hong Kong Special Administrative Region':'Hong Kong'})

    GDP = pd.read_csv(r'C:\Users\giamm\PycharmProjects\pythonProject1\world_bank.csv', skiprows = 4)
    GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.': 'South Korea',
                                                       'Iran, Islamic Rep.': 'Iran',
                                                       'Hong Kong SAR, China' : 'Hong Kong'})

    ScimEn = pd.read_excel(r'C:\Users\giamm\PycharmProjects\pythonProject1\scimagojr-3.xlsx')

    inner1 = pd.merge(ScimEn,Energy,how="inner",left_on="Country",right_on="Country")

    GDP.rename(columns = {"Country Name":"Country"},inplace=True)
    GDP = GDP.loc[:,['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',"Country"]]
    inner2 = pd.merge(inner1,GDP,how="inner",left_on="Country",right_on="Country").set_index("Country")

    outer1 = pd.merge(ScimEn,Energy,how="outer",left_on="Country",right_on="Country")
    outer2 = pd.merge(outer1,GDP,how="outer",left_on="Country",right_on="Country").set_index("Country")

    return len(outer2)-len(inner2)

def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    merged_data = answer_one()
    merged_data['continent'] = pd.Series(ContinentDict)
    merged_data['% Renewable']=pd.cut(merged_data['% Renewable'],5)
    return(merged_data.groupby(['continent','% Renewable'])['continent'].agg(np.size).dropna())

def answer_eleven():
    merged_data = answer_one()
    merged_data['population'] = merged_data['Energy Supply'] / merged_data['Energy Supply per Capita']
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    merged_data = answer_one()
    merged_data['population'] = merged_data['Energy Supply'] * merged_data['Energy Supply per Capita']
    merged_data['continent'] = pd.Series(ContinentDict)
    return merged_data.groupby('continent')['population'].agg([np.size, np.sum, np.mean, np.std])

print(answer_eleven())
