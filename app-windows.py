import streamlit as st
import yt_dlp
import os

# Set up the web page configuration
st.set_page_config(page_title="Media Downloader", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0f172a; }
    h1 { color: #f8fafc !important; font-weight: 800 !important; }
    .stButton>button { 
        background-color: #6366f1 !important; 
        color: white !important; 
        border-radius: 10px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("Media Download Dashboard")
st.caption("Local Network Media Automation Dashboard")
st.markdown("Paste a video link below to download it in full HD directly to your machine.")


# 1. Create a text input box for the URL

st.subheader("Extract HD videos from YouTube and more!")
video_url = st.text_input("🔗 Video URL:", placeholder="https://www.youtube.com/watch?v=...")

# 2. Create a clean click button
if st.button("Download Video", type="primary"):
    if not video_url:
        st.warning("Please paste a valid URL first!")
    else:
        # Show a loading spinner while the backend works
        with st.spinner("⏳ Connecting to server and downloading... please wait."):

            # Use the exact same settings we perfected earlier
            save_path = "media downloads/videos"
            settings = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                'fmpeg_location':'C:/ffmpeg/bin'
            }

            try:
                # Run the yt-dlp engine
                with yt_dlp.YoutubeDL(settings) as ydl:
                    ydl.download([video_url])

                # Show a beautiful success message on the screen
                st.success("✅ Success! Your video has been downloaded to the 'my_downloads' folder.")
                st.balloons() # Fun little celebratory effect

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
