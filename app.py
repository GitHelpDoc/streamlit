from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieur1(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding = ("https://lottie.host/98aef226-3e13-4ab4-a58b-39cb8f667e70/L4dsL2ZKSf.json")
img_lottie_animation = Image.open("gitpodimage.jpg")
with st.container():
    st.subheader("Hi, I'm Rekha working with my Streamlit experts here.:wave:")
    st.title ("I'm working on becoming a Streamlit Evangelist.")
    st.write("I'm passionate about learning Python, VBA, GenAI and everything else related to machine learning on Planet Earth.")
    st.write("https://streamlit.io/")

    st.markdown("""
    <style>
    .normal-font {
        font-size:20px !important;
    }
    .title-font {
        font-size:30px !important;
    }

    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="title-font">I\'m working on becoming a Streamlit Evangelist.', unsafe_allow_html=True)


    st.markdown('<p class="normal-font">We\'re a passionate team wanted to learn and advance in Python to be more effective and efficient.<br> <a href="https://streamlit.io/"> Learn more about Streamlit.', unsafe_allow_html=True)
#st.write("We're a passionate team wanted to learn and advance in Python to be more effective and efficient.")
#st.write("[Learn more >] (https://streamlit.io)")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
        My hobbies:
        - Gardening
        - Running
        - Traveling
        - Swimming
        
        If this sounds interesting, you all can pick up these hobbies.""")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)    
    with text_column:
        st.subheader("Integrate Lottie animations inside Streamlit.")
        st.write("""
        Learn how to use Lottie files in Streamlit!
        Animations make website more engaging and fun.
        I'll show you exactly how to do it.
        """)
        st.markdown("[Watch video...](https://www.youtube.com/watch?v=VqgUkExPvLY)")

