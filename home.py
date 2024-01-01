import streamlit as st

def load_view():
    
    st.markdown("<h1 style='text-align: Left; color: Black; margin-top: -80px;'><u>E-Panchayat Framework</u></h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <h3 style='text-align: Left; color: Black;'>Key capabilities for Translator</h3>
    
    """, unsafe_allow_html=True)

    st.markdown("""<p1 style='text-align: Left; color: Black;'>
    <ul>
        <li>Broad language support Translate between indian and english languages.</li>
        <li>Proven translation models Powered by the same models used by the Meta NLLB app's online mode.</li>
        <li>Dynamic model management Keep on-device storage requirements low by dynamically downloading and managing language packs.</li>
        <li>Runs on the device Translations are performed quickly, and don't require you to send users' text to a remote server.</li>"""
    , unsafe_allow_html=True)

    st.markdown("""
    <h3 style='text-align: Left; color: Black;'>Key capabilities for Chatbot</h3>
    
    """, unsafe_allow_html=True)

    st.markdown("""<p1 style='text-align: Left; color: Black;'>
    <ul>
        <li>The Chatbot will provide assistance in bridging govt services and schemes.</li>
        <li>Personal touch to conversations – Chatbots are intelligent. 
            They have the potential to analyze responses based on customer details/history/demographics, 
            facilitating personal communication while driving the conversation.</li>
        <li>One To One Response – Customers are looking for immediate one-to-one responses. 
            Chatbots do precisely that, enhancing the customer’s experience.</li>
        <li>Runs on the device Translations are performed quickly, and don't require you to send users' text to a remote server.</li>"""
    , unsafe_allow_html=True)


