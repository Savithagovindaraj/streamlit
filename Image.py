import streamlit as st

tab,tab1, tab2, tab3 = st.tabs(["Nature","Cat", "Dog", "Owl"])

with tab:
   st.header("Nature")
   st.image("https://i0.wp.com/picjumbo.com/wp-content/uploads/beautiful-nature-mountain-scenery-with-flowers-free-photo.jpg?w=600&quality=80")
   st.image("https://cdn.pixabay.com/photo/2014/02/27/16/10/flowers-276014_640.jpg")
with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200,use_column_width=1)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
