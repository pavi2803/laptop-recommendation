# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:33:56 2021

@author: Pavithra
"""

import streamlit as st
import time
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as pll
import plotly.graph_objects as go


import pandas as pd

#title 
st.markdown("<h1 style='text-align: center, color: purple'>Laptop Recommendation</h1>", unsafe_allow_html=True)

         
st.image('lapic.png',width=100)
         
#fetching data         
         
DATA_URL = ('C:/Users/Pavithra/Documents/DATASETS/laptops.csv')
data = pd.read_csv(DATA_URL)
data = data.drop('Unnamed: 0',axis=1)


def load_data(nrows):
    newdata = data.head(nrows)
    return newdata

prices = data['Price_euros']
company = data['Company']



def fetch_details(a,b,c):
    #st.text("Enter the Company of which you want to go for ")
    #user_cmp = st.text_input("Enter :")
    
    compdata = data.query('Company == "{}" and TypeName == "{}" and Ram == "{}"'.format(a
                                                                        ,b,c))
    return compdata


def fetch_details_cpu(a,b,c,d):
    #st.text("Enter the Company of which you want to go for ")
    #user_cmp = st.text_input("Enter :")
    
    compdatacpu = data.query('Company == "{}" and TypeName == "{}" and Ram == "{}" and Cpu == "{}"'.format(a
                                                                        ,b,c,d))
    return compdatacpu
    
def color_positive_green(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: green'` for positive
    strings, black otherwise.
    """
    if val > 100000:
        color = 'green'
    else:
        color = 'black'
    return 'color: %s' % color
  
    
    
    
    
optioncmp = st.selectbox('Choose the Brand/Company of Laptop You like to go for :',
    ('Apple', 'HP', 'Acer','Asus','Dell','Lenovo','Chuwi','MSI','Microsoft','Toshiba','Huawei','Xiaomi','Vero','Razer','Mediacom','Samsung','Google','Fujitsu','LG'))

optiontype = st.selectbox('Choose the Type of Laptop :', ('Ultrabook','Notebook','Netbook','Gaming','2 in 1 Convertible','Workstation'))


optionram = st.selectbox('Choose Your Ram Preference :', ('2GB','4GB','6GB','8GB','12GB','16GB','24GB','32GB','64GB'))


if(st.button('Submit')):
    
    askeddata = fetch_details(optioncmp,optiontype,optionram)
    askeddata = askeddata.drop_duplicates()
    mydata=askeddata
 
   
    
    
    if(askeddata.empty):
        st.write("No Recommendation Found for ",optioncmp," ",optiontype, "with ", optionram, " Ram.")
    
    if((askeddata.empty)==False):
        
        st.write('Products available for your choices are :')
        unique_products = askeddata['Product']
        unique_products = unique_products.unique()
        st.write(unique_products)
        
        
        
        dfmax = askeddata[askeddata['Price_in_Rupees']==askeddata['Price_in_Rupees'].min()]
        dfmin = askeddata[askeddata['Price_in_Rupees']==askeddata['Price_in_Rupees'].max()]
        st.write('Product with Maximum Price :')
        st.write(dfmax['Product'])
        
        st.write('Product with Minimum Price :')
        st.write(dfmin['Product'])
        
        st.write('Price Range in Rupees')
        st.write('From Minimum ₹',askeddata['Price_in_Rupees'].min(),'to Maximum ₹',askeddata['Price_in_Rupees'].max() )
        
        st.write('In Dollars:')
        st.write('From Minimum $',askeddata['Price_in_Dollars'].min(), 'to Maximum $', askeddata['Price_in_Dollars'].max())
        
        st.write('In Euros:')
        st.write('From Minimum €',askeddata['Price_euros'].min(), 'to Maximum €', askeddata['Price_euros'].max())
    
        
        st.write('Memory and Cpu Combinations Available :')
        colsprice = askeddata['Price_in_Rupees']
        colsinches=askeddata['Inches']
        colsRes = askeddata['ScreenResolution']
        colsprice1 = askeddata['Price_in_Dollars']
        colsprice2 = askeddata['Price_euros']
        colsprod= askeddata['Product']
        colscpu=askeddata['Cpu']
        colsmemo=askeddata['Memory']
        collist = [colsprod,colscpu,colsmemo,colsprice,colsprice1,colsprice2]
        cpumem = pd.concat(collist,axis=1)
        #cpumemuni = cpumem.unique()
        cpumem = cpumem.style.set_properties(**{'background-color': 'yellow'}, subset=['Price_in_Rupees'])
        
        st.write(cpumem)
        
        
        st.write('Display:')
        st.write('Screen Inches and Resolution Combinations:')
    
        
        collist1 = [colsprod,colsinches,colsRes,colsprice,colsprice1,colsprice2]
        
        
        sires = pd.concat(collist1,axis=1)
        
        sires = sires.style.set_properties(**{'background-color': 'yellow'}, subset=['Price_in_Rupees'])
        
        st.write(sires) 
        
        
        
        
        
       
        
        
        #if(st.button('explore my product')):
         #   st.write('You have selected ', optionprod)
            
          #  prod_info = mydata.query('Product == "{}"'.format(optionprod))
            
           # st.write(prod_info)
        
        #if(st.button('Explore my Product')):
     





# Notify the reader that the data was successfully loaded.
