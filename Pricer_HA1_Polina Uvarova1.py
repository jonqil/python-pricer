#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import date
import interpolation


# In[2]:


USD_rates = pd.read_csv('USD rates.csv', sep=',')
USD_rates['StartDate'] = pd.to_datetime(USD_rates['StartDate'], infer_datetime_format=True)
USD_rates['EndDate'] = pd.to_datetime(USD_rates['EndDate'], infer_datetime_format=True)
USD_rates=USD_rates.rename(columns = {'Unnamed: 1':'Market price'})
USD_rates.sort_values('EndDate', ascending = True)
USD_rates['Implied_rate_3m'] = USD_rates['Market price'].apply(lambda x: (100-x)/100)
USD_rates['EndDate2']=USD_rates['StartDate'].apply(lambda x: x.replace(x.year + 1))
USD_rates['days length']=USD_rates['EndDate']-USD_rates['StartDate']
USD_rates['days length'] = USD_rates['days length'] / pd.to_timedelta(1, unit='D')
USD_rates['Implied_rate_12m'] = USD_rates['Implied_rate_3m']*(USD_rates['days length']/360)
USD_rates['Implied_rate_12m'].astype(str)
USD_rates['Conv, adj'].astype(str)
USD_rates['Forward rate'] = USD_rates['Implied_rate_12m']+USD_rates['Conv, adj']
USD_rates['DF']=1/(1+USD_rates['Implied_rate_12m']*1)
plt.plot(USD_rates['EndDate2'][1:13],USD_rates['DF'][1:13],'-', USD_rates['EndDate2'][1:13], USD_rates['Forward rate'][1:13], '--' )
plt.title('Discount and forward curves (the greatest attempt)')
plt.legend(['Discount factor', 'forward rates'])
plt.show()

