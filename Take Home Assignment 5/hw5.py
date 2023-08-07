'''
Ashwika Sharma
Section AC
This file helps visualize the food deserts and census tracts where there
is low food access. This plots a variety of maps with the shapes of the
census tracts and counties, highlighting low food access based on income
and location. This is done using a dataset comprising of a food access
dataset and the 2010 census, merged by a method in this file.
'''
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(shp_file_name: str, csv_file_name: str) -> gpd.GeoDataFrame:
    '''
    Takes in the string filenames of the census dataset and the food access
    dataset. The function returns a GeoDataFrame that merges the two datasets
    based on their Census Tract Indentifier.
    '''
    census_data = gpd.read_file(shp_file_name)
    food_data = pd.read_csv(csv_file_name)
    merged = census_data.merge(food_data, left_on='CTIDFP00',
                               right_on='CensusTract', how='left')
    return merged


def percentage_food_data(state_data: gpd.GeoDataFrame) -> float:
    '''
    Takes in the merged data GeoDataFrame state_data and returns the float
    value of the percentage of census tracts in Washington that we have
    food access data for.
    '''
    total_tracts = state_data['CensusTract'].count()
    food_tracts = state_data['CTIDFP00'].count()
    if (total_tracts == 0):
        return 0
    return (total_tracts / food_tracts * 100)


def plot_map(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes in the merged data GeoDataFrame state_data and plots the shapes
    of all the Washington census tracts. This is stored in the file map.png
    Returns None.
    '''
    state_data.plot()
    plt.title("Washington State")
    plt.savefig('map.png')


def plot_population_map(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes in the merged data GeoDataFrame state_data and plots the shapes
    of all of the Washington census tracts. Each tract is colored according
    to their population. The plot also includes a legend that shows the
    meaning of the colorings. This is stored in population_map.png.
    Returns None.
    '''
    fig, ax = plt.subplots(1)
    state_data.plot(ax=ax, color='#EEEEEE', legend=True)
    state_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title("Washington Census Tract Populations")
    plt.savefig('population_map.png')


def plot_population_county_map(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes in the merged data GeoDataFrame state_data and plots the
    shapes of the census tracts. Each county is colored according to
    its population. There is also a legend which shows the meaning of
    the colorings. This is stored in county_population_map.png. Returns
    None.
    '''
    fig, ax = plt.subplots(1)
    state_data = state_data[['County', 'geometry', 'POP2010']]
    county_population = state_data.dissolve(by='County', aggfunc='sum')
    state_data.plot(ax=ax, color='#EEEEEE', legend=True)
    county_population.plot(ax=ax, column='POP2010', legend=True)
    plt.title("Washington County Populations")
    plt.savefig("county_population_map.png")


def plot_food_access_by_county(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes in the merged data GeoDataFrame and plots four plots on one
    figure, stored as county_food_access.png which shows information
    on food access across income level. The first plot colors the tracts
    based on the ratio of people who have low access in a half mile radius.
    The second plot colors the tracts based on the ratio of people who have
    low access and low income in a half mile radius. The third shows tracts
    based on the ratio of people with low access in a 10 mile radius, and
    the fourth is based on the ratio of people with low access and low income
    in a 10 mile radius. Returns None.
    '''
    state_data = state_data[['County', 'geometry', 'POP2010',
                            'lapophalf', 'lapop10', 'lalowihalf', 'lalowi10']]
    county_population = state_data.dissolve(by='County', aggfunc='sum')
    county_population['lapophalf_ratio'] = county_population['lapophalf'] \
        / county_population['POP2010']
    county_population['lapop10_ratio'] = county_population['lapop10'] \
        / county_population['POP2010']
    county_population['lalowihalf_ratio'] = county_population['lalowihalf'] \
        / county_population['POP2010']
    county_population['lalowi10_ratio'] = county_population['lalowi10']\
        / county_population['POP2010']
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    state_data.plot(ax=ax1, color='#EEEEEE')

    county_population.plot(ax=ax1, column='lapophalf_ratio',
                           legend=True, vmin=0, vmax=1)
    ax1.set_title('Low Access: Half')
    state_data.plot(ax=ax2, color='#EEEEEE', legend=True)
    county_population.plot(ax=ax2, column='lalowihalf_ratio',
                           legend=True, vmin=0, vmax=1)
    ax2.set_title('Low Access + Low Income: Half')
    state_data.plot(ax=ax3, color='#EEEEEE', legend=True)
    county_population.plot(ax=ax3, column='lapop10_ratio',
                           legend=True, vmin=0, vmax=1)
    ax3.set_title('Low Access: 10')
    state_data.plot(ax=ax4, color='#EEEEEE', legend=True)
    county_population.plot(ax=ax4, column='lalowi10_ratio',
                           legend=True, vmin=0, vmax=1)
    ax4.set_title('Low Access + Low Income: 10')

    plt.savefig("county_food_access.png")


def plot_low_access_tracts(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes in the merged data GeoDataFrame and makes a plot of
    all low access census tracts, stored in low_access.png. A plot
    is considered low access if it is urban and at least 500 people
    or 33% of people are more than half a mile from a food source
    or if it is rural and at least 500 people or 33% of people
    are more than 10 miles away from a food source. Returns None.
    '''
    fig, ax = plt.subplots(1)
    state_data.plot(ax=ax, color="#EEEEEE")
    state_data.dropna().plot(ax=ax, color='#AAAAAA')
    plt.title("Low Access Census Tracts")
    urban = state_data[state_data['Urban'] == 1]
    rural = state_data[state_data['Rural'] == 1]
    urban_new = urban[(urban['lapophalf'] >= 500) |
                      ((urban['lapophalf']/urban['POP2010']) >= 0.33)]
    rural_new = rural[(rural['lapop10'] >= 500) |
                      ((rural['lapop10']/rural['POP2010']) >= 0.33)]
    urban_new.plot(ax=ax)
    rural_new.plot(ax=ax)
    plt.savefig("low_access.png")


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
