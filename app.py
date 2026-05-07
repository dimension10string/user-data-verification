import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Authorized Access Only", page_icon="🔒", layout="wide")

# --- Custom Styling (The "Luxury Boutique" CSS) ---
def local_css():
    st.markdown("""
        <style>
        /* Import Elegant Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        /* Background: Soft Tropical Gradient */
        .stApp {
            background: radial-gradient(circle, #ffffff 0%, #e0f7fa 100%);
        }

        /* Hide Streamlit Clutter */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}

        /* The Image: Rounded and Refined */
        .styled-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 45%; 
            border-radius: 200px 200px 20px 20px; 
            box-shadow: 0px 20px 40px rgba(0,0,0,0.1);
            border: 10px solid white;
            margin-top: 40px;
        }

        /* The Birthday Header: HUGE and Radiant */
        .birthday-text {
            font-family: 'Pinyon Script', cursive;
            color: #00768e;
            text-align: center;
            font-size: clamp(80px, 12vw, 150px);
            line-height: 1;
            margin-top: -30px;
            text-shadow: 2px 2px 8px rgba(0,118,142,0.1);
            animation: fadeIn 3s ease-in-out;
        }

        /* The Letter Box: Minimalist & Clean */
        .personal-wish {
            font-family: 'Montserrat', sans-serif;
            font-size: 20px;
            text-align: center;
            color: #2c3e50;
            line-height: 2;
            margin: 0 auto;
            max-width: 700px;
            padding: 20px 40px 60px 40px;
            animation: fadeIn 4s ease-in-out;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Styling the Login Form to look boring/work-related */
        .stForm {
            border: none !important;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            max-width: 500px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Logic Flow ---
if not st.session_state.authenticated:
    local_css()
    # "The Unsuspecting Front"
    st.markdown("<h2 style='text-align: center; font-family: Montserrat; color: #333;'>Internal Data Verification</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-family: Montserrat; color: #666;'>Please authenticate to sync family records.</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User Identification")
        u_token = st.text_input("Access Token (Vacation Memory)")
        submitted = st.form_submit_button("Verify & Sync")
        
        if submitted:
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Decrypting Archive..."):
                    time.sleep(2)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Authentication Error: Token not recognized.")

else:
    # --- THE LUXURY REVEAL ---
    local_css()
    
    # Persistent Atmosphere
    st.snow()
    for _ in range(3):
        st.balloons()
        time.sleep(0.3)

    # 1. Elegant Arched Image (Placeholder of Cayman, replace with yours if desired)
    st.markdown('<img src="https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop" class="styled-image">', unsafe_allow_html=True)
    
    # 2. Huge Calligraphy Name
    st.markdown(f'<p class="birthday-text">Happy Birthday, [Wife\'s Name]</p>', unsafe_allow_html=True)
    
    # 3. The Letter
    st.markdown(
        f"""
        <div class="personal-wish">
            <p style="letter-spacing: 5px; font-size: 11px; text-transform: uppercase; color: #00768e; margin-bottom: 20px;">For My Incredible Wife</p>
            <i>My Dearest [Wife's Name],</i> <br><br>
            I built this tiny corner of the internet just to remind you how deeply you are loved. 
            You are the quality optimizer of my life, the heart of our home, and my favorite adventure. <br><br>
            May your day be as beautiful and serene as a Cayman sunrise. <br><br>
            <b>Your surprise is waiting for you in the kitchen.</b><br>
            <span style="font-size: 16px;">Love, [Your Name]</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
