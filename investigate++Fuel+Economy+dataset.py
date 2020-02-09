
# coding: utf-8

# # About Fuel Economy dataset

# The fuel economy of an automobile is the fuel efficiency relationship between the distance traveled and the amount of fuel consumed by the vehicle. Consumption can be expressed in terms of volume of fuel to travel a distance, or the distance travelled per unit volume of fuel consumed.

# # step(1):-Gathering Data

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# In[2]:

df_08=pd.read_csv('E:/data analysis project/project_2/fuel_economy_datasets/all_alpha_08.csv')
df_08.head(5)


# In[3]:

df_18=pd.read_csv('E:/data analysis project/project_2/fuel_economy_datasets/all_alpha_18.csv')
df_18.head(5)


# # step(2):-Assessing Data

# In[5]:

df_08.shape


# In[6]:

df_18.shape


# In[9]:

df_08.duplicated().sum()


# In[11]:

df_18.duplicated().sum()


# In[12]:

df_08.info()


# In[13]:

df_18.info()


# In[14]:

df_08.isnull().sum()


# In[15]:

df_18.isnull().sum()


# In[16]:

df_08['SmartWay'].nunique()


# In[17]:

df_18['SmartWay'].nunique()


# In[18]:

df_08[df_08['Fuel']=='Gasoline']


# In[19]:

df_18[df_18['Fuel']=='Gasoline']


# In[20]:

df_08[df_08['Fuel']=='Electricity']


# In[21]:

df_18[df_18['Fuel']=='Electricity']


# In[22]:

df_08[df_08['Fuel']=='CNG']


# In[23]:

df_18[df_18['Fuel']=='CNG']


# # step(3):-Cleaning the Data

# 1. Drop extraneous columns

# From 2008 dataset: 'Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'

# In[26]:

df_08=df_08.drop(['Stnd','Underhood ID','FE Calc Appr','FE Calc Appr'],axis=1)


# In[27]:

df_08.head(3)


# From 2018 dataset: 'Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'

# In[28]:

df_18=df_18.drop(['Stnd','Stnd Description','Underhood ID','Comb CO2'],axis=1)


# In[29]:

df_18.head(3)


# In[30]:

df_18.shape


# In[31]:

df_08.shape


# 2- Rename Columns

# In[32]:

df_08.columns


# In[33]:

col=['model', 'displ', 'cyl', 'trans', 'drive', 'fuel', 'cert_region',
       'veh_class', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg',
       'unadj_cmb_mpg', 'greenhouse_gas_score', 'smartWay']


# In[34]:

df_08.columns=col


# In[35]:

df_08.columns


# In[36]:

df_18.columns


# In[37]:

colu=['model', 'displ', 'cyl', 'trans', 'drive', 'fuel', 'cert_region',
       'veh_class', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg',
        'greenhouse_gas_score', 'smartWay']


# In[38]:

df_18.columns=colu


# In[39]:

df_18.head(3)


# In[41]:

df_08=df_08.drop('unadj_cmb_mpg',axis=1)


# In[42]:

(df_08.columns == df_18.columns).all()


# # create checkpoint

# In[58]:

df_2008=df_08.copy()
df_2018=df_18.copy()


# In[46]:

df_2008.head(2)


# In[47]:

df_2018.head(2)


# 3.Filter

# For consistency, only compare cars certified by California standards. Filter both datasets using query to select only rows where cert_region is CA. Then, drop the cert_region columns, since it will no longer provide any useful information (we'll know every value is 'CA').

# In[59]:

df_2008=df_2008[df_2008['cert_region']=='CA']


# In[60]:

df_2018=df_2018[df_2018['cert_region']=='CA']


# In[61]:

df_2008=df_2008.drop('cert_region',axis=1)


# In[62]:

df_2018=df_2018.drop('cert_region',axis=1)


# 4.Drop Nulls

# In[65]:

df_2008=df_2008.dropna(axis=0)


# In[66]:

df_2018=df_2018.dropna(axis=0)


# In[69]:

df_2008.isnull().sum().any()


# 5.Drop duplicates

# In[67]:

df_2008=df_2008.drop_duplicates()


# In[70]:

df_2018=df_2018.drop_duplicates()


# In[71]:

print(df_2008.duplicated().sum())


# # create new checkpoint

# In[147]:

df_20_08=df_2008.copy()
df_20_18=df_2018.copy()


# 6-Fixing Data Types

# 1-Fix cyl datatype
# 2008: extract
# int from string.
# 2018: convert float to int.

# In[148]:

df_20_08['cyl']=df_20_08['cyl'].str.extract('(\d+)').astype(int)


# In[149]:

df_20_18['cyl']=df_20_18['cyl'].astype(int)


# 2-Fix air_pollution_score datatype
# 2008: convert string to float.
# 2018: convert int to float

# In[150]:

df_20_08['air_pollution_score']=df_20_08['air_pollution_score'].astype(float)


# In[151]:

df_20_08[df_20_08['air_pollution_score']=='6/4']


# solve the problem

# In[152]:

#let's get all the hybrid rows in 2008
hyb_08=df_20_08[df_20_08['fuel'].str.contains('/')]


# In[153]:

hyb_08


# In[154]:

#create two copies of the 2008 hybird dataframe
df_1=hyb_08.copy()
df_2=hyb_08.copy()


# In[155]:

df_1


# In[156]:

split_column=['fuel','air_pollution_score','city_mpg','hwy_mpg','cmb_mpg','greenhouse_gas_score']
for i in split_column:
    df_1[i]=df_1[i].apply(lambda x:x.split("/")[0])
    df_2[i]=df_2[i].apply(lambda x:x.split("/")[1])


# In[157]:

new_rows=df_1.append(df_2)


# In[158]:

new_rows


# In[159]:

df_20_08.drop(hyb_08.index,inplace=True)


# In[160]:

df_20_08=df_20_08.append(new_rows)


# In[161]:

df_20_08['air_pollution_score']=df_20_08['air_pollution_score'].astype(float)


# work with 2018

# In[162]:

hyb_18=df_20_18[df_20_18['fuel'].str.contains('/')]


# In[163]:

hyb_18


# In[164]:

df1=hyb_18.copy()
df2=hyb_18.copy()


# In[165]:

split_column=['fuel','city_mpg','hwy_mpg','cmb_mpg']
for i in split_column:
    df1[i]=df1[i].apply(lambda x:x.split("/")[0])
    df2[i]=df2[i].apply(lambda x:x.split("/")[1])


# In[166]:

new_rows=df1.append(df2)


# In[167]:

df_20_18.drop(hyb_18.index,inplace=True)


# In[168]:

df_20_18=df_20_18.append(new_rows)


# In[169]:

df_20_18.air_pollution_score = df_20_18.air_pollution_score.astype(float)


# In[170]:

df_20_08.info()


# In[171]:

df_20_18.info()


# Fix city_mpg, hwy_mpg, cmb_mpg datatypes
# 2008 and 2018: convert string to float

# In[172]:

df_20_08['city_mpg']=df_20_08['city_mpg'].astype(float)


# In[173]:

df_20_08['hwy_mpg']=df_20_08['hwy_mpg'].astype(float)


# In[174]:

df_20_08['cmb_mpg']=df_20_08['cmb_mpg'].astype(float)


# In[175]:

df_20_08.info()


# In[176]:

df_20_18['city_mpg']=df_20_18['city_mpg'].astype(float)


# In[177]:

df_20_18['hwy_mpg']=df_20_18['hwy_mpg'].astype(float)


# In[178]:

df_20_18['cmb_mpg']=df_20_18['cmb_mpg'].astype(float)


# In[179]:

df_20_18.info()


# Fix greenhouse_gas_score datatype

# In[184]:

df_20_08['greenhouse_gas_score'] = df_20_08['greenhouse_gas_score'].astype(int)


# In[185]:

df_20_08.info()


# # step(4):-Exploring with Visuals

# q(1):-Compare the distributions of greenhouse gas score in 2008 and 2018.

# In[186]:

df_20_08['greenhouse_gas_score'].hist()


# In[187]:

df_20_18['greenhouse_gas_score'].hist()


# A(1):-Distribution for 2008 is more skewed to the left.

# q(2):-How has the distribution of combined mpg changed from 2008 to 2018?

# In[189]:

df_20_08['cmb_mpg'].hist()


# In[190]:

df_20_18['cmb_mpg'].hist()


# A(2):-Became much more skewed to the right

# q(3):-Describe the correlation between displacement and combined mpg

# In[191]:

df_20_08.plot(x='displ',y='cmb_mpg',kind='scatter')


# In[192]:

df_20_18.plot(x='displ',y='cmb_mpg',kind='scatter')


# A(3):-Negative correlation

# q(4):-Describe the correlation between greenhouse gas score and combined mpg.

# In[193]:

df_20_08.plot(x='greenhouse_gas_score',y='cmb_mpg',kind='scatter')


# In[194]:

df_20_18.plot(x='greenhouse_gas_score',y='cmb_mpg',kind='scatter')


# A(4):-Positive correlation

# # step(5):- Conclusions

# # Q1: Are more unique models using alternative fuels in 2018 compared to 2008? By how much?

# Let's first look at what the sources of fuel are and which ones are alternative sources

# In[196]:

df_20_08.fuel.value_counts()


# In[197]:

df_20_18.fuel.value_counts()


# Looks like the alternative sources of fuel available in 2008 are CNG and ethanol, and those in 2018 ethanol and electricity. (You can use Google if you weren't sure which ones are alternative sources of fuel!)

# In[198]:

# how many unique models used alternative sources of fuel in 2008
alt_08 = df_20_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
alt_08


# In[205]:

# how many unique models used alternative sources of fuel in 2018
alt_18 = df_20_18.query('fuel in ["Ethanol", "Electricity"]').model.nunique()
alt_18


# Since 2008, the number of unique models using alternative sources of fuel increased by 24

# In[202]:

# total unique models each year
total_08 = df_20_08.model.nunique()
total_18 = df_20_18.model.nunique()
total_08, total_18


# In[203]:

prop_08 = alt_08/total_08
prop_18 = alt_18/total_18
prop_08, prop_18


# # Q2: How much have vehicle classes improved in fuel economy?

# Let's look at the average fuel economy for each vehicle class for both years

# In[206]:

veh_08 = df_20_08.groupby('veh_class').cmb_mpg.mean()
veh_08


# In[207]:

veh_18 = df_20_18.groupby('veh_class').cmb_mpg.mean()
veh_18


# In[208]:

# how much they've increased by for each vehicle class
inc = veh_18 - veh_08
inc


# # Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?

# We can analyze this by filtering each dataframe by SmartWay classification and exploring these datasets

# In[211]:

# smartway labels for 2008
df_20_08.smartWay.unique()


# In[212]:

# get all smartway vehicles in 2008
smart_08 = df_20_08.query('smartWay == "yes"')


# In[213]:

# explore smartway vehicles in 2008
smart_08.describe()


# In[215]:

# smartway labels for 2018
df_20_18.smartWay.unique()


# In[217]:

# get all smartway vehicles in 2018
smart_18 = df_20_18.query('smartWay in ["Yes", "Elite"]')


# In[218]:

smart_18.describe()

