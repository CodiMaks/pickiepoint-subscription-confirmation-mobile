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

st.caption('<span style="font-size:40px; font-weight:bold; color:white;">Thanks for your     subscription</span>', unsafe_allow_html=True)
st.write("")

st.image("tick.png", width=265)
st.write("")

st.header("You're all set")
st.header("Start picking the main points")
st.subheader("")

return_to_website = st.button("Let's go", type="primary", use_container_width=True)
st.text("")
st.image("pickiepoint_logo_profile_picture.png", use_column_width=True)
