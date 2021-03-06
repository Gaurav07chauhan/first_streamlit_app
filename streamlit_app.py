import streamlit


streamlit.title('My Parent New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#New Section to display fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#take the son version of the response and normalize it

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output It the screen as a table

streamlit.dataframe(fruityvice_normalized)
#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input ('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response  = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
import snowflake.connector 
