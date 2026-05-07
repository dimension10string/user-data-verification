import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Authorized Access Only", page_icon="🔒", layout="wide")

# --- Custom Styling ---
def local_css():
    # Replace the URL below with your preferred background image (e.g., a beach or a photo of you two)
    bg_img = "https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop"
    
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        /* Full Page Background Image */
        .stApp {{
            background-image: url("{bg_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Hide Streamlit UI */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        .stDeployButton {{display:none;}}

        /* Glassmorphism Container for the Content */
        .glass-card {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 40px 20px;
            margin-top: 50px;
            text-align: center;
        }}

        /* The Birthday Header */
        .birthday-text {{
            font-family: 'Pinyon Script', cursive !important;
            color: #ffffff !important; /* White looks better on a photo bg */
            text-align: center !important;
            font-size: clamp(50px, 12vw, 90px) !important; 
            line-height: 1.1 !important;
            margin: 20px 0 !important;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }}

        /* The Letter Box */
        .personal-wish {{
            font-family: 'Montserrat', sans-serif !important;
            font-size: clamp(16px, 4vw, 20px) !important;
            text-align: center !important;
            color: #ffffff !important;
            line-height: 1.7 !important;
            margin: 0 auto !important;
            max-width: 90% !important;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
        }}

        /* Login Form Styling */
        .stForm {{
            background: rgba(255, 255, 255, 0.9) !important;
            padding: 30px;
            border-radius: 15px;
            max-width: 400px;
            margin: 100px auto 0 auto;
        }}
        </style>
    """, unsafe_allow_html=True)

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    local_css()
    # Keep the login screen clean and focused
    with st.form("login_form"):
        st.markdown("<h3 style='text-align: center; color: #333;'>Security Verification</h3>", unsafe_allow_html=True)
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token")
        submitted = st.form_submit_button("Authorize")
        
        if submitted:
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Authorizing..."):
                    time.sleep(1)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Authentication Error.")

else:
    local_css()
    st.snow()
    st.balloons()

    # Using a transparent 'Glass' container to hold the text over the background image
    st.markdown(f'''
        <div class="glass-card">
            <p style="letter-spacing: 4px; font-size: 11px; text-transform: uppercase; color: #ffffff; margin-bottom: 10px; opacity: 0.8;">A Dedicated Message</p>
            <div class="birthday-text">Happy Birthday, [Wife's Name]</div>
            <div class="personal-wish">
                <br>
                <i style="font-size: 24px;">My Dearest [Wife's Name],</i> <br><br>
                I built this corner of the internet to remind you how deeply you are loved. 
                You make every ordinary day feel extraordinary. <br><br>
                May your day be as serene as a Cayman sunrise. <br><br>
                <b style="color: #e0f7fa;">Your surprise is waiting for you in the kitchen.</b><br><br>
                <span style="font-size: 32px; font-family: 'Pinyon Script';">Love, [Your Name]</span>
            </div>
        </div>
    ''', unsafe_allow_html=True)
