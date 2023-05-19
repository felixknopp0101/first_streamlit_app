import streamlit
import pandas

streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('eggs and spinach')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.multiselect("Pick some fruits:", list my_fruit_list.index)

streamlit.dataframe(my_fruit_list)
                  
