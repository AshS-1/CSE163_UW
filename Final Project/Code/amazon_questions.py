'''
Ashwika Sharma
Section AC
The functions for analyzing the leading causes of Amazon Rainforest
deforestation over time, predicts the regions with the most
deforestation, and how forest fires are related to temperature
in the rainforest.
'''
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree


def question_1(data_counties: pd.DataFrame, data_all: pd.DataFrame) -> None:
    '''
    Takes in a data_counties DataFrame which represents the correponding
    counties for each municipalty ID and data_all DataFrame which represents
    the dataset for each of the regions and the amount of deforestation in each
    Creates a ML model that predicts the regions with deforestation based on
    features.
    '''
    data = data_all.merge(data_counties, left_on='id_municipio',
                          right_on='Código Município Completo')

    label = "Nome_Microrregião"
    features = data.columns[data.columns != label]

    print("Features:")
    print(features)
    print("Label:", label)
    print()

    train_data, test_data, train_labels, test_labels = train_test_split(
        data[features], data[label], test_size=0.2)

    print("Train size:", len(train_data))
    print("Test  size:", len(test_data))
    print()

    encoder = OneHotEncoder(handle_unknown='ignore')\
        .fit(train_data)
    train_data = encoder.transform(train_data)
    test_data = encoder.transform(test_data)

    model = DecisionTreeClassifier()
    model.fit(train_data, train_labels)

    class_names_list = model.classes_.tolist()

    plt.figure(figsize=(20, 10))
    plot_tree(model, feature_names=None, class_names=class_names_list,
              filled=True, rounded=True, max_depth=5)
    plt.title("Decision Tree Visualization")
    plt.show()

    train_predictions = model.predict(train_data)
    test_predictions = model.predict(test_data)

    print("Train Accuracy:", accuracy_score(train_labels, train_predictions))
    print("Test  Accuracy:", accuracy_score(test_labels, test_predictions))


def precalc_2(fire_data: pd.DataFrame,
              temp_data: pd.DataFrame) -> pd.DataFrame:
    '''
    Takes in pd.DataFrame fire_data and temp_data. Correspond to datasets on
    firespots and temperature over time. Returns modified versions of these
    two DataFrames so that they align with the right time interval and
    have only the values needed for question 2.
    '''
    temp_data_common = temp_data.groupby('year')['ave_air_temp_adjusted']\
                                .max().reset_index()
    temp_interval = temp_data_common[(temp_data_common['year'] > 1998)
                                     & (temp_data_common['year'] < 2020)]
    temp_interval = temp_interval[['year', 'ave_air_temp_adjusted']]
    yearly_fire = fire_data.groupby('year')['firespots'].sum()
    yearly_fire = yearly_fire.reset_index()
    return yearly_fire, temp_interval


def question_2(fire_data: pd.DataFrame, temp_data: pd.DataFrame) -> None:
    '''
    Take in pd.DataFrame fire_data, and temp_data. They correspond to datasets
    on firespots and temperature over time.
    Answers question "What is the trend in the number of forest fires in the
    Amazon rainforest by year? Does this correlate with an increase in forest
    temperature? Creates a line pot showing the change in fire outbreaks over
    time from 1999-2019. Also plots a scatterplot showing the number of fire
    outbreaks when corresponded to the temperature, in Celcius.
    '''
    yearly_fire, temp_interval = precalc_2(fire_data, temp_data)
    fig = px.line(yearly_fire, x="year", y="firespots",
                  title='Number of Fire Outbreaks in 1999-2019')
    fig.show()
    merged = yearly_fire.merge(temp_interval, left_on='year', right_on='year')
    fig = px.scatter(merged, x="ave_air_temp_adjusted", y="firespots", labels={
                        'ave_air_temp_adjusted': 'Yearly High temperature in\
                        Celsius'
                    },
                     title='Number of Fire Outbreaks vs Highest Air\
                     Temperature Yearly')
    plt.savefig('temp_fire.png')
    fig.show()


def question_3(data: pd.DataFrame) -> None:  # change the question name
    '''
    Take in pd.DataFrame data, corresponds to dataset on leading causes of
    deforestation. Answers the question "What are the leading causes of
    deforestation from 2001-2013? If there are certain leading causes
    prevalent throughout most of the decade, what is their trend over the
    years? This is done by creating a figure of a
    pie charts showing the hectares of land lost due to various causes
    such as fires, flooding, industry, etc. Further expands on what is
    identified as the leading cause, pastures, and the change in
    pastures over time.
    '''

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))

    # Assuming data is already defined and imported
    current_data = data[data['Year'] == 2013]
    categories = current_data.columns[3:]
    values = current_data.iloc[0, 3:]

    # Create a pie chart within ax1 subplot
    ax1.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    ax1.set_title('Distribution of Categories in 2013')
    ax1.axis('equal')

    current_data = data[data['Year'] == 2009]
    categories = current_data.columns[3:]
    values = current_data.iloc[0, 3:]

    # Create a pie chart within ax2 subplot
    ax2.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    ax2.set_title('Distribution of Categories in 2009')
    ax2.axis('equal')

    current_data = data[data['Year'] == 2005]
    categories = current_data.columns[3:]
    values = current_data.iloc[0, 3:]

    # Create a pie chart within ax3 subplot
    ax3.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    ax3.set_title('Distribution of Categories in 2005')
    ax3.axis('equal')

    current_data = data[data['Year'] == 2001]
    categories = current_data.columns[3:]
    values = current_data.iloc[0, 3:]

    # Create a pie chart within ax4 subplot
    ax4.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    ax4.set_title('Distribution of Categories in 2001')
    ax4.axis('equal')

    plt.tight_layout()  # Adjust spacing between subplots
    plt.savefig('leading_causes_subplot.png')
    plt.show()

    # Make a bar graph on pastures over time
    fig = px.bar(data, x='Year', y='pasture', labels={
                     "Year": "Year",
                     "pasture": "Hectares of Pasture",
                 }, title="Hectares of Pasture from 2001-2013")
    fig.show()
