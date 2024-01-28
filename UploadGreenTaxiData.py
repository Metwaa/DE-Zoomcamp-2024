#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


pd.__version__


# In[4]:


df = pd.read_csv('csvfiles/green_tripdata_2019-09.csv', nrows=100)


# In[5]:


df.head()


# In[6]:


pip install Flask-SQLAlchemy


# In[6]:


from sqlalchemy import create_engine


# In[3]:


pip install psycopg2


# In[7]:


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[8]:


print(pd.io.sql.get_schema(df, name='green_taxi_data', con=engine))


# In[10]:


df_iter = pd.read_csv('csvfiles/green_tripdata_2019-09.csv', iterator=True, chunksize=100000)


# In[11]:


df = next(df_iter)


# In[12]:


df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


# In[13]:


df.head()


# In[14]:


df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')


# In[15]:


get_ipython().run_line_magic('time', "df.to_sql(name='green_taxi_data', con=engine, if_exists='append')")


# In[16]:


from time import time


# In[17]:


while True: 
    t_start = time()

    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    
    df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

    t_end = time()

    print('inserted another chunk, took %.3f second' % (t_end - t_start))


# In[18]:


df_zones = pd.read_csv('csvfiles/taxi+_zone_lookup.csv')


# In[19]:


df_zones.to_sql(name='zones', con=engine, if_exists='replace')


# In[ ]:




