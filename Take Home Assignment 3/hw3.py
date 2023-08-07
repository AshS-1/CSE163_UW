'''
Ashwika Sharma
Section AC
Implements the functions of HW3: Education. Using a dataset from the National
Center for Education Statistics that gives information on the percentage of
people from 25-29 with specific levels of education by race/ethnicity and sex
from 1920 through 2018, these functions provide information at specific
instances,a variety of different graphs to visualize specific data over time,
and trained a model to predict the percentage of degrees based on demographics.
'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

sns.set()


def compare_bachelors_1980(dataset: pd.DataFrame) -> pd.DataFrame:
    '''
    Takes in data as a DataFrame, and gets the percentage of men and
    women who at minimum recieved a Bachelor's degree in 1980. It returns
    a 2 by 2 DataFrame with the two rows representing men and women,
    and the two columns correspond to Sex and Total percentage.
    '''
    year = dataset['Year'] == 1980
    degree = dataset['Min degree'] == 'bachelor\'s'
    sex = dataset['Sex'] != 'A'
    final = dataset[year & degree & sex]
    return final[['Sex', 'Total']]


def top_2_2000s(dataset: pd.DataFrame, sex: str = 'A') -> pd.Series:
    '''
    Takes in a dataset DataFrame, as well as a string M or F for the sex. The
    default value for that string would be 'A'. The function returns a
    2-element series with the two most commonly earned degrees for the
    particular sex and their mean percentage of students.
    '''
    sex = dataset['Sex'] == sex
    years = ((dataset['Year'] >= 2000) & (dataset['Year'] <= 2010))
    final = dataset[sex & years]
    one = final.groupby('Min degree')['Total'].mean()
    top2 = one.nlargest(2)
    print(top2)
    return top2


def line_plot_bachelors(dataset: pd.DataFrame) -> None:
    '''
    Takes in a DataFrame dataset, and plots a line chart of the percentage
    of people with sex A (all sexes) with a bachelor's degree over time
    (in years), from 1940-2020. Saves the image in line_plot_bachelors.png
    but returns nothing.
    '''
    sexes = dataset['Sex'] == 'A'
    degree = dataset['Min degree'] == 'bachelor\'s'
    plot = dataset[sexes & degree]
    sns.relplot(x='Year', y='Total', data=plot, kind='line')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title('Percentage Earning Bachelor\'s over Time')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(dataset: pd.DataFrame) -> None:
    '''
    Takes in DataFrame dataset and plots a bar chart with sexes F, M, and A,
    with their corresponding total percentages who had a minimum degree
    of high school in 2009. Saves the image in line_plot_bachelors.png but
    returns nothing.
    '''
    year = dataset['Year'] == 2009
    degree = dataset['Min degree'] == 'high school'
    plot = dataset[year & degree]
    sns.catplot(data=plot, x="Sex", kind="bar", y='Total')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.title('Percentage Completed High School by Sex')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(dataset: pd.DataFrame) -> None:
    '''
    Takes in a DataFrame dataset and plots how the percentage of all (A)
    Hispanic students with a high school or bachelor's minimum degree change
    over time as a line graph over the time period of 1990-2010. Graph is
    saved in bar_chart_high_school.png but nothing is returned.
    '''
    year = (dataset['Year'] >= 1990) & (dataset['Year'] <= 2010)
    degree = (dataset['Min degree'] == 'high school') | \
        (dataset['Min degree'] == 'bachelor\'s')
    gender = dataset['Sex'] == 'A'
    plot = dataset[year & degree & gender]
    sns.relplot(x='Year', y='Hispanic', data=plot,
                kind='line', hue='Min degree')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title('Percentage of Hispanic Students with High School and \
        Bachelor\'s by Year')
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(dataset: pd.DataFrame) -> float:
    '''
    Takes in a DataFrame dataset and trains a DecisionTreeRegressor model to
    predict the percentage of degrees that a particular Sex, Minimum Degree,
    and Year obtain. It takes in the dataset and returns the test mean squared
    error as a float.
    '''
    data = dataset[['Sex', 'Min degree', 'Year', 'Total']]
    data = data.dropna()
    features = data.loc[:, data.columns != 'Total']
    features = pd.get_dummies(features)
    labels = data['Total']
    feat_train, feat_test, lab_train, lab_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(feat_train, lab_train)
    predictions = model.predict(feat_test)
    return mean_squared_error(lab_test, predictions)


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    compare_bachelors_1980(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    top_2_2000s(data, 'A')


if __name__ == '__main__':
    main()
