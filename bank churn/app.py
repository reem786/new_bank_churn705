import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- CONFIG & STYLING ---
st.set_page_config(page_title="NEURAL CHURN ANALYTICS", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top, #1a1a2e, #16213e, #0f3460);
        color: #e94560;
    }
    [data-testid="stMetricValue"] {
        color: #00fff2;
        text-shadow: 0 0 15px #00fff2;
        font-family: 'Courier New';
    }
    .stHeader {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(5px);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("churn_data.csv")
        # Feature Engineering for AI Analysis
        df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 45, 60, 100], labels=['Alpha', 'Beta', 'Gamma', 'Delta'])
        return df
    except:
        return None

# --- UI LOGIC ---
st.title("💠 NEURAL LINK: CUSTOMER RETENTION INTERFACE")

df = load_data()

if df is None:
    st.error("❌ CRITICAL ERROR: DATABASE OFFLINE. Run the generator script first.")
    st.stop()

# --- KPI STRIP ---
st.write("### ⚡ REAL-TIME SYSTEM METRICS")
m1, m2, m3, m4 = st.columns(4)
m1.metric("NODES ANALYZED", f"{len(df):,}")
m2.metric("CHURN PROBABILITY", f"{df['Exited'].mean()*100:.1f}%")
m3.metric("AVG LIQUIDITY", f"${df['Balance'].mean():,.0f}")
m4.metric("SYSTEM UPTIME", "99.9%")

st.divider()

# --- ANALYTICS ROW ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 GEOGRAPHIC RISK TOPOGRAPHY")
    fig = px.density_heatmap(df, x="Age", y="CreditScore", z="Exited", 
                             histfunc="avg", nbinsx=20, nbinsy=20,
                             color_continuous_scale='Viridis')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🧬 SEGMENT DYNAMICS")
    fig_pie = px.sunburst(df, path=['Geography', 'Gender', 'AgeGroup'], values='Exited',
                          color='Exited', color_continuous_scale='RdBu')
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_pie, use_container_width=True)

# --- NEURAL LOG ---
with st.expander("👁️ VIEW NEURAL LOG (RAW DATA)"):
    st.dataframe(df.style.background_gradient(cmap='Blues'))