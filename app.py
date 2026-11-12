
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

from config import APP_NAME, APP_VERSION, MISSION_NAME, MISSION_ID, ASTRONAUT, COLORS, REFERENCE_RANGES
from modules.data_engine import generate_health_data, validate_uploaded_data
from modules.anomaly_detector import detect_anomalies, get_anomaly_summary
from modules.health_analyzer import get_health_status
from modules.recommendations import generate_recommendations
from modules.database import initialize_database, save_alerts, get_alert_history, clear_alert_history


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ASTROHEALTH AI | Mission Control",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

BG = "#07111F"
PANEL = "#101D30"
PANEL2 = "#14263D"
CYAN = "#39D5F6"
BLUE = "#648BFF"
PURPLE = "#A78BFA"
GREEN = "#35D39A"
YELLOW = "#F5C66A"
RED = "#FF657A"
TEXT = "#E8F0FC"
MUTED = "#91A3BA"

# ============================================================
# PREMIUM INTERFACE
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #07111F;
    --panel: #101D30;
    --panel2: #14263D;
    --cyan: #39D5F6;
    --blue: #648BFF;
    --purple: #A78BFA;
    --green: #35D39A;
    --red: #FF657A;
    --text: #E8F0FC;
    --muted: #91A3BA;
}

.stApp {
    background:
        radial-gradient(ellipse at 80% 0%, rgba(57,213,246,.075), transparent 35%),
        radial-gradient(ellipse at 10% 35%, rgba(167,139,250,.055), transparent 35%),
        var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1550px;
    padding-top: 1.3rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #0A1728;
    border-right: 1px solid #20364F;
}

[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #142942, #0D1C2E);
    border: 1px solid #29415C;
    border-radius: 15px;
    padding: 19px 20px;
    min-height: 112px;
}

[data-testid="stMetricLabel"] {
    color: #A1B4CB;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1px;
}

[data-testid="stMetricValue"] {
    color: #F0F7FF;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
}

[data-testid="stMetricDelta"] {
    font-size: 12px;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -0.6px;
}

p, label, span {
    font-family: 'Inter', sans-serif;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 32px;
    border-radius: 20px;
    border: 1px solid #315473;
    background:
        radial-gradient(circle at 85% 30%, rgba(57,213,246,.17), transparent 28%),
        linear-gradient(115deg, #102B45, #152447 58%, #211F45);
    margin-bottom: 23px;
}

.hero::after {
    content: "◈";
    position: absolute;
    right: 50px;
    top: 2px;
    font-size: 145px;
    color: rgba(57,213,246,.10);
}

.hero-label {
    font-family: 'DM Mono', monospace;
    color: #70DFF7;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 700;
    color: #F4F8FF;
    line-height: 1.05;
}

.hero-subtitle {
    color: #B4C9DF;
    font-size: 13px;
    margin-top: 12px;
    max-width: 620px;
    line-height: 1.7;
}

.hero-meta {
    margin-top: 23px;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.meta-chip {
    background: rgba(5,17,31,.35);
    border: 1px solid rgba(113,192,226,.24);
    padding: 7px 12px;
    border-radius: 7px;
    font-size: 11px;
    color: #D7E9F8;
    font-family: 'DM Mono', monospace;
}

.section-head {
    display: flex;
    align-items: center;
    gap: 11px;
    margin-top: 30px;
    margin-bottom: 15px;
}

.section-indicator {
    width: 4px;
    height: 24px;
    border-radius: 5px;
    background: var(--cyan);
}

.section-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--text);
}

.section-caption {
    color: var(--muted);
    font-size: 12px;
    margin-top: 3px;
}

.panel {
    background: linear-gradient(145deg, #12243A, #0D1A2C);
    border: 1px solid #263D57;
    border-radius: 15px;
    padding: 19px;
    margin-bottom: 15px;
}

.panel-label {
    color: #91A3BA;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

.panel-value {
    color: #F0F7FF;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 700;
    margin-top: 9px;
}

.panel-description {
    color: #91A3BA;
    font-size: 11px;
    margin-top: 5px;
}

.status-dot {
    display: inline-block;
    height: 8px;
    width: 8px;
    border-radius: 50%;
    background: #35D39A;
    box-shadow: 0 0 12px #35D39A;
    margin-right: 8px;
}

.status-chip {
    color: #35D39A;
    background: rgba(53,211,154,.09);
    border: 1px solid rgba(53,211,154,.28);
    padding: 7px 12px;
    border-radius: 7px;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
}

.info-card {
    border-left: 3px solid var(--cyan);
    background: #10243A;
    padding: 14px 17px;
    border-radius: 0 10px 10px 0;
    margin: 10px 0;
    color: #C9D9E9;
    font-size: 13px;
}

div.stButton > button {
    background: #142B43;
    color: #E8F0FC;
    border: 1px solid #315170;
    border-radius: 9px;
    font-weight: 600;
    transition: all .2s ease;
}

div.stButton > button:hover {
    background: #193B57;
    border-color: #39D5F6;
    color: #39D5F6;
}

div[data-testid="stDownloadButton"] button {
    background: #123B4A;
    border: 1px solid #39D5F6;
    color: white;
    border-radius: 9px;
}

div[data-testid="stFileUploader"] {
    background: #101D30;
    border: 1px dashed #42627E;
    border-radius: 12px;
    padding: 12px;
}

div[data-testid="stSelectbox"] > div,
div[data-testid="stTextInput"] > div {
    border-radius: 8px;
}

hr {
    border-color: #243B56;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

@media(max-width: 700px) {
    .hero { padding: 22px; }
    .hero::after { font-size: 90px; right: 12px; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# REUSABLE FUNCTIONS
# ============================================================

def section(title, caption=""):
    st.markdown(f"""
    <div class="section-head">
        <div class="section-indicator"></div>
        <div>
            <div class="section-heading">{title}</div>
            <div class="section-caption">{caption}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def panel(label, value, description="", accent=CYAN):
    st.markdown(f"""
    <div class="panel" style="border-top:2px solid {accent};">
        <div class="panel-label">{label}</div>
        <div class="panel-value">{value}</div>
        <div class="panel-description">{description}</div>
    </div>
    """, unsafe_allow_html=True)


def chart_layout(fig, height=350):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=MUTED, family="Inter"),
        margin=dict(l=15, r=15, t=45, b=15),
        legend=dict(
            orientation="h",
            y=1.13,
            x=0
        ),
        xaxis=dict(
            gridcolor="#24374E",
            zerolinecolor="#24374E"
        ),
        yaxis=dict(
            gridcolor="#24374E",
            zerolinecolor="#24374E"
        ),
        title_font=dict(
            family="Space Grotesk",
            size=15,
            color=TEXT
        )
    )
    return fig


def line_chart(data, column, title, color, unit):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["timestamp"],
        y=data[column],
        mode="lines",
        name=title,
        line=dict(color=color, width=2.5),
        fill="tozeroy",
        fillcolor="rgba(57,213,246,0.07)",
        hovertemplate="%{x}<br>%{y:.2f} " + unit + "<extra></extra>"
    ))

    fig.update_layout(
        title=title,
        yaxis_title=unit
    )

    return chart_layout(fig)


def calculate_health_score(row):
    """
    Transparent demonstration score.
    This is not a clinical health score.
    """
    scores = []

    for metric, (low, high) in REFERENCE_RANGES.items():
        value = float(row[metric])

        if low <= value <= high:
            scores.append(100)
        else:
            distance = min(abs(value - low), abs(value - high))
            penalty = min(distance * 5, 100)
            scores.append(100 - penalty)

    return round(float(np.mean(scores)), 1)


def make_forecast(data, column, steps=12):
    """
    Experimental linear trend projection.
    Not a medical prediction.
    """
    values = data[column].tail(60).to_numpy(dtype=float)

    if len(values) < 5:
        return None

    x = np.arange(len(values))
    slope, intercept = np.polyfit(x, values, 1)

    future_x = np.arange(len(values), len(values) + steps)
    predictions = slope * future_x + intercept

    future_times = pd.date_range(
        start=data["timestamp"].iloc[-1],
        periods=steps + 1,
        freq="5min"
    )[1:]

    return pd.DataFrame({
        "timestamp": future_times,
        "prediction": predictions
    })


# ============================================================
# DATA INITIALIZATION
# ============================================================

initialize_database()

if "health_data" not in st.session_state:
    st.session_state.health_data = generate_health_data(rows=300)

if "alerts_saved" not in st.session_state:
    st.session_state.alerts_saved = False

df = st.session_state.health_data.copy()

df = validate_uploaded_data(df)
df = detect_anomalies(df)

latest = df.iloc[-1]
previous = df.iloc[-2] if len(df) > 1 else latest

summary = get_anomaly_summary(df)

status, status_type, current_alerts = get_health_status(
    latest,
    bool(latest["ai_anomaly"])
)

health_score = calculate_health_score(latest)

if not st.session_state.alerts_saved:
    save_alerts(current_alerts, latest["timestamp"])
    st.session_state.alerts_saved = True


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="font-family:Space Grotesk;font-size:25px;font-weight:700;color:#39D5F6;">
        ◈ ASTROHEALTH
    </div>
    <div style="font-size:10px;letter-spacing:2px;color:#91A3BA;">
        INTELLIGENT SPACE SYSTEMS
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        "<div class='panel-label'>MISSION NAVIGATION</div>",
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Mission Overview",
            "Health Monitoring",
            "AI Intelligence",
            "Alert Command",
            "Analytics Laboratory",
            "Data Command"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(
        "<div class='panel-label'>ASTRONAUT PROFILE</div>",
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div style="background:#12243A;padding:14px;border-radius:12px;border:1px solid #29415C;">
        <div style="font-size:23px;color:#39D5F6;">◉</div>
        <div style="font-weight:700;margin-top:8px;">{ASTRONAUT['name']}</div>
        <div style="font-size:11px;color:#91A3BA;margin-top:4px;">{ASTRONAUT['role']}</div>
        <div style="font-size:11px;color:#91A3BA;margin-top:8px;">ID: {ASTRONAUT['id']}</div>
        <div style="font-size:11px;color:#91A3BA;">MISSION DAY: {ASTRONAUT['mission_day']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        "<div class='panel-label'>SYSTEM STATUS</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='color:#35D39A;font-size:12px;margin-top:10px;'><span class='status-dot'></span>ANALYTICS ONLINE</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='color:#35D39A;font-size:12px;margin-top:9px;'><span class='status-dot'></span>DATABASE CONNECTED</div>",
        unsafe_allow_html=True
    )

    st.caption("ASTROHEALTH AI · " + APP_VERSION)


# ============================================================
# MAIN HERO
# ============================================================

st.markdown(f"""
<div class="hero">
    <div class="hero-label">◈ {MISSION_NAME} / {MISSION_ID}</div>
    <div class="hero-title">MISSION CONTROL</div>
    <div class="hero-subtitle">
        An intelligent astronaut health-monitoring environment.
        Physiological telemetry, machine-learning anomaly detection,
        and mission health analytics in one unified platform.
    </div>
    <div class="hero-meta">
        <span class="meta-chip">MISSION DAY {ASTRONAUT['mission_day']}</span>
        <span class="meta-chip">LOW EARTH ORBIT</span>
        <span class="meta-chip">AI SYSTEM V{APP_VERSION}</span>
        <span class="meta-chip">DEMONSTRATION MODE</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# PAGE 1: MISSION OVERVIEW
# ============================================================

if page == "Mission Overview":

    st.markdown(
        f"### Welcome back, {ASTRONAUT['name']}"
    )

    st.caption(
        "MISSION TELEMETRY OVERVIEW  /  "
        + datetime.now().strftime("%d %B %Y · %H:%M:%S")
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "HEART RATE",
            f"{latest['heart_rate']:.1f} bpm",
            f"{latest['heart_rate'] - previous['heart_rate']:+.1f}"
        )

    with c2:
        st.metric(
            "BLOOD OXYGEN",
            f"{latest['spo2']:.1f}%",
            f"{latest['spo2'] - previous['spo2']:+.1f}%"
        )

    with c3:
        st.metric(
            "BODY TEMPERATURE",
            f"{latest['temperature']:.1f} °C",
            f"{latest['temperature'] - previous['temperature']:+.2f} °C"
        )

    with c4:
        st.metric(
            "AI ANOMALIES",
            summary["anomalies"],
            f"{summary['anomaly_rate']:.1f}% of readings"
        )

    section(
        "Mission health intelligence",
        "A unified snapshot of astronaut physiological status."
    )

    a, b, c = st.columns(3)

    with a:
        panel(
            "DEMONSTRATION HEALTH SCORE",
            f"{health_score}/100",
            "Transparent reference-range indicator",
            GREEN if health_score >= 80 else YELLOW
        )

    with b:
        panel(
            "MONITORING RECORDS",
            f"{len(df):,}",
            "Validated telemetry observations",
            CYAN
        )

    with c:
        panel(
            "LATEST SYSTEM STATUS",
            status,
            "Based on the latest configured checks",
            GREEN if status_type == "success" else YELLOW
        )

    section(
        "Physiological telemetry",
        "Recent trends from the demonstration monitoring dataset."
    )

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            line_chart(df, "heart_rate", "Heart Rate", CYAN, "bpm"),
            use_container_width=True
        )

    with right:
        st.plotly_chart(
            line_chart(df, "spo2", "Blood Oxygen", PURPLE, "%"),
            use_container_width=True
        )

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            line_chart(df, "temperature", "Body Temperature", YELLOW, "°C"),
            use_container_width=True
        )

    with right:
        st.plotly_chart(
            line_chart(df, "respiration", "Respiration Rate", GREEN, "breaths/min"),
            use_container_width=True
        )

    section("Mission environment")

    e1, e2, e3, e4 = st.columns(4)

    with e1:
        panel("MISSION PHASE", "ORBITAL", "Simulated mission context", CYAN)

    with e2:
        panel("ORBITAL LOCATION", "LEO", "Low Earth Orbit", BLUE)

    with e3:
        panel("DATA SOURCE", "SYNTHETIC", "Demonstration telemetry", PURPLE)

    with e4:
        panel("AI ENGINE", "ACTIVE", "Isolation Forest", GREEN)

    section("Latest physiological observation")

    st.dataframe(
        pd.DataFrame([latest]),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 2: HEALTH MONITORING
# ============================================================

elif page == "Health Monitoring":

    section(
        "Physiological monitoring",
        "Explore seven physiological indicators and their measurement history."
    )

    indicators = {
        "Heart Rate": ("heart_rate", "bpm", CYAN),
        "Blood Oxygen": ("spo2", "%", PURPLE),
        "Body Temperature": ("temperature", "°C", YELLOW),
        "Respiration": ("respiration", "breaths/min", GREEN),
        "Systolic Pressure": ("systolic", "mmHg", BLUE),
        "Diastolic Pressure": ("diastolic", "mmHg", RED),
        "Activity": ("activity", "%", GREEN)
    }

    choice = st.selectbox(
        "SELECT PHYSIOLOGICAL INDICATOR",
        list(indicators.keys())
    )

    column, unit, color = indicators[choice]

    st.plotly_chart(
        line_chart(df, column, choice, color, unit),
        use_container_width=True
    )

    a, b, c, d = st.columns(4)

    with a:
        st.metric("LATEST", f"{latest[column]:.2f} {unit}")

    with b:
        st.metric("AVERAGE", f"{df[column].mean():.2f} {unit}")

    with c:
        st.metric("MINIMUM", f"{df[column].min():.2f} {unit}")

    with d:
        st.metric("MAXIMUM", f"{df[column].max():.2f} {unit}")

    section("Reference-range comparison")

    if column in REFERENCE_RANGES:
        low, high = REFERENCE_RANGES[column]

        st.info(
            f"Configured demonstration range: {low} – {high} {unit}. "
            "These are illustrative values, not validated astronaut-specific clinical limits."
        )

    section("Full physiological dataset")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 3: AI INTELLIGENCE
# ============================================================

elif page == "AI Intelligence":

    section(
        "Artificial intelligence laboratory",
        "Unsupervised machine learning for unusual physiological pattern identification."
    )

    a, b, c = st.columns(3)

    with a:
        st.metric("TOTAL OBSERVATIONS", summary["total_readings"])

    with b:
        st.metric("AI-FLAGGED OBSERVATIONS", summary["anomalies"])

    with c:
        st.metric("ANOMALY RATE", f"{summary['anomaly_rate']:.2f}%")

    normal = df[df["ai_anomaly"] == 0]
    unusual = df[df["ai_anomaly"] == 1]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=normal["timestamp"],
        y=normal["heart_rate"],
        mode="markers",
        name="Typical pattern",
        marker=dict(color=CYAN, size=6)
    ))

    fig.add_trace(go.Scatter(
        x=unusual["timestamp"],
        y=unusual["heart_rate"],
        mode="markers",
        name="AI-flagged pattern",
        marker=dict(color=RED, size=11, symbol="diamond")
    ))

    fig.update_layout(
        title="Machine Learning Pattern Detection",
        xaxis_title="Observation time",
        yaxis_title="Heart rate (bpm)"
    )

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )

    section(
        "AI anomaly score",
        "Higher scores indicate greater statistical unusualness relative to this dataset."
    )

    score_fig = px.histogram(
        df,
        x="anomaly_score",
        color="ai_anomaly",
        nbins=25,
        title="Distribution of anomaly scores",
        color_discrete_map={
            0: CYAN,
            1: RED
        }
    )

    st.plotly_chart(
        chart_layout(score_fig),
        use_container_width=True
    )

    section("Flagged observations")

    if unusual.empty:
        st.success("No unusual observations were flagged.")
    else:
        st.dataframe(
            unusual,
            use_container_width=True,
            hide_index=True
        )

    st.info(
        "Model: Isolation Forest. It identifies statistically unusual "
        "patterns without requiring labelled training data. Its output "
        "does not establish illness, medical risk, or a diagnosis."
    )


# ============================================================
# PAGE 4: ALERT COMMAND
# ============================================================

elif page == "Alert Command":

    section(
        "Mission alert command",
        "Review configured reference-range deviations and AI observations."
    )

    if current_alerts:

        for alert in current_alerts:

            if alert["level"] == "Warning":
                st.warning(
                    f"{alert['indicator']} · {alert['value']} {alert['unit']} — "
                    f"{alert['message']}"
                )

            else:
                st.info(
                    f"{alert['indicator']} — {alert['message']}"
                )

        section("Recommended verification actions")

        for item in generate_recommendations(current_alerts):
            st.markdown(
                f"<div class='info-card'>◈ &nbsp; {item}</div>",
                unsafe_allow_html=True
            )

    else:
        st.success(
            "No configured reference-range deviations were found in the latest observation."
        )

    section("Persistent alert history")

    history = get_alert_history()

    if history.empty:
        st.caption("No alert records are currently available.")

    else:
        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download alert history",
            history.to_csv(index=False).encode("utf-8"),
            "astrohealth_alert_history.csv",
            "text/csv"
        )

    st.divider()

    if st.button("Clear stored alert history"):
        clear_alert_history()
        st.success("Stored alert history cleared.")
        st.rerun()


# ============================================================
# PAGE 5: ANALYTICS LABORATORY
# ============================================================

elif page == "Analytics Laboratory":

    section(
        "Advanced mission analytics",
        "Statistical exploration of physiological monitoring observations."
    )

    numeric = df.select_dtypes(include=np.number)

    correlation = numeric.corr()

    heatmap = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title="Physiological Correlation Matrix"
    )

    heatmap.update_layout(
        height=570,
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=TEXT
    )

    st.plotly_chart(
        heatmap,
        use_container_width=True
    )

    section("Distribution analysis")

    selected = st.selectbox(
        "Select variable for distribution analysis",
        list(numeric.columns)
    )

    distribution = px.histogram(
        df,
        x=selected,
        nbins=30,
        marginal="box",
        title=f"Distribution of {selected.replace('_', ' ').title()}"
    )

    distribution.update_traces(
        marker_color=CYAN,
        opacity=0.85
    )

    st.plotly_chart(
        chart_layout(distribution),
        use_container_width=True
    )

    section("Experimental trend forecasting")

    forecast_choice = st.selectbox(
        "Select indicator for experimental projection",
        ["heart_rate", "spo2", "temperature", "respiration"]
    )

    forecast = make_forecast(df, forecast_choice)

    if forecast is not None:

        history = df.tail(60)

        forecast_fig = go.Figure()

        forecast_fig.add_trace(go.Scatter(
            x=history["timestamp"],
            y=history[forecast_choice],
            mode="lines",
            name="Historical observations",
            line=dict(color=CYAN, width=2)
        ))

        forecast_fig.add_trace(go.Scatter(
            x=forecast["timestamp"],
            y=forecast["prediction"],
            mode="lines",
            name="Experimental projection",
            line=dict(color=PURPLE, width=2, dash="dash")
        ))

        st.plotly_chart(
            chart_layout(forecast_fig),
            use_container_width=True
        )

        st.caption(
            "This is a simple linear trend projection for demonstration, "
            "not a validated medical or physiological prediction."
        )

    section("Statistical summary")

    st.dataframe(
        numeric.describe().T,
        use_container_width=True
    )


# ============================================================
# PAGE 6: DATA COMMAND
# ============================================================

elif page == "Data Command":

    section(
        "Mission data command centre",
        "Import, validate, inspect and export physiological telemetry."
    )

    uploaded = st.file_uploader(
        "IMPORT HEALTH TELEMETRY CSV",
        type=["csv"]
    )

    if uploaded is not None:

        try:

            imported = pd.read_csv(uploaded)
            cleaned = validate_uploaded_data(imported)

            st.success(
                f"Validation successful: {len(cleaned)} valid observations."
            )

            st.dataframe(
                cleaned.head(15),
                use_container_width=True
            )

            if st.button("Load imported dataset into dashboard"):

                st.session_state.health_data = cleaned
                st.session_state.alerts_saved = False

                st.rerun()

        except Exception as error:

            st.error(f"Dataset validation error: {error}")

    section("Export mission telemetry")

    st.download_button(
        "DOWNLOAD COMPLETE TELEMETRY CSV",
        df.to_csv(index=False).encode("utf-8"),
        "astrohealth_mission_telemetry.csv",
        "text/csv"
    )

    section("Generate mission report")

    report = f"""
ASTROHEALTH AI
ASTRONAUT HEALTH MONITORING REPORT

Mission: {MISSION_NAME}
Mission ID: {MISSION_ID}
Astronaut: {ASTRONAUT['name']}
Astronaut ID: {ASTRONAUT['id']}
Mission Day: {ASTRONAUT['mission_day']}

REPORT GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

LATEST OBSERVATIONS
Heart Rate: {latest['heart_rate']:.2f} bpm
Blood Oxygen: {latest['spo2']:.2f} %
Temperature: {latest['temperature']:.2f} C
Respiration: {latest['respiration']:.2f}
Systolic Pressure: {latest['systolic']:.2f}
Diastolic Pressure: {latest['diastolic']:.2f}
Activity: {latest['activity']:.2f}

DEMONSTRATION HEALTH SCORE: {health_score}/100
AI-FLAGGED OBSERVATIONS: {summary['anomalies']}
ANOMALY RATE: {summary['anomaly_rate']:.2f}%

CURRENT CONFIGURED STATUS: {status}

IMPORTANT DISCLAIMER:
This report uses synthetic demonstration data.
The score and AI observations are educational outputs.
They are not medical diagnoses or validated clinical assessments.
"""

    st.download_button(
        "GENERATE AND DOWNLOAD MISSION REPORT",
        report,
        "astrohealth_mission_report.txt",
        "text/plain"
    )

    section("Demonstration environment controls")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Generate new telemetry dataset"):

            st.session_state.health_data = generate_health_data(
                rows=300,
                seed=int(datetime.now().timestamp()) % 100000
            )

            st.session_state.alerts_saved = False

            st.rerun()

    with col2:

        if st.button("Reset demonstration dataset"):

            st.session_state.health_data = generate_health_data(
                rows=300,
                seed=42
            )

            st.session_state.alerts_saved = False

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div style="text-align:center;padding:20px 5px;color:#71869F;">
    <div style="font-family:Space Grotesk;font-size:15px;letter-spacing:3px;color:#39D5F6;font-weight:700;">
        ASTROHEALTH AI
    </div>
    <div style="font-size:10px;letter-spacing:1.5px;margin-top:7px;">
        INTELLIGENT ASTRONAUT HEALTH MONITORING
    </div>
    <div style="font-size:10px;margin-top:12px;">
        Educational prototype · Synthetic demonstration data · Not a medical diagnostic system
    </div>
</div>
""", unsafe_allow_html=True)
