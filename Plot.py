import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header('Datas')
    st.write(df.head())

def plot(dataframe):
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Group'],y=df['sold'])
    ax.set_xlabel('Group')
    ax.set_ylabel('Sold')
    st.pyplot(fig)

    a = df['Group']
    b= df['sold']
    ax.plot(a,b)
    st.pyplot(fig)

st.title('Grocery Mart')
st.text('This is a wggeb app to explore Grocery data.')

st.sidebar.title('Navigation')
uploaded_file = st.sidebar.file_uploader('Upload your file here')

options = st.sidebar.radio('Pages',options=['Home','Data Statistics','Data','Plot'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data Downloaded Successfully")

if options == 'Data Statistics':
    stats(df)
elif options == 'Data':
    data_header(df)
elif options == 'Plot':
    plot(df)
# elif options == 'Home':
#     if df!=None:
#         st.success("Data Downloaded Successfully")
