# Covid19-Sentiment-Analysis
The basic agenda for this project is to use the #tags and other twitter components to analyse the behaviour of the indian citizens towards the overall situation of the lockdown.   

# Timeline of lockdown :
Phase 1 : 25 March – 14 April   
Phase 2 : 15 April – 3 May   
Phase 3 : 4–17 May    
Phase 4 : 18–31 May     
Phase 5 : 1–30 June    
We will be analyzing the tweets on 16th April,2020 i.e a day after Phase-2 was declared to see the sentiment of the people.   

# Data Collection :
For this project i have obtained the dataset from Kaggle :    
https://www.kaggle.com/smid80/coronavirus-covid19-tweets-late-april?select=2020-04-16+Coronavirus+Tweets.CSV.   

# Visualization :
* Word Cloud
* Count Plot
* Histogram
* Distribution Plot
* Bar Plot

# Web App
A simple web app is made using Streamlit for displaying the visualizations.    
The code and dataset for the same is in the 'app.py' file and 'tweeting.csv' respectively.

The webapp is deployed on heroku platform : https://covid19-sentiment-analysis.herokuapp.com/        
The following files are required for deployment :
* Procfile
* requirements.txt 
* setup.sh

![alt text](https://github.com/kartikmohan123/Covid19-Sentiment-Analysis/blob/master/webapp-1.JPG)

![alt text](https://github.com/kartikmohan123/Covid19-Sentiment-Analysis/blob/master/webapp-2.JPG)
## TextBlob is used to predict the sentiment as Positive, Negative or Neutral.



### You can also find the notebook on Kaggle :
https://www.kaggle.com/kartikmohan1999/covid19-sentiment-analysis
