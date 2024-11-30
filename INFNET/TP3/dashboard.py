import streamlit as st
import matplotlib.pyplot as plt
import csv

st.title('Sentiment Analysis')

sentiments_count = {}

with open('sentiments.csv', 'r', encoding='latin-1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        sentiment = row['sentiment']
        if sentiment in sentiments_count:
            sentiments_count[sentiment] += 1
        else:
            sentiments_count[sentiment] = 1

labels = list(sentiments_count.keys())
sizes = list(sentiments_count.values())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

