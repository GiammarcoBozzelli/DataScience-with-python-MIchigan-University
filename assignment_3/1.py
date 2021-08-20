import pandas as pd
import numpy as np
def ans():
    Energy = pd.read_excel(r'Energy_Indicators.xls',
                       header=16,usecols='C:F',skipfooter=38)
    Energy.drop(labels=0,axis=0, inplace=True)
    Energy.columns = ['Country','Energy Supply','Energy Supply per Capita', '% Renewable']

    Energy['Country'].replace({'\.\.\.':np.NaN,'Republic of Korea':'South Korea',
                    "United States of America": "United States",
                    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                    "China, Hong Kong Special Administrative Region": "Hong Kong",
                    '\(.*\)':'', '\d':''}, regex=True, inplace=True)

    Energy['Country'] = Energy['Country'].str.strip()

    Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000

    GDP = pd.read_csv(r"world_bank.csv",
                      header=4,
                      usecols=['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'])
    GDP.rename({'Country Name':'Country'},axis=1, inplace=True)
    GDP.replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran",
                 "Hong Kong SAR, China": "Hong Kong"}, inplace=True)

    ScimEn = pd.read_excel(r'scimagojr-3.xlsx')
    merged_data = GDP.merge(Energy, on = 'Country').merge(ScimEn,on='Country')
    merged_data.set_index('Country', inplace = True)
    merged_data.sort_values('Rank',inplace=True)
    merged_data.columns=['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
                         'Citations per document', 'H index', 'Energy Supply',
                         'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
                         '2009', '2010', '2011', '2012', '2013', '2014', '2015']



    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    group = list(merged_data.groupby(ContinentDict))
    print(group)
    merged_data['population'] = merged_data['Energy Supply'] * merged_data['Energy Supply per Capita']
    frame = pd.DataFrame(columns=['size', 'sum', 'mean', 'std'],index = ['Asia', 'Australia', 'Europe', 'North America', 'South America'])
    for group in frame:
        frame.loc[group] = [len(frame), merged_data['population'].sum(), frame['Estimate Population'].mean(),
                            frame['Estimate Population'].std()]
    return frame


print(ans())