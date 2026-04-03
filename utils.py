# utils.py
import streamlit as st
from detection_engine import CallShieldEngine

def initialize_session():
    """Initialize session state variables"""
    if 'engine' not in st.session_state:
        st.session_state.engine = CallShieldEngine()
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'current_risk' not in st.session_state:
        st.session_state.current_risk = 0
    if 'current_alert' not in st.session_state:
        st.session_state.current_alert = "No active alerts"
    if 'current_pattern' not in st.session_state:
        st.session_state.current_pattern = "No patterns detected yet"
    if 'sms_history' not in st.session_state:
        st.session_state.sms_history = []
    if 'whatsapp_history' not in st.session_state:
        st.session_state.whatsapp_history = []

def reset_session():
    """Reset all session data"""
    st.session_state.engine.reset()
    st.session_state.conversation = []
    st.session_state.current_risk = 0
    st.session_state.current_alert = "No active alerts"
    st.session_state.current_pattern = "No patterns detected yet"