import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import pickle
import sklearn


path_to_model = 'Model/model.pkl'

pickled_model = pickle.load(open(path_to_model, 'rb'))
#selection = st.sidebar.radio("Navigation", ["Home", "About us"])
#image = Image.open('images/logo.jpg')
header = st.container()
prediction = st.container()
dataset = st.container()
data_viz = st.container()
#background-color: #070729;
#primary-color: #FF4B4B;
#secondary-background-color: #6F6F6F;
#text-color: #DADADA;
#font: sans-serif;


st.markdown("""
<style> 
.main {
   
    primary-color: #FF4B4B;
    secondary-background-color: #6F6F6F;
    text-color: #DADADA;
    font: sans-serif;
}
</style>
""", unsafe_allow_html=True
)
  

with header:
    #st.image(image)
    st.markdown("<h1 style='text-align: center; color: white;'>SEETHROUGHNYC</h1>", unsafe_allow_html=True)
     
with prediction:

    #option1:

    st.header("Try our model")
    sel_col, disp_col = st.columns(2) 

    input_year = sel_col.slider("Enter the year in which you want to predict the price of your property?", 
    min_value=2022, max_value=2100, value=2022, step=1)

    zipcode_input = sel_col.text_input("Enter the zipcode of the property", max_chars=5)

    sqft_input = sel_col.text_input("Enter the size of the property (sqft):")
    

   

    if sel_col.button("Calculate your prediction"):
 
        predictions = pickled_model.predict([[sqft_input, zipcode_input, input_year]])
        prediction = predictions[0]
        st.write("Price per square ft in " + str(input_year) + " with zipcode " + zipcode_input)
        disp_col.subheader("Price Predicted: $" + str(round(prediction,2)))
        disp_col.subheader("Price/Sqft: $" + str(round((prediction/int(sqft_input)), 2)))
       
    

    #option2: Input approx Gross sqft and neighborhood(which would be assigned a zipcode) and compare price prediction
    
 

with dataset:
    st.header("Dataset used")
    df_sales = pd.read_csv('data/nyc-rolling-sales.csv')
    st.write(df_sales.head())
    #change to statistics table to make it more visually appealing


   


with data_viz:
    st.header("More insights about our dataset")

    sel_col, disp_col = st.columns(2) 

    heatmap = Image.open('images/heatmap.jpg')
    sel_col.image(heatmap)

    borough_dist = Image.open('images/borough_dist.jpg')
    disp_col.image(borough_dist)

    avgp_borough = Image.open('images/avgp_borough.jpg')
    st.image(avgp_borough)
   


 





