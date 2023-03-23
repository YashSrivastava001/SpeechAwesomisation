import streamlit as st
from model import OpenAIModel
st.set_page_config(page_title="Speech Awesomisation", layout="wide")


def app():

    prediction = OpenAIModel()
    st.markdown(f'<h1 style="color:#157145;font-size:32px;">{"Welcome to Speech Awesomisation:"}</h1>', unsafe_allow_html=True)
    st.sidebar.markdown(f'<h1 style="color:#157145;font-size:24px;">{"Enter your OpenAI API key to get started!"}</h1>', unsafe_allow_html=True)
    api_key = st.sidebar.text_input("APIkey:", type="password", placeholder="sk-ExaMpleaPiKeY")

    def process_prompt(input):

        return prediction.model_prediction(input=input.strip(), api_key=api_key)

    if api_key:

        # Setting up the Title
        st.markdown(f'<h1 style="color:#57A773;font-size:48px;">{"Generate a speech using the words below:"}</h1>', unsafe_allow_html=True)

        
        input = st.text_area(
            "Input a general idea of what you want to talk about in your speech. Try to include all the important points you want to get across and please keep it between 200-400 words. Let's go!",
            height=300,
            placeholder="Enter your ideas for the speech here. Be creative ;)"
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")


