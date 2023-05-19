import streamlit
import pandas

streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Create your own smoothie!')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



selected_fruits = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = selected_fruits.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)
                  
