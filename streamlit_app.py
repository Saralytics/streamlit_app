import streamlit 
import pandas 

streamlit.title("My parent's healthy diner")
streamlit.header("Breakfast menu")                  
streamlit.header("Build your own fruit smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
