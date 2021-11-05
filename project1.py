#!/usr/bin/env python
# coding: utf-8

# # Business Understanding 
# in this project we will take a look at data about video games sales to try to understand and improve the video games industry.
# to do that,we came up with these three qustions : 
# -  what is the best selling genre ?
# -  what is the best selling genre in japan ?
# -  what genre have the most games ?

# # Data Understanding
# in this section we will take a look at the raw data provided by Kaggle,
#  to have an understanding of how we can handle the data to prepared it for the data analysis 

# In[2]:


#import used libraries
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import ALookAtTheData as t
from collections import Counter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#showing the raw data
df = pd.read_csv('./Video_Games_Sales_as_at_22_Dec_2016.csv')
df


# In[4]:


#show information about the data 
df.info()


# In[6]:


#get the number of rows and columns
print("Number of rows:" , df.shape[0]) 
print("Number of columns:" , df.shape[1])


# As we can see the raw data consists of 16 columns and 16719 rows, 
#  and based on the number of values for each column, we can see that some of the column have null values that we need to deal with . 

# # Data Preparation
# to preper the data we will need to drop the unrelated columns, check for duplicates and null values, then drop duplicates and null values if found.
# 

# In[7]:


#drop unrelated columns
cleaned = df.drop(["NA_Sales","EU_Sales","Other_Sales","Critic_Score","Critic_Count","User_Score","User_Count","Rating"],axis = 1)
cleaned


# In[8]:


#check if there are duplicates 
print(cleaned.duplicated().sum())


# In[16]:


#drop NA values and reformat Year_of_Release column
cleaned = cleaned.dropna()
cleaned['Year_of_Release']=cleaned['Year_of_Release'].astype(int)
cleaned


# # Data analysis

# # Question 1: What is the best selling genre ?
# 

# In[10]:


#group data based on genre and sort based on total sales
Q1 = cleaned.groupby(["Genre"])["Global_Sales"].sum().sort_values(ascending=False)
Q1


# In[11]:


#plot the results 
Q1.plot.bar(x='Genre', y='Global_Sales')


# in this figure we can see that the best selling genre globally is the Action genre with 1338 million units sold
# and the second best selling genre is sports with 982 million units sold.

# # Question 2: What is the best selling genre in japan ?

# In[12]:


#gruop by genre and sort by most sales in JP_Sales column
Q2 = cleaned[['Genre', 'JP_Sales']].sort_values('JP_Sales', ascending=False)
Q2 = Q2.groupby(["Genre"])["JP_Sales"].sum().sort_values(ascending=False)
Q2


# In[13]:


#plot the results
Q2.plot.bar(x = 'Genre', y = 'JP_Sales' )


# in this figure we can see that the best selling genre in Japan is Role-Playing with 129 million units sold
# and the worst selling genre in Japan is Strategy with only  4.46 million units sold.
# 
# which indicates that there is a huge market for the Role-Playing genre in Japan unlike the Strategy genre.  

# # Question 3: What genre have the most games ?

# In[14]:


#counter the number of game per genre
Q3 = cleaned[['Genre']]
c = Counter(Q3['Genre'])
c


# In[15]:


#plot the results
plt.xticks(rotation=90)
plt.bar(c.keys(), c.values())


# this bar chart shows the number of games per genre, we can see that the genre with the highest number of games is the Action genre.
