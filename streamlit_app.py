import streamlit as st
import webbrowser

st.set_page_config("Subscription confirmation", "pickiepoint_logo_profile_picture.png")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.caption('<span style="font-size:40px; font-weight:bold; color:white;">Thanks for your \u00A0\u00A0 subscription</span>', unsafe_allow_html=True)
st.write("")

st.image("tick.png", width=265)
st.write("")
st.write("")

st.caption('<span style="font-size:25px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0You are all set</span>', unsafe_allow_html=True)
st.caption('<span style="font-size:25px; font-weight:bold; color:white;">\u00A0\u00A0\u00A0\u00A0Start picking the main \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 points</span>', unsafe_allow_html=True)
st.subheader("")

return_to_website = st.button("Let's go", type="primary", use_container_width=True)
if return_to_website:
    webbrowser.open("https://pickiepoint-mobile.streamlit.app")

st.text("")
st.image("pickiepoint_logo_profile_picture.png", use_column_width=True)
