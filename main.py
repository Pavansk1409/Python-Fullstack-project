import streamlit as st
import utils as utl
from views import home,about, lbtranslation, translation, chatbot
import base64



def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)





st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()
set_background('img.jpeg')

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "about":
        about.load_view()
    elif route == "translation":
        translation.load_view()
    elif route == "lbtranslation":
        lbtranslation.load_view()
    elif route == "chatbot":
        chatbot.load_view()
    elif route == None:
        home.load_view()
        
navigation()