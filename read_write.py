# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:42:57 2022

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:59 2021

@author: Admin
"""
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:\\Users\\DELL\\Downloads\\python dataset\\User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:\\Users\\DELL\\Downloads\\python dataset\\User_Data.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:\\Users\\DELL\\Downloads\\python dataset\\User_Data.xlsx')

#df1 = pandas.read_excel('User_Data.xlsx')
#print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('C:\\Users\\DELL\\Downloads\\python dataset\\User_Data.xlsx')
