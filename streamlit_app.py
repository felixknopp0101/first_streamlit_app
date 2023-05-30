import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError
import requests

streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Create your own smoothie!')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

selected_fruits = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]

streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#new section

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information about it.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
 except URLError as e:
  streamlit.error()



streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruitload list contains:")
streamlit.dataframe(my_data_rows)

added_fruit = streamlit.text_input('What fruit would you like to add?', 'Kiwi')

my_cur.execute("insert into fruit_load_list values('from streamlit')")



                  
