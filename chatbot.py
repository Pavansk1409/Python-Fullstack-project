import streamlit as st
import chat as bot
def load_view():
    st.markdown("""<h3 style='text-align: Left; color: Black; margin-top: -80px;'>NLP Bot is an NLP conversational chatbot..</h3>
    """, unsafe_allow_html=True)
    

            
    user_input = get_text()
    if True:
        st.text_area("Bot:", value=bot.results(user_input), height=200, max_chars=None, key=None)
    
def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text


