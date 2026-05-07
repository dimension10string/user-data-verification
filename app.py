import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Secure Portal", page_icon="🌴", layout="wide")

# --- Custom Styling for the "Elegant Cayman" Look ---
def local_css():
    st.markdown("""
        <style>
        /* Import Elegant Handwriting Font */
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300&display=swap');

        /* Main Background: Tropical Gradient */
        .stApp {
            background: linear-gradient(135deg, #fdfcf0 0%, #a2dce7 100%);
        }

        /* Birthday Header (The Handwriting) */
        .birthday-text {
            font-family: 'Great Vibes', cursive;
            color: #00768e;
            text-align: center;
            font-size: clamp(60px, 10vw, 120px);
            font-weight: 400;
            padding-top: 20px;
            margin-bottom: 0px;
        }

        /* The Letter Box */
        .personal-wish {
            font-family: 'Montserrat', sans-serif;
            font-size: 20px;
            text-align: center;
            color: #2c3e50;
            line-height: 1.8;
            margin: 0 auto;
            max-width: 750px;
            background: rgba(255, 255, 255, 0.4);
            padding: 50px;
            border-radius: 30px;
            border: 1px solid rgba(255,255,255,0.5);
        }

        /* Styling the 'Hint' text */
        .stMarkdown p {
            font-family: 'Montserrat', sans-serif;
        }
        
        /* Clean Buttons */
        .stButton>button {
            border-radius: 50px;
            border: 2px solid #00768e;
            background-color: transparent;
            color: #00768e;
            padding: 10px 30px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #00768e;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Logic ---
if not st.session_state.authenticated:
    st.title("📂 Archive Retrieval System")
    st.write("Authorized access only. Please verify your credentials.")
    
    with st.form("login_form"):
        name = st.text_input("Name")
        favorite_memory = st.text_input("Access Key (Vacation Location)")
        submit = st.form_submit_button("Access Files")
        
        if submit:
            if name.strip().lower() != "" and "cayman" in favorite_memory.lower():
                with st.spinner("Syncing..."):
                    time.sleep(1.5)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Access Denied.")

else:
    # --- THE ELEGANT REVEAL ---
    local_css()
    st.balloons()
    
    # Hero Image: A stunning Cayman view
    st.image("https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop", 
             use_container_width=True)
    
    # The Handwriting Header
    st.markdown('<p class="birthday-text">Happy Birthday, [Name]!</p>', unsafe_allow_html=True)
    
    # The Letter
    st.markdown(
        """
        <div class="personal-wish">
            <i>My Dearest [Name],</i> <br><br>
            I wanted to build something as beautiful and intentional as the life we've created together. 
            You are the heart of our home and the light in my every day. <br><br>
            Thank you for being the most incredible partner. 
            I hope this year brings you as much joy as you give to everyone around you. <br><br>
            <b>I love you beyond measure.</b>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Final Surprise Hint
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h3 style='text-align: center; color: #00768e; font-family: Montserrat;'>Now, go check the kitchen...</h3>", unsafe_allow_html=True)
    
    if st.button("End Session"):
        st.session_state.authenticated = False
        st.rerun()
