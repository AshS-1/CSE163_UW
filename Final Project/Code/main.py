'''
Ashwika Sharma
Section AC
Analyzes the leading causes of Amazon Rainforest deforestation over time,
predicts the regions with the most deforestation, and how forest fires are
related to temperature in the rainforest.
'''
import pandas as pd
import seaborn as sns
import amazon_questions

sns.set()


def main():
    data_1_counties = pd.read_csv('Counties.csv')
    data_1 = pd.read_csv('data.csv')
    percent = 0.2
    test_data_1 = data_1.sample(frac=percent)

    amazon_questions.question_1(data_1_counties, data_1)
    amazon_questions.question_1(data_1_counties, test_data_1)

    data_2_fire = pd.read_csv('regions_of_fire.csv')
    data_2_temp = pd.read_csv('air_temp.csv')
    test_data_2_fire = data_2_fire.sample(frac=percent)
    test_data_2_temp = data_2_temp.sample(frac=percent)
    amazon_questions.question_2(data_2_fire, data_2_temp)
    amazon_questions.question_2(test_data_2_fire, test_data_2_temp)

    data_3 = pd.read_csv('deforestation_causes.csv')
    test_data_3 = data_3[(data_3['Year'] == 2013) | (data_3['Year'] == 2009)
                         | (data_3['Year'] == 2005) | (data_3['Year'] == 2001)]
    amazon_questions.question_3(data_3)
    amazon_questions.question_3(test_data_3)


if __name__ == '__main__':
    main()
