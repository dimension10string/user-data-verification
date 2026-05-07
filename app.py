import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Authorized Access Only", page_icon="🔒", layout="wide")

# --- Custom Styling ---
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        /* Clean White Background for that High-End Feel */
        .stApp {
            background-color: #ffffff;
        }

        /* Hide Streamlit Clutter */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}

        /* Full Width Mobile Image - No Rounding */
        .styled-image {
            display: block;
            width: 100vw !important; /* Full screen width */
            margin-left: calc(-50vw + 50%); /* Centers the full-width image */
            height: auto;
            border: none !important;
            border-radius: 0px !important;
            margin-top: -60px; /* Pulls it to the very top of the page */
            margin-bottom: 20px;
        }

        /* The Birthday Header */
        .birthday-text {
            font-family: 'Pinyon Script', cursive !important;
            color: #00768e !important;
            text-align: center !important;
            font-size: clamp(60px, 15vw, 100px) !important; 
            line-height: 1.2 !important;
            margin-top: 10px !important; 
            margin-bottom: 10px !important;
            padding: 0 10px;
        }

        /* The Letter Box */
        .personal-wish {
            font-family: 'Montserrat', sans-serif !important;
            font-size: clamp(18px, 4vw, 22px) !important;
            text-align: center !important;
            color: #2c3e50 !important;
            line-height: 1.8 !important;
            margin: 0 auto !important;
            max-width: 90% !important;
            padding: 10px 10px 100px 10px !important;
        }

        /* Login Form Styling */
        .stForm {
            border: 1px solid #eee !important;
            background: white;
            padding: 20px;
            border-radius: 10px;
            max-width: 400px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    local_css()
    st.markdown("<h3 style='text-align: center; font-family: Montserrat; color: #333; padding-top: 100px;'>Internal Data Verification</h3>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token")
        submitted = st.form_submit_button("Verify")
        
        if submitted:
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Authorizing..."):
                    time.sleep(1)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Error.")

else:
    local_css()
    st.snow()
    st.balloons()

    # 1. Full-Width Image (No borders, no rounding)
    st.markdown('<img src="https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop" class="styled-image">', unsafe_allow_html=True)
    
    # 2. Centered Name
    st.markdown(f'<div class="birthday-text">Happy Birthday, [Wife\'s Name]</div>', unsafe_allow_html=True)
    
    # 3. Message
    st.markdown(
        f"""
        <div class="personal-wish">
            <p style="letter-spacing: 4px; font-size: 11px; text-transform: uppercase; color: #00768e; margin-bottom: 15px;">A Birthday Message</p>
            <i style="font-size: 24px;">My Dearest [Wife's Name],</i> <br><br>
            I built this corner of the internet to remind you how deeply you are loved. 
            You make every ordinary day feel extraordinary. <br><br>
            May your day be as serene as a Cayman sunrise. <br><br>
            <b style="color: #00768e;">Your surprise is waiting for you in the kitchen.</b><br><br>
            <span style="font-size: 30px; font-family: 'Pinyon Script';">Love, [Your Name]</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
