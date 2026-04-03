# start_page.py
import streamlit as st

st.set_page_config(
    page_title="CallShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Animated CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0f0f23 100%);
        overflow: hidden;
    }
    
    /* Animated background particles */
    @keyframes float {
        0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.3; }
        25% { transform: translateY(-20px) translateX(10px); opacity: 0.6; }
        50% { transform: translateY(10px) translateX(-15px); opacity: 0.4; }
        75% { transform: translateY(-10px) translateX(-5px); opacity: 0.5; }
    }
    
    .particle {
        position: fixed;
        border-radius: 50%;
        background: linear-gradient(135deg, #4ecdc4, #667eea);
        animation: float 8s infinite ease-in-out;
        z-index: 0;
    }
    
    /* Main container */
    .splash-container {
        position: relative;
        z-index: 10;
        text-align: center;
        padding: 100px 20px;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    /* Animated logo */
    @keyframes logoPulse {
        0%, 100% { transform: scale(1); text-shadow: 0 0 20px rgba(78,205,196,0.3); }
        50% { transform: scale(1.05); text-shadow: 0 0 50px rgba(78,205,196,0.8); }
    }
    
    .logo {
        font-size: 6em;
        animation: logoPulse 2s infinite;
        margin-bottom: 20px;
    }
    
    /* Glitch text effect */
    @keyframes glitch {
        0%, 100% { transform: skew(0deg, 0deg); opacity: 1; }
        95% { transform: skew(0deg, 0deg); opacity: 1; }
        96% { transform: skew(5deg, 2deg); opacity: 0.8; }
        97% { transform: skew(-5deg, -2deg); opacity: 0.9; }
        98% { transform: skew(3deg, 1deg); opacity: 0.85; }
        99% { transform: skew(-3deg, -1deg); opacity: 0.95; }
    }
    
    .glitch-text {
        font-family: 'Orbitron', monospace;
        font-size: 4em;
        font-weight: 900;
        background: linear-gradient(135deg, #4ecdc4, #667eea, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glitch 4s infinite;
        margin-bottom: 10px;
    }
    
    /* Typewriter effect */
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    .typewriter {
        font-size: 1.2em;
        color: #888;
        border-right: 2px solid #4ecdc4;
        white-space: nowrap;
        overflow: hidden;
        display: inline-block;
        animation: blink 1s step-end infinite;
    }
    
    /* Loading bar */
    @keyframes loading {
        0% { width: 0%; }
        100% { width: 100%; }
    }
    
    .loading-bar {
        width: 300px;
        height: 3px;
        background: rgba(255,255,255,0.1);
        border-radius: 3px;
        margin: 30px auto;
        overflow: hidden;
    }
    
    .loading-fill {
        height: 100%;
        background: linear-gradient(90deg, #4ecdc4, #667eea);
        width: 0%;
        animation: loading 3s ease-out forwards;
        border-radius: 3px;
    }
    
    /* Fade in animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 1s ease-out forwards;
        opacity: 0;
    }
    
    .delay-1 { animation-delay: 0.3s; }
    .delay-2 { animation-delay: 0.6s; }
    .delay-3 { animation-delay: 0.9s; }
    
    /* Button style */
    .stButton button {
        background: linear-gradient(135deg, #4ecdc4, #667eea);
        color: white;
        border: none;
        padding: 15px 50px;
        font-size: 1.2em;
        border-radius: 50px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(78,205,196,0.5);
    }
</style>
""", unsafe_allow_html=True)

# Animated particles
for i in range(20):
    size = 50 + i * 10
    left = (i * 73) % 100
    top = (i * 47) % 100
    delay = i * 0.5
    st.markdown(f"""
    <div class="particle" style="
        width: {size % 80 + 20}px;
        height: {size % 80 + 20}px;
        left: {left}%;
        top: {top}%;
        animation-delay: {delay}s;
        opacity: {0.1 + (i % 5) * 0.05};
    "></div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="splash-container">
    <div class="logo fade-in">🛡️</div>
    <div class="glitch-text fade-in">CALLSHIELD AI</div>
    <div class="typewriter fade-in delay-1">Real-time Scam Detection System</div>
    
    <div class="loading-bar fade-in delay-2">
        <div class="loading-fill"></div>
    </div>
    
    <p class="fade-in delay-2" style="color: #666; margin-top: 10px;">Initializing security protocols...</p>
    
    <p class="fade-in delay-3" style="color: #444; margin-top: 40px; font-size: 0.8em;">🔒 Protected by advanced pattern recognition</p>
</div>
""", unsafe_allow_html=True)

# Button to enter dashboard
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🚀 ENTER SECURE DASHBOARD", use_container_width=True):
        st.switch_page("pages/1_Voice_Call.py")

# Note: To go to main dashboard, just use Voice Call page as entry