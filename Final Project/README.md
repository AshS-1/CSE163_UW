Analyzing Models, Trends and Causes of Deforestation and Degradation of Forests in the Amazon Rainforest
8/16/2023
Summary of Questions and Results:
1.	How can we model which regions in the Amazon Rainforest experience deforestation?

I created a decision tree ML model that would use the column in my dataset, such as hydrography area, forested area, etc. to predict which regions were likely to experience deforestation. When testing with all of my test data, it had an accuracy score of 0.94, which indicates that the model is working well and is largely accurate. When I tested it with 20% of my data, the accuracy score dropped to 0.74, which is reasonable because I am giving it less data.

2.	What is the trend in the number of forest fires in the Amazon rainforest by year? Does this correlate with an increase in rainforest temperature?

Plotting the number of firespots from each of the years from 1999 to 2019 shows that there was a sharp increase from 1999 to 2001, and 2001 was the peak of forest fires in between 1999 and 2001. Following 2001, the number of forest fires gradually has decreased to levels relatively similar to 1999.
Plotting the number of forest fires as a “function” of temperature showed that there wasn’t any clear trend on whether temperature was an indicator of the number of forest fires. Contrary to popular belief that higher temperatures mean greater forest fires, the scatter plot shows me that temperatures even as low as 26 degrees Celsius can still have high amounts of forest fires compared to the corresponding number of firespots for higher temperatures.

3.	What are the leading causes of deforestation from 2001-2013? If there are certain leading causes prevalent throughout most of the decade, what is their trend over the years?

Looking at pie charts breaking down the number of hectares of degraded land were attributed to causes such as industrial usage, pastures, fires, flooding due to dams, etc., pastures were the leading cause for all of the graphs by a significant amount. Throughout the years, pastures have consistently accounted for over 50% of the degradation/deforestation of the Amazon Rainforest.
Pastures was the most prominent leading cause, and looking into any trends in the amount of land cleared for pastures over the years, I notices that although the number of hectares jumped up between 2001 and 2002 and remained relatively constant between 2002 and 2005, it then decreased sharply and remains much lower than it was in 2001.
Motivation:
Deforestation is an issue that is only on the rise, affecting forests all over the world. The World Resources Institute estimated that around 2.9 million acres of forest were cleared in 2018. In context, this is about the same amount of land as the continent of Australia. Deforestation as this level can have devastating effects on wildlife, who are displaced from their natural habitats. Rainforests contain over 80% of the world’s terrestrial biodiversity, and to ruin these habitats can have disastrous implications as these actions can drive many species (including countless undiscovered ones) into extinction. Deforestation also leads to intensifying of global warming, accounting for close to 15% of emissions (cutting down trees releases lots of greenhouse gases).
I narrowed down my investigation to analyzing deforestation in the Amazon Rainforest in particular, firstly because the wide scope of this issue it was impossible to look into deforestation throughout the world without compromising specificity and meaningful results. Secondly, I’ve read a lot of news articles at school about how deforestation in the Amazon Rainforest has been increasing in an alarming rate, and I wanted to look into the data to gain more insight about this proposed trend.

Datasets:
https://www.kaggle.com/datasets/diegosilvadefrana/brazilian-deforestation-from-2000-to-2021?resource=download&select=data.csv 
This dataset, in the standard csv format, includes historical data from 2000-2021 about deforestation in the Amazon Rainforest. This data was obtained from the Brazilian National Institute for Space Research (INPE). 
The columns in this dataset include ano (year), id_municipio (County ID), area (total area of county), desmatado (area deforested), Floresta (forest area), nuvem (area covered by clouds, nao_observado (non-observed area), nao_floresta (non-forest area), and hidografia (hydrography area). 
There is a smaller dataset that corresponds the id_municipio with the county name.
This dataset will be used to identify which regions experience the most deforestation.
https://www.kaggle.com/datasets/mbogernetto/brazilian-amazon-rainforest-degradation?select=inpe_brazilian_amazon_fires_1999_2019.csv
This dataset, contains three files with information on fire outbreaks, deforestation by state, and occurances of el nino and la nina. However I will only be using inpe_brazillain_amazon_fires_1999_2019. This file has data in the standard csv format with the number of fire outbreaks in the Amazon by state, month, and year, from 1999 to 2019. The dataset was extracted from the INPE website (http://terrabrasilis.dpi.inpe.br/queimadas/portal/) on December 13th, 2019, which detected fire outbreaks though satellite imaging, and was updated every 3 hours. 
The columns in this dataset include year, month, state, latitude (average latitude of all occurrences in that specific month, year, and state), and firespots (number of fire outbreaks)
This dataset will be used to explore trends in fire outbreaks in the Amazon and see if they corresponded with the temperature of the rainforest.
https://demo.arcticdata.io/view/urn%3Auuid%3A2894fbf8-7cbf-4ce8-8101-94a1e545be06
This csv dataset has information on the air temperature of the Amazon from 2000-2010. The raw data was collected by Mai Fosline and Halina Do-Linh by using remote sensing to record the temperature every hour and calculate a daily average. Because of the yellow fever epidemic in 2005, there is a gap in data from that year.
The columns of this dataset include sampledate, year, and ave_air_temp_adjusted (daily average temperature). 
This dataset was used with the dataset above to see if there was any correlation between the number of fire outbreaks and the temperature.
https://ourworldindata.org/grapher/drivers-forest-loss-brazil-amazon?time=2002..latest
This csv dataset is about the causes of forest loss in the Amazon from 2001 to 2013. It has data on how many hectares of forest are either deforested or degraded each year due to causes such as fires, flooding, mining, etc.
The columns are Entity, Code, Year, flooding_due_to_dams, natural_disturbances, fire, selective_logging, other_infrastructure, roads, mining, small-scale_clearing, tree_plantations_including_palm, pasture, and commercial_crops. The Entity and Code both refer to the country, which is Brazil for all rows. 
This dataset was used to look into what were the leading causes of forest loss in the Amazon and how has this dynamic changed over time.
Method:
Research Question 1: What are the regions in the Amazon Rainforest that experience the greatest deforestation?
1.	Merge the datasets data_counties and data_all, so that the IDs in data_all correspond with a county name that is given in data_counties
2.	Separate the features and the labels  assign the label as Nome_Microrregião.
3.	Print the features and labels for reference
4.	Train the test split based on the features
5.	Use the OneHotEncoder and transform the existing train and test data
6.	Train the model as a DecisionTreeClassifier()
7.	Make predictions
8.	Print the accuracy scores for the train and test data.
Research Question 2: What is the trend in the number of forest fires in the Amazon rainforest by year? Does this correlate with an increase in rainforest temperature?
1.	The parameters of my function take in pd.DataFrame fire_data, and temp_data. They correspond to the dataset on firespots and temperature over time. These files have already been read in the main method.
2.	Filtering and modifying temp_data:
a.	The temp_data has data on the temperature for multiple days in a year. Because I need only one value for the temperature per year, I took the maximum daily temperature for each year. This was done by applying Groupby by year, and obtaining a series with the maximum ave_air_temp_adjusted for each year.
b.	I will be merging this data in the future so I need to make the Series into a DataFrame, and do so by applying reset_index()
c.	The fire_data dataset only includes information on firespots from 1999 to 2019, whereas temp_data includes information from 1870 onwards, so I filtered the temp_data to only include years 1999-2019.
d.	Only needed the columns for year and ave_air_temp_adjusted, so I sliced the DataFrame to only include those columns
3.	Groupby on fire_data.
a.	Applied Groupby by year on fire_dara and created a series yearly_fire with the total number of firespots each year.
b.	Because I will be merging this with the temperature DataFrame, I converted this Series into a DataFrame using reset_index()
4.	Used plotly library to plot the number of firespots per year using a line plot.
a.	Saved the figure as yearly_fire.png
5.	Merged the two DataFrames yearly_fire and temp_interval (the modified temperature dataset) by year.
6.	Plot a scatterplot of the merged data using the plotly library. The scatterplot shows the number of firespots as a function of temperature.
a.	Saved the figure as temp_fire.png
Research Question 3: What are the leading causes of deforestation from 2001-2013? If there are certain leading causes prevalent throughout most of the decade, what is their trend over the years?
1.	The parameters of this function take in pd.DataFrame data. This corresponds to the dataset on leading causes of deforestation, and the csv file was read in the main method.
2.	Created a figure with four axes using plt.subplots
3.	For each of the years 2013, 2009, 2005, and 2001
a.	Filtered the data into a new DataFrame with just that particular year.
b.	Assign categories as the 4th column and onwards using current_data.columns[3:]  removes the first three columns because they are not categories I will use in the pie chart.
c.	Assign values as the values corresponding to the 4th column and onward. These are the number of hectares lost because of each of these categories.
d.	Create a pie chart with the values and categories using seaborn.
i.	Each pie chart is on a different axis for the same figure.
4.	Plt.tight_layout(), plt.title(), plt.savefig(‘leading_causes_subplot.png’) as final adjustments to the overall figure.
5.	Create a bar graph with the plotly library that shows how land used for pastures changed over time, with x as ‘Year’ and y as ‘pasture’
Results:
Research Question 1: How can we model which regions in the Amazon Rainforest experience deforestation?
I decided to use a ML model to predict what regions experience deforestation. This model made a decision tree that used the columns from the dataset provided, such as total area of county, area deforested, forest area, area covered by clouds, non-observed area, non-forest area, and hydrography area, as features to predict the label of which regions were most likely to experience deforestation.
Above is the visualization for my decision tree. I had to make the maximum depth 5 because there were thousands of data points and they would not fit in this image.
The decision tree model that I created had a train accuracy of 1.0 and a test accuracy of approximately 0.94. Anything between a 70-90% test accuracy indicates that the ML model is performing well and accurately, and is consistent with industry standards. My ML model has a test accuracy of 94% which is way above the threshold for a good ML model.
Research Question 2: What is the trend in the number of forest fires in the Amazon rainforest by year? Does this correlate with an increase in rainforest temperature?

I used a line graph to plot the number of firespots/fire outbreaks from 1999 to 2019. What’s important to notice is that there were relatively low numbers of fire outbreaks in 1999 (around 60K), but there was a dramatic jump in the number of fire outbreaks (400-500% increase since 1999). The graph shows that it reaches a peak in 2001, however, it then starts to decrease.
It's surprising to see that following the peak of forest fires in 2001, the number of fire outbreaks decreased significantly, even reaching levels comparable to 1999 by 2019. A possible reason for this could be an increase in climate agreements and increased awareness about the forest degradation in the Amazon Rainforest, which could have led to measures that deal with better prevention/dealing with forest fires.
One of the reasons why this finding was so interesting to me was because I always correlated increased temperature with greater numbers of forest fires. Because of global warming, which leads to increased temperature, I thought that there would be more forest fires in recent years, which isn’t the case as seen in the graph. I decided to expand upon this observation and look into whether there was any observable correlation between the highest temperature and number of firespots in a year. I chose to look at the highest temperature as a representative of a year’s temperature because I assumed that greater numbers of forest fires occur in seasons where the temperature was already very high, so it seemed irrelevant/more difficult to look at lower temperatures. I plotted a scatter plot with the yearly high temperature being the x axis and the number of firespots as the y-axis.
The results were not at all aligned with some of the assumptions I had. The scatterplot shows datapoints with no obvios trend – they are all over the graph with no clear pattern. Temperature seems to have no bearing on the number of forest fires there are in a year, because we can see a large variety (lows and highs) of fire outbreak quantities, regardless of it being a relatively high or low temperature. The data shows that the yearly high temperature (in Celsius) does not correlate with the number of fire outbreaks.
A possible explanation for this observation may be that high temperatures lead to drier conditions which makes regions more susceptible to fires. As the Amazon Rainforest is extremely humid, higher temperatures may not create a noticeable amount of “dryness” that can lead to a visible change in fire outbreaks.
Research Question 3: What are the leading causes of deforestation from 2001-2013? If there are certain leading causes prevalent throughout most of the decade, what is their trend over the years?
Using my csv file on deforestation causes, I decided to create 4 pie charts, focusing on the distribution of how much land each cause had affected, based on equal intervals from my time frame. Thus, I created four pie charts from 2013, 2009, 2005, and 2001 to see if there was any specific cause of deforestation/degradation that stood out or had a significant impact.
As seen in the pie charts pastures take up the majority of deforested land. In recent years, it makes up for around 50% of all deforested land, however in previous years such as 2005 and 2001 it made up for over 2/3 of that land. Following pastures, small scale clearing are the next leading cause, and their purpose is also similar to that of pastures – agriculture and livestock.
I wasn’t expecting to see that one cause would lead to such a “monopoly” over the total deforested land, but it makes sense, based on previous research that I’ve done about how it is hard for the agriculture sector to deal with the rapidly increasing world population, because existing agricultural land is being overused and depleted of its resources. The Amazon is a place where people may be interested in growing crops in. 
I wanted to look into how the number of hectares of land did pastures take up and how that changed over the timeframe (2001-2013). This was represented in a bar graph, as seen below.
This graph shows that the amount of land cleared out for pastures jumped significantly from 2001 to 2002 and remained relatively constant at that high value from 2002 to 2005, and then decreased sharply. This aligns with the pie charts as they show why the percentage of total deforested land decreased from 67% to 52% over the years.
Surprisingly, this also aligns with Research Question #2, in which I noticed that the number of forest fires had a peak in 2001 and then decreased steadily. While I can’t be sure about how minimizing pastures leads to less forest fires, definitely it shows that 2001-2002 may have been a turning point for the Amazon Rainforest.
Impact and Limitations:
To a certain extent, these results bring optimism. They give an alternative perspective to the common understanding that the environment of the world is getting worse by showing how deforestation, forest fires, and pasture usage decreases, by showing that things are getting better, but there’s still a long way to go. It clearly identifies pastures as a leading cause of deforestation, so these results will be useful in increasing awareness to minimize clearing land for these purposes. Unfortunately, my results don’t mean that the Amazon Rainforest is being unharmed, it just means that the level of harm may not be as high as we commonly think it is. These results shouldn’t be interpreted as a way for people to justify current unstable, detrimental actions, rather it should show how increased awareness and consciousness of actions can go a long way in protecting the environment. A limitation is that some of this data goes to 2013, which is 10 years ago. A lot can happen in 10 years, so I think my results and models need to include those missing 10 years to come up with conclusions that are immediately relevant to right now. Ranchers and farmers should use this research as a clear indicator about how actions such as clearing out land for pastures leads to detrimental impacts to the rainforest.
Challenge Goals:
Firstly, I met the challenge goal of Machine Learning. I trained and tested a decision tree model that used the statistics about each region in the Amazon such as forested area, hydrography, etc. as features to predict the label of which regions were likely to have deforestation. The ML model had an accuracy score of 0.94, which is relatively high. 
I also used a new library, Plotly to create most of my graphs (excluding the pie charts). I found it really useful in creating clean graphs that minimized complex, buggy code that would have been needed in spacing out text and making the colors match.
Lastly, I merged my datasets for my first and second research questions. For my first research question, I needed to merge the IDs for the regions in one dataset with a dataset that showed what counties the IDs corresponded to. In my second research question, I had to merge the data on how many fire outbreaks there were in a year with the highest temperature in that year, so that I could plot a graph that would show if the number of fire outbreaks and highest temperature in the same year would show some sort of correlation.
Work Plan Evaluation:
I did this project individually, so I didn’t set very strict deadlines for each of the components of my work. I started 4 days before the due date, and I decided that I was going to set up the environment and start the basic coding on Sunday and get the majority of my graphing/visualizations done by Monday. Unfortunately, I didn’t know how to import plotly until Tuesday so that slowed me down greatly. I had planned to work on the ML model portion two days before the deadline, and surprisingly it took much less time than I had anticipated, so I was able to use that time to catch up with my visualizations. However, because everything was only ready by the morning of the due date, I had to write the entire paper and record the video in one day. It was definitely a time crunch that I had anticipated.
Testing:
Research Question 1:
To test the ML model, I applied the same code on a smaller dataset with only 20% of the data values. Above is the decision tree visualization. 
It looks relatively similar to the decision tree from the larger dataset. Also, the model has an accuracy score of 0.71, which makes sense because I am giving it less data than it got for the main model. Still, an accuracy score of 0.71 is still high enough for it to be relevant.
Research Question 2:
I inputted datasets that were 20% of their original size for fire_data and temp_data. 
 
Looking at the change in fire outbreaks over time, I can see that there is a similar trend as seen with the larger dataset. The number of firespots is at a peak in 2001, and then sharply decreases. This exact trend was seen above.

Similarly, when looking at the relationship between fire outbreaks and highest air temperature, we see that there is no clear correlation, which aligns with what we concluded when testing with the larger dataset.
Research Question 3:
I narrowed down my dataset of causes of deforestation to only 2013, 2009, 2005, and 2001, excluding all other years, and looked into the visualizations that they provided.
 
Figure 8 Testing pie charts on leading causes of deforestation
As seen above, pastures account for the vast majority of the deforested land, which aligns with the conclusions made with the larger dataset. Plotting the change in the amount of land pastures take up from 2001-2013, we see something similar to the trends seen above about a peak in 2004 that steadily declines.
 
Figure 9 Testing Hectares of pasture from 2001 to 2013
Even in this graph, we can see that there is a peak in 2004 and the number of hectares then sharply decreases as we approach 2013.
Collaboration:
https://www.worldwildlife.org/threats/deforestation-and-forest-degradation#:~:text=Deforestation%20and%20forest%20degradation%20are,frequency%20of%20extreme%20weather%20events.  Information about Deforestation
https://animlbook.com/classification/trees/index.html  Helped me with constructing my ML model

![image](https://github.com/AshS-1/CSE163_UW/assets/108997371/a4c0b0b9-f43c-462b-924f-eeed09a18476)

