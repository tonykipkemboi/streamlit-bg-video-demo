import streamlit as st

# Page Configurations
st.set_page_config(layout="centered", 
                   page_icon="📺",
                   page_title="Background Video Demo")

# CSS for Background Video and Content Styling
def set_css():
    st.markdown("""
        <style>
            #myVideo {
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%; 
                min-height: 100%;
            }
            .content {
                position: fixed;
                bottom: 0;
                background: rgba(0, 0, 0, 0.5);
                color: #f1f1f1;
                width: 100%;
                padding: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

# Embed Background Video
def embed_video():
    video_link = "https://videos.pond5.com/binary-digital-tech-data-code-footage-009784511_main_xxl.mp4"
    st.markdown(f"""
        <video autoplay muted loop id="myVideo">
            <source src="{video_link}">
            Your browser does not support HTML5 video.
        </video>
    """, unsafe_allow_html=True)

# Main App Content
def main_content():
    st.title(":balloon: :red[Streamlit BG Video Demo] :balloon:")
    st.video("https://youtu.be/Z41pEtTAgfs")

    if st.checkbox(":red[Show BG Video Credits & Code]"):
        st.markdown("""
            :orange[**Video credits:**]          
            :green[Creator: @pond5] \n       
            :green[Description: abstract zeros and ones digital data code typing on screen. hd 1080 seamless loop..] \n 
            :green[License: Free for commercial use. No attribution required. [License Details](https://www.pond5.com/our-licenses)] \n
            :green[[URL to video](https://www.pond5.com/stock-footage/item/9784511-binary-digital-tech-data-code-compute)]
        """)
        st.markdown(":orange[**App Code 👇🏾**]")
        st.code('''
                import streamlit as st

                # Page Configurations
                st.set_page_config(layout="centered", 
                                page_icon="📺",
                                page_title="Background Video Demo")

                # CSS for Background Video and Content Styling
                def set_css():
                    st.markdown("""
                        <style>
                            #myVideo {
                                position: fixed;
                                right: 0;
                                bottom: 0;
                                min-width: 100%; 
                                min-height: 100%;
                            }
                            .content {
                                position: fixed;
                                bottom: 0;
                                background: rgba(0, 0, 0, 0.5);
                                color: #f1f1f1;
                                width: 100%;
                                padding: 20px;
                            }
                        </style>
                    """, unsafe_allow_html=True)

                # Embed Background Video
                def embed_video():
                    video_link = "https://videos.pond5.com/binary-digital-tech-data-code-footage-009784511_main_xxl.mp4"
                    st.markdown(f"""
                        <video autoplay muted loop id="myVideo">
                            <source src="{video_link}">
                            Your browser does not support HTML5 video.
                        </video>
                    """, unsafe_allow_html=True)

                # Main App Content
                def main_content():
                    st.title(":balloon: :red[Streamlit BG Video Demo] :balloon:")
                    st.video("https://youtu.be/Z41pEtTAgfs")

                    if st.checkbox(":red[Show BG Video Credits]"):
                        st.markdown("""
                            :orange[**Video credits:**]          
                            :green[Creator: @pond5] \n       
                            :green[Description: abstract zeros and ones digital data code typing on screen. hd 1080 seamless loop..] \n 
                            :green[License: Free for commercial use. No attribution required. [License Details](https://www.pond5.com/our-licenses)] \n
                            :green[[URL to video](https://www.pond5.com/stock-footage/item/9784511-binary-digital-tech-data-code-compute)]
                        """)

                if __name__ == "__main__":
                    set_css()
                    embed_video()
                    main_content()
            ''')

if __name__ == "__main__":
    set_css()
    embed_video()
    main_content()