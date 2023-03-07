import streamlit
import pandas
streamlit.title ( ' My parents healthy new diner')
streamlit.header ( ' Breakfast Menu ')
streamlit.text ( ' Omega 2 and Blueberry Oatmeal ')
streamlit.text (' Kale , Spinach , and Rocket Smoothie ')
streamlit.text (' Hrad Boiled Free Range Egg')

streamlit.header(' Buid your own fruit smoothie')
my_fruit_list = pandas.read_csv(pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
                                streamlit.dataframe(my_fruit_list)
  
