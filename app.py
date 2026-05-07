import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="System Verification Portal", page_icon="🌴", layout="wide")

# --- Custom Styling for the "Cayman Reveal" ---
def local_css():
    st.markdown("""
        <style>
        /* Main Background */
        .stApp {
            background: linear-gradient(135deg, #e0f7fa 0%, #80deea 100%);
        }

        /* Birthday Header */
        .birthday-text {
            font-family: 'Georgia', serif;
            color: #00768e; /* Deep Cayman Teal */
            text-align: center;
            font-size: clamp(40px, 8vw, 80px);
            font-weight: bold;
            padding-top: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        /* The Message Box */
        .personal-wish {
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 22px;
            text-align: center;
            color: #2c3e50;
            line-height: 1.8;
            margin: 20px auto;
            max-width: 800px;
            background: rgba(255, 255, 255, 0.6);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }

        /* Making buttons look cleaner */
        .stButton>button {
            border-radius: 20px;
            background-color: #00768e;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Login Logic ---
if not st.session_state.authenticated:
    st.title("📂 User Profile Data Sync")
    st.info("System Security Protocol: Active")
    
    with st.form("login_form"):
        name = st.text_input("Full Name")
        favorite_memory = st.text_input("Secret Access Code (Hint: Our favorite vacation spot?)")
        submit = st.form_submit_button("Verify Identity & Sync Data")
        
        if submit:
            if name.strip().lower() != "" and "cayman" in favorite_memory.lower():
                with st.spinner("Decrypting personal data..."):
                    time.sleep(2)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Credential mismatch. Please try again.")

else:
    # --- THE REVEAL ---
    local_css()
    st.balloons()
    st.snow() # Adds a gentle shimmering effect
    
    # 1. Top Image (A beautiful Cayman Beach or a photo of you two)
    # You can replace this URL with a link to a photo of you two!
    st.image("https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop", 
             caption="Our Happy Place", use_container_width=True)
    
    # 2. The Header
    st.markdown('<p class="birthday-text">Happy Birthday, [Name]! ❤️</p>', unsafe_allow_html=True)
    
    # 3. The Letter
    st.markdown(
        """
        <div class="personal-wish">
            Dearest [Name], <br><br>
            I wanted to create something as unique and wonderful as you are. 
            You make every day feel like a sunset in the Caymans. <br><br>
            You’ve always been the <b>Quality Optimizer</b> of my life, making every moment 
            sweeter and every day easier just by being you. <br><br>
            I love you more than words (or code) can say.<br>
            <b>Here's to another year of us.</b>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # 4. The Gift Reveal (Optional)
    st.divider()
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.subheader("Your Birthday Surprise is waiting...")
        st.write("Check the kitchen counter! 🎁")
    
    if st.button("Secure Logout"):
        st.session_state.authenticated = False
        st.rerun()
