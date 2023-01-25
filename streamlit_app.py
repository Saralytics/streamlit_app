import streamlit 
import pandas 
import requests 
import snowflake.connector

streamlit.title("My parent's healthy diner")
streamlit.header("Breakfast menu")                  
streamlit.header("Build your own fruit smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.title("Fruity Vice Fruit Advice")

fruit_choice = streamlit.text_input("What fruit do you want information about?","Kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

add_fruit = streamlit.text_input("What fruit do you want to add?","Write fruit name here")
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ({})".format(add_fruit))

streamlit.text("Thank you for adding {}".format(add_fruit))

