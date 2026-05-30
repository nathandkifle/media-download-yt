🚀 Features

- Dual-Engine Architecture: Uses `yt-dlp` for raw high-definition video extraction.
- Local Network Broadcasting: Formatted to host locally (`0.0.0.0`) so it can be accessed seamlessly from mobile browsers, tablets, or other laptops on the same Wi-Fi.
- Automated Processing: Integrates system-level `FFmpeg` to cleanly merge separate high-res audio and video streams into standard `.mp4` and `.mp3` containers.
- Smart Metadata Embedding: Automatically fetches and embeds official album artwork, artist tags, and track information directly into downloaded audio files.

 🛠️ Tech Stack

- Language: Python 3
- Frontend/UI: Streamlit Framework
- Core Engines: `yt-dlp` & 
- Media Processor: FFmpeg

Instructions to run locally

Step 1
Clone the repository:
  git clone https://github.com/nathandkifle/media-download-yt
  cd media-download-yt

Step 2
Install the required Python modules and ffmpeg
  pip install streamlit yt-dlp 
  ffmpeg download for Windows: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z (unzip in C:\)
  ffmgeg install command with HomeBrew for Mac: brew install ffmpeg

Step 3
If on Windows:
  1. Search "Edit the system environment variables" in the Start menu and open it
     <img width="514" height="453" alt="image" src="https://github.com/user-attachments/assets/fd0c8271-a49d-45b7-ba74-47d1d9fb7d19" />

  2. Click on the Enviroment Variables button at the bottom
     <img width="273" height="310" alt="image" src="https://github.com/user-attachments/assets/6e834ad9-2378-49a8-8b7a-ea737ca1e981" />
  3. Under System Variables, click the "New Button"
     <img width="411" height="400" alt="image" src="https://github.com/user-attachments/assets/71580bc7-a893-4ae7-bf7e-0eb6d5977e43" />
  4. Paste this exact path: C:\ffmpeg\bin
     <img width="420" height="107" alt="image" src="https://github.com/user-attachments/assets/ba1710f6-6b59-47fd-9f6d-1918d4726048" />
  5. Click OK on all the windows and close them
If on Mac:
  No setup needed

Step 4:
If on Windows:
  In the command prompt type: streamlit run app-windows.py (if that doesn't work try python -m streamlit run app-windows.py)
  It should open to the Web UI
If on Mac:
In the terminal type: streamlit run app.py
It should open to the Web UI
