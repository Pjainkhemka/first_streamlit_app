import streamlit
import pandas
streamlit.title ( ' My parents healthy new diner')
streamlit.header ( ' Breakfast Menu ')
streamlit.text ( ' Omega 2 and Blueberry Oatmeal ')
streamlit.text (' Kale , Spinach , and Rocket Smoothie ')
streamlit.text (' Hrad Boiled Free Range Egg')

streamlit.header(' Buid your own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show )
  
