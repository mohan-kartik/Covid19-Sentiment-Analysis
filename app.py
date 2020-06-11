# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:27:51 2020

@author: KARTIK
"""

import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import re

from collections import Counter

st.title("Sentiment Analysis of Tweets about COVID19")
st.sidebar.title("Sentiment Analysis of Tweets")
st.markdown("* Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.")
st.markdown("* There are worldwide curfews, quarantines and lockdown established to prevent further spread of the virus.")
st.markdown("* The basic agenda for this project is to use the #tags and other twitter components to analyse the behaviour of the indian citizens towards the overall situation of the lockdown.")

st.markdown(" ")
st.markdown(" ")

st.sidebar.markdown("We will be analyzing the tweets on 16th April,2020 i.e a day after Phase-2 was declared.")

@st.cache
def get_data():
    return pd.read_csv('tweeting.csv')
tweet = get_data()
        
st.sidebar.subheader("Show top 5 tweets by :")
select = st.sidebar.selectbox('Type', ['Favourite Count', 'Retweets'], key='1')
if not st.sidebar.checkbox("Hide", True):
    if select == 'Favourite Count' :
        st.subheader('Top 5 most Favourited tweets:')
        fav = tweet[['favourites_count','text']].sort_values('favourites_count',ascending = False)[:5].reset_index()
        for i in range(5):
            st.markdown((i, fav['text'][i]))

    if select == 'Retweets' :
        st.subheader('Top 5 most Retweeted tweets:')
        retweet = tweet[['retweet_count','text']].sort_values('retweet_count',ascending = False)[:5].reset_index()
        for i in range(5):
            st.markdown((i , retweet['text'][i]))
        

st.subheader("Number of Tweets/Hour")
plt.figure(1, figsize=(10,6))
plt.hist(tweet["created_at"],bins = 24);
plt.xlabel('Hours',size = 15)
plt.ylabel('No. of Tweets',size = 15)
st.pyplot()

st.subheader("Sentiment Count")
sns.countplot(x='sentiment', data = tweet);
st.pyplot()

st.subheader("Sentiment Distribution")
plt.figure(figsize=(10,6))
sns.distplot(tweet['polarity'], bins=30)
plt.xlabel('Polarity',size = 15)
plt.ylabel('Frequency',size = 15)
st.pyplot()
