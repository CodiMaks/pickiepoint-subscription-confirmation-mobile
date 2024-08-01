import streamlit as st

st.set_page_config("Subscription confirmation", "pickiepoint_logo_profile_picture.png")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Thanks for your subscription")
st.image("tick.png", width=300)
st.subheader("You're all set")
st.subheader("You can return to the website")
st.subheader("Start picking the main points")
st.image("pickiepoint_logo_profile_picture.png", use_column_width=True)
