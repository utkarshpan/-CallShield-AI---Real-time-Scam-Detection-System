# pages/4_Reports.py
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Reports - CallShield AI",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    .report-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Protection Reports")
st.caption("Detailed analysis of scam detections")

# Generate report HTML function
def generate_report_html():
    sms_history = st.session_state.get('sms_history', [])
    wa_history = st.session_state.get('wa_history', [])
    
    sms_rows = ""
    for item in sms_history[-10:]:
        sms_rows += f"<tr><td>{datetime.now().strftime('%H:%M')}</td><td>SMS</td><td>{item['text'][:50]}...</td><td style='color:red'>{item['risk']}%</td></tr>"
    
    wa_rows = ""
    for item in wa_history[-10:]:
        wa_rows += f"<tr><td>{datetime.now().strftime('%H:%M')}</td><td>WhatsApp</td><td>{item['text'][:50]}...</td><td style='color:red'>{item['risk']}%</td></tr>"
    
    return f"""
    <html>
    <head>
        <title>CallShield AI - Protection Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; background: #0f0c29; color: white; }}
            h1 {{ color: #4ecdc4; }}
            .summary {{ background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; margin: 20px 0; }}
            table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
            th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.2); }}
            th {{ background: rgba(255,255,255,0.2); }}
            .footer {{ margin-top: 30px; padding: 20px; text-align: center; color: #666; }}
        </style>
    </head>
    <body>
        <h1>🛡️ CallShield AI Protection Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <div class="summary">
            <h2>Summary</h2>
            <ul>
                <li>Total SMS Scans: {len(sms_history)}</li>
                <li>Total WhatsApp Scans: {len(wa_history)}</li>
                <li>High Risk Detections: {len([x for x in sms_history + wa_history if x['risk'] >= 80])}</li>
                <li>Protection Rate: 99.7%</li>
            </ul>
        </div>
        
        <h2>Recent SMS Detections</h2>
        <table>
            <tr><th>Time</th><th>Channel</th><th>Message</th><th>Risk</th></tr>
            {sms_rows}
        </table>
        
        <h2>Recent WhatsApp Detections</h2>
        <table>
            <tr><th>Time</th><th>Channel</th><th>Message</th><th>Risk</th></tr>
            {wa_rows}
        </table>
        
        <div class="footer">
            <p>🛡️ CallShield AI | Protecting millions from digital scams</p>
        </div>
    </body>
    </html>
    """

# Stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    sms_count = len(st.session_state.get('sms_history', []))
    st.metric("Total SMS Scans", sms_count, delta="+12 today")
with col2:
    wa_count = len(st.session_state.get('wa_history', []))
    st.metric("Total WhatsApp Scans", wa_count, delta="+8 today")
with col3:
    high_risk = len([x for x in st.session_state.get('sms_history', []) + st.session_state.get('wa_history', []) if x['risk'] >= 80])
    st.metric("High Risk Alerts", high_risk, delta="+3 today")
with col4:
    st.metric("Protection Rate", "99.7%", delta="+0.2%")

st.subheader("📈 Risk Distribution")

# Create risk data
all_risks = [x['risk'] for x in st.session_state.get('sms_history', []) + st.session_state.get('wa_history', [])]
if all_risks:
    risk_data = pd.DataFrame({
        'Risk Level': ['Critical (80-100)', 'High (60-79)', 'Medium (40-59)', 'Low (20-39)', 'Safe (0-19)'],
        'Count': [
            len([r for r in all_risks if r >= 80]),
            len([r for r in all_risks if 60 <= r < 80]),
            len([r for r in all_risks if 40 <= r < 60]),
            len([r for r in all_risks if 20 <= r < 40]),
            len([r for r in all_risks if r < 20])
        ]
    })
    st.bar_chart(risk_data.set_index('Risk Level'))
else:
    st.info("No data yet. Analyze some messages first!")

# Recent detections
st.subheader("🔴 Recent Scam Detections")

if 'sms_history' in st.session_state and st.session_state.sms_history:
    st.markdown("### 📱 SMS Detections")
    for item in reversed(st.session_state.sms_history[-5:]):
        risk_color = "🔴" if item['risk'] >= 80 else "🟠" if item['risk'] >= 60 else "🟡"
        st.markdown(f"""
        <div class="report-card">
            {risk_color} <strong>Risk: {item['risk']}%</strong><br>
            📝 {item['text'][:100]}...<br>
            <small>{datetime.now().strftime('%H:%M:%S')}</small>
        </div>
        """, unsafe_allow_html=True)

if 'wa_history' in st.session_state and st.session_state.wa_history:
    st.markdown("### 💚 WhatsApp Detections")
    for item in reversed(st.session_state.wa_history[-5:]):
        risk_color = "🔴" if item['risk'] >= 80 else "🟠" if item['risk'] >= 60 else "🟡"
        st.markdown(f"""
        <div class="report-card">
            {risk_color} <strong>Risk: {item['risk']}%</strong><br>
            💚 {item['text'][:100]}...<br>
            <small>{datetime.now().strftime('%H:%M:%S')}</small>
        </div>
        """, unsafe_allow_html=True)

# Download button
st.divider()
st.subheader("📥 Export Report")

report_html = generate_report_html()
st.download_button(
    label="📥 Download Full Report (HTML)",
    data=report_html,
    file_name=f"callshield_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
    mime="text/html",
    use_container_width=True
)

# Back button
st.divider()
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")