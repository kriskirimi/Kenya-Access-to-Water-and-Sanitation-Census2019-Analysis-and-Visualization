# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:28:52 2020

@author: KIRIMI
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\KIRIMI\Documents\GitHub\Kenya-Access-to-Water-and-Sanitation-Census2019-Analysis-and-Visualization\Data\volume_4-table-2.15_chouseholds-by-main-source-of-drinking-water-area-of-residence-county-and-su.csv')

cols = (['Conventional Households', 'Pond(%)', 'Dam/Lake(%)', 
         'Stream/River', 'Protected Spring', 'Unprotected Spring', 
         'Protected Well', 'Unprotected  Well', 'Borehole/ Tube well',
         'piped into  dwelling', 'Piped to yard/ Plot', 'Bottled water', 
         'Rain/ Harvested water', 'Water Vendor', 
         'Public tap/ Standpipe','Not Stated'])
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df1 = df[df['County/ Sub-County'].str.contains('NAIROBI|MOMBASA')]
df1.set_index('County/ Sub-County', inplace=True)
df1.sort_values(by=['NAIROBI CITY'], 
                axis=1, ascending=False, inplace=True)
percent_to_population = lambda x:x/100* df1['Conventional Households']
df2=df1.iloc[:,1:].apply(percent_to_population)
df3 = df2.iloc[:,0:7].T

df3.columns=['Mombasa County Access to Water, Census 2019', 
             'Nairobi City Access to Water, Census 2019']

fig, axes= plt.subplots(1,2, figsize=(3,6))
plt.style.use('ggplot')
explode = (0.03, 0.03, 0.03, 0.03, 0.03,0.03, 0.03)

for ax, col in zip(axes, df3.columns):
    ax.pie(df3[col],labels=df3.index, radius=.85,explode=explode,autopct='%1.1f%%', wedgeprops=dict(width=.22))
    ax.set_title(col, fontsize=14)
plt.show()