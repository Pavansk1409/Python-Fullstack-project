import streamlit as st
from io import StringIO
import os
import base64
import speech_recognition as sr
import text2audio as ta
from transformers import AutoTokenizer , AutoModelForSeq2SeqLM, pipeline



class translate():
    def __init__(self) -> None:
        t = '../model600/tokenizers'
        m = '../model600/model'
        self.tokenizer = AutoTokenizer.from_pretrained(t)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(m)

    def getres(self, sentence, src, dest):
        translator = pipeline('translation',model=self.model, tokenizer=self.tokenizer, src_lang=src,tgt_lang=dest,max_length = 400)
        res = translator(sentence)[0]
        print(res)
        return res

def load_view():
    st.markdown("<h1 style='text-align: left; color: Black;'>Offline Translator</h1>", unsafe_allow_html=True)

    option_src = st.selectbox(
    'Select Select Languge you want to translate',
    ('Kannada', 'Sanskrit', 'Hindi', 'Marati', 'Telugu', 'French', 'English'))

    sentence = st.text_input(label='Enter Text')
    
    option_dest = st.selectbox(
    'Select Languge you want to translate to',
    ('Kannada', 'Sanskrit', 'Hindi', 'Marati', 'Telugu', 'French', 'English'))

    
    lang_code = {
        'Kannada' : 'kan_Knda',
        'Sanskrit' : 'san_Deva',
        'Hindi' : 'hin_Deva',
        'Marati' : 'mar_Deva',
        'Telugu' : 'tel_Telu',
        'French' : 'fra_Latn',
        'English' : 'eng_Latn'        
    }

    src = lang_code[option_src]
    dest = lang_code[option_dest]
    if st.button('Say hello'):
        res = trans.getres(sentence,src,dest)
        st.text_area(value=res, height=200, max_chars=None, key=None,label="Result")

trans = translate()