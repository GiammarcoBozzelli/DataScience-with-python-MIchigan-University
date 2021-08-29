import pandas as pd
import numpy as np
import scipy.stats as stats
import re

pd.set_option('display.max_rows', 100)


def get_area(city):
    area = city.split()[0]

    # Some names need to be updated manually
    if area in ['New', 'Los', 'St.', 'San', 'Tampa', 'Oklahoma', 'Kansas']: area = area + ' ' + city.split()[1]
    if area == "Vegas": area = 'Las Vegas'
    if area in ["New Jersey", 'Brooklyn']: area = 'New York'
    if area in ["San Jose", 'Golden', 'Oakland']: area = 'San Francisco'
    if area == "Arizona": area = 'Phoenix'
    if area == "Florida": area = 'Miami'
    if area == "Anaheim": area = 'Los Angeles'
    if area == "Colorado": area = 'Denver'
    if area == "Carolina": area = 'Raleigh'
    if area == "Minnesota": area = 'Minneapolis'
    if area == "Utah": area = 'Salt Lake City'
    if area == "Indiana": area = 'Indianapolis'
    if area == "Texas": area = 'Dallas'
    return area


def get_city_area(city):
    # Some names need to be updated manually
    dct = {'New York City': 'New York',
           'San Francisco Bay Area': 'San Francisco',
           'Dallas–Fort Worth': 'Dallas',
           'Washington, D.C.': 'Washington',
           'Minneapolis–Saint Paul': 'Minneapolis',
           'Miami–Fort Lauderdale': 'Miami',
           'Tampa Bay Area': 'Tampa Bay'
           }
    return dct.get(city, city)


def mlb_correlation():
    mlb_df = pd.read_csv(r"C:\Users\giamm\PycharmProjects\pythonProject1\Assignment_4\mlb.csv")
    cities = pd.read_html(r"C:\Users\giamm\PycharmProjects\pythonProject1\Assignment_4\wikipedia.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    # load cities and get rid of [notes], __ values and white spaces
    cities = pd.read_html(r"C:\Users\giamm\PycharmProjects\pythonProject1\Assignment_4\wikipedia.html", na_values='—')[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    cities = cities.replace("\[.*\]", "", regex=True).replace(r'^\s*$', np.nan, regex=True).replace(r'—', np.nan,
                                                                                                    regex=True)
    cities.rename(columns={'Population (2016 est.)[8]': 'Population'}, inplace=True)
    cities = cities.astype({'Population': 'int64'})  # change to numeric type so the aggregation can be done
    cities['area'] = cities['Metropolitan area'].apply(get_city_area)  # adjuct the names
    cities.drop(['NFL', 'NBA', 'Metropolitan area', 'NHL', 'MLB'], inplace=True, axis=1)  # drop obsolete columns

    # load mlb, get rid of * in team names and drop "Divisions" lines, select just 2018 data
    mlb_df = pd.read_csv(r"C:\Users\giamm\PycharmProjects\pythonProject1\Assignment_4\mlb.csv")
    mlb_df = \
    mlb_df[mlb_df['year'] == 2018].replace("\(.*\)", "", regex=True).replace('\*', '', regex=True)[['team', 'W-L%']][
        ~mlb_df['team'].str.contains("Division")]
    mlb_df.rename(columns={'W-L%': 'ratio'}, inplace=True)
    mlb_df = mlb_df.astype({'ratio': 'float64'})  # change to numeric type so the aggregation can be done
    mlb_df['area'] = mlb_df['team'].apply(get_area)  # adjust the names

    df = pd.merge(cities, mlb_df, how='outer').dropna().groupby(['area']).agg({"Population": np.mean, "ratio": np.mean})

    population_by_region = df['Population']  # pass in metropolitan area population from cities
    win_loss_by_region = df[
        'ratio']  # pass in win/loss ratio from mlb_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


print(mlb_correlation())
