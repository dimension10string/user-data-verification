import streamlit as st
import time

# ══════════════════════════════════════════════════════════════════════════════
#  ✏️  EDIT EVERYTHING IN THIS BLOCK BEFORE DEPLOYING
# ══════════════════════════════════════════════════════════════════════════════

WIFE_NAME  = "Ashal"       # e.g. "Sophia"
YOUR_NAME  = "Wakeel"      # e.g. "James"

# Secret 1 → the "Memory Archive Key" field  (she types your vacation spot)
SECRET_VACATION = "Wakeel"

# Secret 2 → the "Personal Passphrase" field
# Pick something only she knows: pet's name, year you met, first song, etc.
SECRET_PERSONAL = "ashalwakeel"    # ← Replace this

# ── Image file names ────────────────────────────────────────────────────────
# Upload ALL of these to your GitHub repo, then update the names below.
BG_IMAGE   = "bg.jpg"         # Full-page background (beach / sunset works beautifully)
HERO_IMAGE = "photo1.jpg"     # Main hero photo — landscape orientation preferred
PHOTO_2    = "photo2.jpg"     # Left photo in the duo grid
PHOTO_3    = "photo3.jpg"     # Right photo in the duo grid

# ── Your personal message ───────────────────────────────────────────────────
# Each variable is one "paragraph" in the letter. Edit freely.
MSG_1 = "Every single day with you has been the most beautiful accident I never planned for."
MSG_2 = ("You bring colour to every ordinary Tuesday, warmth to every grey morning, "
         "and laughter to every moment in between. I didn't know a person could make "
         "the world feel this much like home.")
MSG_3 = ("Thank you for being exactly who you are — endlessly kind, a little chaotic "
         "in the very best way, and completely, irreversibly irreplaceable.")
MSG_4 = "Today is entirely yours. I hope it feels as extraordinary as you make me feel every single day."
KITCHEN_NOTE = "Your birthday surprise is waiting for you in the kitchen."

# ── Optional: a romantic quote shown over the photo duo ────────────────────
PHOTO_QUOTE = "Every love story is beautiful, but ours is my favourite."

# ══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="FamilyVault — Secure Access",
    page_icon="🔒",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# ─────────────────────────────────────────────────────────────────────────────
#  L O G I N   P A G E   (convincingly boring)
# ─────────────────────────────────────────────────────────────────────────────
if not st.session_state.authenticated:

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

        html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif !important; }

        .stApp { background-color: #0e0f14 !important; }
        #MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }
        .block-container { padding-top: 0 !important; padding-bottom: 0 !important; }

        /* ── Top navigation bar ── */
        .topnav {
            background: #0a0b0f;
            border-bottom: 1px solid #1f2230;
            padding: 0 32px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100vw;
            margin-left: calc(-50vw + 50%);
        }
        .topnav-brand {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 12px;
            font-weight: 500;
            color: #e2e8f0;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .topnav-status {
            display: flex;
            gap: 24px;
            align-items: center;
        }
        .topnav-status span {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            color: #475569;
            letter-spacing: 1.5px;
        }
        .status-live {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #22d3ee !important;
        }
        .dot-live {
            width: 5px; height: 5px;
            border-radius: 50%;
            background: #22d3ee;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        /* ── Warning bar ── */
        .warn-bar {
            background: linear-gradient(90deg, #1e1b4b 0%, #1a1a2e 100%);
            border-bottom: 1px solid #312e81;
            padding: 9px 32px;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            color: #a5b4fc;
            letter-spacing: 2px;
            text-transform: uppercase;
            width: 100vw;
            margin-left: calc(-50vw + 50%);
        }

        /* ── Main login card ── */
        .lcard-wrap { max-width: 520px; margin: 56px auto 0; }
        
        .lcard-head {
            background: #13141a;
            border: 1px solid #1f2230;
            border-bottom: none;
            border-radius: 6px 6px 0 0;
            padding: 28px 32px 24px;
        }
        .lcard-head h1 {
            font-family: 'IBM Plex Sans', sans-serif;
            font-size: 17px;
            font-weight: 600;
            color: #f1f5f9;
            margin: 0 0 6px;
            letter-spacing: 0.3px;
        }
        .lcard-head p {
            font-size: 12px;
            font-weight: 300;
            color: #475569;
            margin: 0;
            line-height: 1.6;
        }

        .lcard-body {
            background: #101117;
            border: 1px solid #1f2230;
            border-top: none;
            border-radius: 0 0 6px 6px;
            padding: 28px 32px 32px;
        }

        /* ── Field overrides ── */
        [data-testid="stForm"] { background: transparent !important; border: none !important; padding: 0 !important; }
        
        .stTextInput label {
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 10px !important;
            font-weight: 500 !important;
            letter-spacing: 2px !important;
            text-transform: uppercase !important;
            color: #64748b !important;
        }
        .stTextInput > div > div > input {
            background: #0a0b0f !important;
            border: 1px solid #1f2230 !important;
            border-radius: 4px !important;
            color: #cbd5e1 !important;
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 13px !important;
            padding: 10px 14px !important;
        }
        .stTextInput > div > div > input::placeholder { color: #334155 !important; }
        .stTextInput > div > div > input:focus {
            border-color: #4f46e5 !important;
            box-shadow: 0 0 0 2px rgba(79,70,229,0.2) !important;
            background: #0d0e16 !important;
        }

        /* ── Submit button ── */
        [data-testid="stFormSubmitButton"] > button {
            background: #4f46e5 !important;
            color: #fff !important;
            border: none !important;
            border-radius: 4px !important;
            width: 100% !important;
            padding: 13px !important;
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 11px !important;
            letter-spacing: 3px !important;
            text-transform: uppercase !important;
            font-weight: 500 !important;
            margin-top: 6px !important;
            transition: background 0.2s, box-shadow 0.2s !important;
        }
        [data-testid="stFormSubmitButton"] > button:hover {
            background: #4338ca !important;
            box-shadow: 0 0 20px rgba(79,70,229,0.35) !important;
        }

        /* ── Progress bar ── */
        .stProgress > div > div {
            background: #4f46e5 !important;
        }
        .stProgress {
            margin-top: 12px !important;
        }

        /* ── Error ── */
        [data-testid="stAlert"] {
            background: rgba(239,68,68,0.08) !important;
            border: 1px solid rgba(239,68,68,0.25) !important;
            border-radius: 4px !important;
            color: #fca5a5 !important;
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 12px !important;
        }

        /* ── Footer ── */
        .lfooter {
            text-align: center;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 9px;
            color: #1e293b;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 28px;
            padding-bottom: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Top nav
    st.markdown("""
        <div class="topnav">
            <div class="topnav-brand">🔒 FamilyVault™</div>
            <div class="topnav-status">
                <span class="status-live"><span class="dot-live"></span>LIVE</span>
                <span>NODE: EU-WEST-2</span>
                <span>v4.2.1</span>
            </div>
        </div>
        <div class="warn-bar">
            ⚑ &nbsp; Authentication required — unauthorised access attempts are logged and reported
        </div>
    """, unsafe_allow_html=True)

    # Login card (centred via columns)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        st.markdown("""
            <div class="lcard-head">
                <h1>Identity Verification</h1>
                <p>All four fields are required. Your session will expire after 30 minutes of inactivity.</p>
            </div>
            <div class="lcard-body">
        """, unsafe_allow_html=True)

        with st.form("vault_login"):
            c1, c2 = st.columns(2)
            with c1:
                uid = st.text_input("Staff ID", placeholder="e.g. FAM-2024-001")
            with c2:
                dept = st.text_input("Department", placeholder="e.g. HOME-OPS")

            mem_key   = st.text_input("Memory Archive Key",
                                      placeholder="A place that holds everything")
            passphrase = st.text_input("Personal Passphrase",
                                       placeholder="Something only you would know",
                                       type="password")

            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("▶  VERIFY IDENTITY & DECRYPT ARCHIVE")

            if submitted:
                valid = (
                    uid.strip() != "" and
                    dept.strip() != "" and
                    SECRET_VACATION.lower() in mem_key.lower() and
                    SECRET_PERSONAL.lower() in passphrase.lower()
                )
                if valid:
                    bar = st.progress(0)
                    msgs = [
                        "Verifying credentials...",
                        "Establishing encrypted tunnel...",
                        "Decrypting personal archive...",
                    ]
                    for i, msg in enumerate(msgs):
                        with st.spinner(msg):
                            for p in range(i * 33, min((i + 1) * 33, 100), 3):
                                time.sleep(0.05)
                                bar.progress(p)
                    bar.progress(100)
                    time.sleep(0.4)
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("⚠️  Authentication failed — credentials do not match records on file.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <div class="lfooter">
            FamilyVault™ &nbsp;·&nbsp; AES-256 Encrypted &nbsp;·&nbsp;
            ISO 27001 Compliant &nbsp;·&nbsp; All sessions monitored
        </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  R E V E A L   P A G E   (luxury reveal)
# ─────────────────────────────────────────────────────────────────────────────
else:
    # Streamlit balloons (per your request — keeping them, removing snow)
    st.balloons()

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Raleway:wght@200;300;400&display=swap');

        /* ── Global reset ── */
        .stApp {{
            background-image: url("app/static/{BG_IMAGE}");
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
        }}
        #MainMenu, footer, header, .stDeployButton {{ visibility: hidden; display: none; }}
        .block-container {{
            padding: 0 !important;
            max-width: 100% !important;
        }}

        /* ── Animations ── */
        @keyframes riseUp {{
            from {{ opacity: 0; transform: translateY(40px); }}
            to   {{ opacity: 1; transform: translateY(0);    }}
        }}
        @keyframes fadeSlowly {{
            from {{ opacity: 0; }}
            to   {{ opacity: 1; }}
        }}
        @keyframes goldPulse {{
            0%, 100% {{ opacity: 0.85; text-shadow: 0 0 20px rgba(255,215,0,0.3); }}
            50%       {{ opacity: 1;   text-shadow: 0 0 35px rgba(255,215,0,0.6); }}
        }}

        /* ────────────────────────────────────────────
           HERO SECTION
        ──────────────────────────────────────────── */
        .hero-section {{
            position: relative;
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            overflow: hidden;
            max-height: 94vh;
            display: flex;
            align-items: flex-end;
            justify-content: center;
        }}
        .hero-section img {{
            width: 100%;
            height: 94vh;
            object-fit: cover;
            object-position: center 20%;
            display: block;
        }}
        /* Scrim: transparent at top, rich black at bottom */
        .hero-scrim {{
            position: absolute;
            inset: 0;
            background: linear-gradient(
                to bottom,
                rgba(0,0,0,0)   40%,
                rgba(0,0,0,0.3) 65%,
                rgba(0,0,0,0.72) 100%
            );
        }}
        /* Birthday title overlaid on the photo */
        .hero-title-block {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            text-align: center;
            padding: 0 20px 48px;
        }}
        .hero-eyebrow {{
            font-family: 'Raleway', sans-serif;
            font-weight: 300;
            font-size: clamp(9px, 1.8vw, 13px);
            letter-spacing: 8px;
            text-transform: uppercase;
            color: rgba(255,255,255,0.6);
            display: block;
            margin-bottom: 10px;
            animation: fadeSlowly 2s ease-out 0.3s both;
        }}
        .hero-name {{
            font-family: 'Pinyon Script', cursive;
            color: #ffffff;
            font-size: clamp(62px, 14vw, 130px);
            line-height: 1.0;
            display: block;
            text-shadow:
                0 2px 8px  rgba(0,0,0,0.55),
                0 8px 30px rgba(0,0,0,0.35);
            animation: riseUp 1.8s cubic-bezier(0.16,1,0.3,1) 0.2s both;
        }}

        /* ────────────────────────────────────────────
           ORNAMENT DIVIDER
        ──────────────────────────────────────────── */
        .ornament-row {{
            text-align: center;
            padding: 36px 0 30px;
            animation: fadeSlowly 2s ease-out 0.8s both;
        }}
        .ornament-line {{
            display: inline-flex;
            align-items: center;
            gap: 16px;
            color: rgba(255,255,255,0.5);
            font-size: 11px;
            letter-spacing: 8px;
        }}
        .ornament-line::before,
        .ornament-line::after {{
            content: '';
            display: inline-block;
            width: clamp(40px, 10vw, 100px);
            height: 1px;
            background: rgba(255,255,255,0.3);
        }}

        /* ────────────────────────────────────────────
           PHOTO DUO
        ──────────────────────────────────────────── */
        .photo-duo {{
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            display: grid;
            grid-template-columns: 1fr 1fr;
            position: relative;
            animation: fadeSlowly 2s ease-out 1s both;
        }}
        .photo-duo-cell {{
            position: relative;
            overflow: hidden;
            height: clamp(220px, 48vw, 440px);
        }}
        .photo-duo-cell img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            display: block;
            transition: transform 0.7s cubic-bezier(0.25,0.46,0.45,0.94);
        }}
        .photo-duo-cell:hover img {{
            transform: scale(1.04);
        }}
        /* Subtle gradient on each cell */
        .photo-duo-cell::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.18);
            transition: background 0.4s;
        }}
        .photo-duo-cell:hover::after {{
            background: rgba(0,0,0,0.08);
        }}
        /* Hairline separator between the two photos */
        .photo-duo-sep {{
            position: absolute;
            top: 0; bottom: 0;
            left: 50%;
            width: 1px;
            background: rgba(255,255,255,0.25);
            z-index: 2;
        }}
        /* Quote overlay positioned over the duo */
        .photo-duo-quote {{
            position: absolute;
            inset: 0;
            z-index: 3;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            pointer-events: none;
            padding-bottom: 28px;
        }}
        .photo-duo-quote-text {{
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-size: clamp(14px, 2.8vw, 22px);
            color: rgba(255,255,255,0.82);
            text-align: center;
            max-width: 70%;
            line-height: 1.5;
            text-shadow: 0 2px 8px rgba(0,0,0,0.5);
            letter-spacing: 0.3px;
        }}

        /* ────────────────────────────────────────────
           GLASS LETTER
        ──────────────────────────────────────────── */
        .glass-letter {{
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            padding: clamp(56px,8vw,100px) clamp(24px,10vw,140px) clamp(80px,10vw,120px);
            background: rgba(5, 5, 12, 0.65);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-top: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            animation: fadeSlowly 2.5s ease-out 1.4s both;
        }}
        .letter-label {{
            font-family: 'Raleway', sans-serif;
            font-weight: 300;
            font-size: clamp(9px, 1.5vw, 11px);
            letter-spacing: 7px;
            text-transform: uppercase;
            color: rgba(255,255,255,0.35);
            margin-bottom: 36px;
            display: block;
        }}
        .letter-salutation {{
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-weight: 300;
            font-size: clamp(28px, 5vw, 48px);
            color: #fff;
            margin-bottom: 36px;
            display: block;
            line-height: 1.2;
        }}
        .letter-para {{
            font-family: 'Cormorant Garamond', serif;
            font-weight: 300;
            font-size: clamp(17px, 2.6vw, 24px);
            color: rgba(255,255,255,0.82);
            line-height: 1.95;
            max-width: 720px;
            margin: 0 auto 22px;
        }}
        .letter-para:last-of-type {{ margin-bottom: 0; }}
        .letter-kitchen {{
            display: inline-block;
            margin-top: 44px;
            font-family: 'Raleway', sans-serif;
            font-weight: 400;
            font-size: clamp(13px, 2vw, 17px);
            color: #ffd700;
            letter-spacing: 2px;
            animation: goldPulse 3.5s ease-in-out infinite;
        }}
        .letter-divider {{
            width: 40px;
            height: 1px;
            background: rgba(255,215,0,0.4);
            margin: 28px auto 0;
        }}
        .letter-sig {{
            font-family: 'Pinyon Script', cursive;
            font-size: clamp(44px, 7.5vw, 78px);
            color: rgba(255,255,255,0.9);
            margin-top: 40px;
            display: block;
            line-height: 1.1;
        }}
        </style>

        <!-- Premium JS confetti (replaces snow entirely) -->
        <canvas id="conf-cv"
            style="position:fixed;top:0;left:0;width:100vw;height:100vh;
                   pointer-events:none;z-index:9999;"></canvas>
        <script>
        (function(){{
            var cv = document.getElementById('conf-cv');
            if (!cv) return;
            var ctx = cv.getContext('2d');
            function resize(){{ cv.width=window.innerWidth; cv.height=window.innerHeight; }}
            resize();
            window.addEventListener('resize', resize);

            var palette = [
                '#FFD700','#FFC0CB','#DDA0DD','#ADD8E6',
                '#90EE90','#FFB6C1','#FFFACD','#E6E6FA','#FFFFFF'
            ];
            var ps = [];
            for (var i=0; i<200; i++) {{
                var shape = ['rect','circle','ribbon'][Math.floor(Math.random()*3)];
                ps.push({{
                    x:  Math.random()*cv.width,
                    y:  -20 - Math.random()*cv.height*0.7,
                    vx: (Math.random()-0.5)*3.5,
                    vy: Math.random()*3.2 + 1.2,
                    w:  Math.random()*11+4,
                    h:  Math.random()*7+3,
                    r:  Math.random()*4+2,
                    angle: Math.random()*Math.PI*2,
                    spin:  (Math.random()-0.5)*0.13,
                    color: palette[Math.floor(Math.random()*palette.length)],
                    alpha: 1,
                    shape: shape
                }});
            }}

            var frame=0, total=380;
            function tick(){{
                if (frame > total) {{ ctx.clearRect(0,0,cv.width,cv.height); return; }}
                ctx.clearRect(0,0,cv.width,cv.height);
                ps.forEach(function(p){{
                    p.x += p.vx;
                    p.y += p.vy;
                    p.angle += p.spin;
                    p.alpha = (frame > 280) ? Math.max(0, 1-(frame-280)/100) : 1;
                    if (p.y > cv.height) {{ p.y=-10; p.x=Math.random()*cv.width; }}

                    ctx.save();
                    ctx.translate(p.x, p.y);
                    ctx.rotate(p.angle);
                    ctx.globalAlpha = p.alpha;
                    ctx.fillStyle = p.color;

                    if (p.shape==='circle') {{
                        ctx.beginPath();
                        ctx.arc(0,0,p.r,0,Math.PI*2);
                        ctx.fill();
                    }} else if (p.shape==='ribbon') {{
                        ctx.beginPath();
                        ctx.moveTo(-p.w/2, -p.h/2);
                        ctx.quadraticCurveTo(0, p.h, p.w/2, -p.h/2);
                        ctx.closePath();
                        ctx.fill();
                    }} else {{
                        ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h);
                    }}
                    ctx.restore();
                }});
                frame++;
                requestAnimationFrame(tick);
            }}
            setTimeout(tick, 600);
        }})();
        </script>
    """, unsafe_allow_html=True)

    # ── HERO PHOTO WITH TITLE OVERLAY ──────────────────────────────────────
    st.markdown(f"""
        <div class="hero-section">
            <img src="app/static/{HERO_IMAGE}" alt="Birthday hero photo">
            <div class="hero-scrim"></div>
            <div class="hero-title-block">
                <span class="hero-eyebrow">Today is all yours</span>
                <span class="hero-name">Happy Birthday, {WIFE_NAME}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ── ORNAMENT ────────────────────────────────────────────────────────────
    st.markdown("""
        <div class="ornament-row">
            <div class="ornament-line">✦</div>
        </div>
    """, unsafe_allow_html=True)

    # ── PHOTO DUO ───────────────────────────────────────────────────────────
    st.markdown(f"""
        <div class="photo-duo">
            <div class="photo-duo-cell">
                <img src="app/static/{PHOTO_2}" alt="Memory">
            </div>
            <div class="photo-duo-cell">
                <img src="app/static/{PHOTO_3}" alt="Memory">
            </div>
            <div class="photo-duo-sep"></div>
            <div class="photo-duo-quote">
                <span class="photo-duo-quote-text">{PHOTO_QUOTE}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ── GLASS LETTER ────────────────────────────────────────────────────────
    st.markdown(f"""
        <div class="glass-letter">
            <span class="letter-label">A message written with love</span>
            <span class="letter-salutation">My Dearest {WIFE_NAME},</span>
            <p class="letter-para">{MSG_1}</p>
            <p class="letter-para">{MSG_2}</p>
            <p class="letter-para">{MSG_3}</p>
            <p class="letter-para">{MSG_4}</p>
            <span class="letter-kitchen">✦ &nbsp; {KITCHEN_NOTE} &nbsp; ✦</span>
            <div class="letter-divider"></div>
            <span class="letter-sig">Love, {YOUR_NAME}</span>
        </div>
    """, unsafe_allow_html=True)
