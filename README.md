# 🛰️ AstroHealth AI
### Intelligent Astronaut Health Monitoring & Mission Control System

**An AI-powered prototype exploring how machine learning and data analytics can support astronaut physiological monitoring during space missions.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Isolation%20Forest-8A63D2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Project-Research%20Prototype-28A745?style=for-the-badge" />
</p>

---

## 🌌 About the Project

Human space exploration introduces complex health-monitoring challenges. Microgravity, isolation, confinement, and other spaceflight conditions can influence astronauts' physiological well-being.

**AstroHealth AI** is an intelligent monitoring dashboard developed to explore the application of artificial intelligence in astronaut health monitoring.

The platform combines physiological telemetry, machine-learning-based anomaly detection, interactive visualizations, and monitoring alerts in a unified mission-control environment.

The project was developed in response to the NASA Space Apps Challenge 2026 challenge:

**Create Health Monitoring Software for Astronauts on Space Missions.**

---

## 🖥️ Application Screenshots

AstroHealth AI contains six integrated dashboard modules.

### 01 — Mission Overview

A centralized mission-control dashboard featuring astronaut information, monitoring statistics, physiological indicators, and telemetry visualizations.

![AstroHealth AI Mission Overview](assets/AstroHealthAI%20ss1.png)

### 02 — Health Monitoring

Interactive monitoring of seven physiological indicators, with historical trends, statistical summaries, and configured reference-range comparisons.

![AstroHealth AI Health Monitoring](assets/AstroHealthAI%20ss2.png)

### 03 — AI Intelligence

Machine-learning anomaly detection using Isolation Forest, with unusual observation identification, anomaly scoring, and visual analysis.

![AstroHealth AI Intelligence](assets/AstroHealthAI%20ss3.png)

### 04 — Alert Command

A dedicated monitoring interface for configured reference-range deviations, recommended verification actions, and persistent alert history.

![AstroHealth AI Alert Command](assets/AstroHealthAI%20ss4.png)

### 05 — Analytics Laboratory

Advanced data exploration featuring physiological correlation heatmaps, distribution analysis, descriptive statistics, and experimental trend projections.

![AstroHealth AI Analytics Laboratory](assets/AstroHealthAI%20ss5.png)

### 06 — Data Command

A data-management environment supporting CSV uploads, dataset validation, telemetry exports, and downloadable mission reports.

![AstroHealth AI Data Command](assets/AstroHealthAI%20ss6.png)

---

## 🎯 Problem Statement

Astronauts undertaking extended space missions require reliable approaches to monitoring physiological observations and identifying unusual changes.

Conventional data collection alone does not necessarily provide an accessible way to explore relationships, identify statistically unusual observations, and organize monitoring information.

AstroHealth AI explores a software-based approach that combines data visualization and machine learning to support the interpretation of physiological telemetry.

## 💡 Proposed Solution

The platform brings together six complementary capabilities:

1. Mission overview and astronaut monitoring.
2. Physiological indicator analysis.
3. Unsupervised machine-learning anomaly detection.
4. Monitoring alerts and verification recommendations.
5. Statistical and experimental trend analysis.
6. Data management and report generation.

## 🧠 Artificial Intelligence Methodology

The core anomaly-detection component uses **Isolation Forest**, an unsupervised machine-learning algorithm.

Isolation Forest identifies observations that are statistically unusual compared with the patterns represented in the dataset.

### Processing Workflow

```text
      PHYSIOLOGICAL TELEMETRY
                 |
                 ▼
          DATA VALIDATION
                 |
                 ▼
         FEATURE PROCESSING
                 |
                 ▼
          ISOLATION FOREST
                 |
                 ▼
        ANOMALY IDENTIFICATION
                 |
                 ▼
        MONITORING ALERTS
                 |
                 ▼
       INTERACTIVE ANALYTICS
                 |
                 ▼
          MISSION CONTROL
```

### Physiological Indicators

| Indicator | Measurement |
|---|---|
| Heart Rate | Beats per minute |
| Blood Oxygen | Percentage |
| Body Temperature | Celsius |
| Respiration | Breaths per minute |
| Systolic Pressure | mmHg |
| Diastolic Pressure | mmHg |
| Activity Level | Percentage |

The platform also calculates anomaly scores to help users explore the degree of statistical unusualness in individual observations.

## ✨ Key Features

| Module | Capabilities |
|---|---|
| Mission Overview | Astronaut profile, telemetry overview, KPI cards |
| Health Monitoring | Seven indicators, interactive charts, range comparisons |
| AI Intelligence | Isolation Forest, anomaly scores, flagged observations |
| Alert Command | Monitoring alerts, recommendations, SQLite history |
| Analytics Laboratory | Correlation heatmaps, distributions, trend projections |
| Data Command | CSV upload, validation, exports, mission reports |

## 🛠️ Technology Stack

- **Python** — Core application development.
- **Streamlit** — Interactive mission-control dashboard.
- **Pandas** — Data manipulation and processing.
- **NumPy** — Numerical computation.
- **Scikit-learn** — Machine-learning anomaly detection.
- **Plotly** — Interactive data visualizations.
- **SQLite** — Persistent alert history.

## 🏗️ Project Architecture

```text
AstroHealthAI/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── AstroHealthAI ss1.png
│   ├── AstroHealthAI ss2.png
│   ├── AstroHealthAI ss3.png
│   ├── AstroHealthAI ss4.png
│   ├── AstroHealthAI ss5.png
│   └── AstroHealthAI ss6.png
│
├── data/
│
├── modules/
│   ├── __init__.py
│   ├── data_engine.py
│   ├── health_analyzer.py
│   ├── anomaly_detector.py
│   ├── recommendations.py
│   └── database.py
│
└── .streamlit/
    └── config.toml
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ab9eha/AstroHealth_AI.git
cd AstroHealth_AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run AstroHealth AI

```bash
python -m streamlit run app.py
```

The application will provide a local URL in the terminal.

## 📊 Data Handling

The application generates synthetic physiological telemetry for demonstration and testing.

It also supports CSV uploads containing the following required columns:

```text
timestamp
heart_rate
spo2
temperature
respiration
systolic
diastolic
activity
```

Uploaded data is validated and processed before being used in the monitoring interface.

## 🔬 Innovation and Potential Impact

AstroHealth AI explores the potential of combining machine learning, physiological monitoring, and interactive analytics in a single software environment.

Its central idea is to make physiological observations easier to explore while highlighting statistically unusual patterns that may warrant further review.

Potential applications include:

- Supporting the organization of astronaut health observations.
- Making physiological trends easier to interpret.
- Highlighting unusual data patterns for further investigation.
- Exploring AI-assisted monitoring workflows.
- Supporting future research into intelligent space-health software.

## 🔭 Future Development

Future development opportunities include:

- Integration with relevant validated astronaut health datasets.
- Personalized physiological baseline modelling.
- More advanced anomaly explanation techniques.
- Improved alert prioritization.
- Offline-first capabilities for space environments.
- Integration of additional environmental monitoring indicators.
- Validation with aerospace and medical experts.

## ⚠️ Limitations and Disclaimer

AstroHealth AI is an educational and research prototype.

The current application uses synthetic demonstration telemetry by default. It is not connected to live NASA mission systems or actual astronaut medical records.

Its reference ranges, demonstration health score, anomaly detection outputs, and experimental trend projections are not clinically validated.

The application does not diagnose medical conditions and is not intended to replace professional medical assessment or established astronaut healthcare procedures.

## 🏆 NASA Space Apps Challenge 2026

**Challenge:** Create Health Monitoring Software for Astronauts on Space Missions.

Official website: https://www.spaceappschallenge.org/

AstroHealth AI demonstrates an exploratory approach to AI-assisted physiological monitoring and unusual-pattern identification in the context of human space exploration.

## 👩‍💻 Developer

**Abeeha Zeeshan**

Project concept, software development, dashboard implementation, machine-learning integration, and technical documentation.

## 🔗 Project Links

- **GitHub Repository:** https://github.com/ab9eha/AstroHealth_AI.git
- **Live Application:** https://astrohealthai1.streamlit.app/
- **NASA Space Apps:** https://www.spaceappschallenge.org/

---

<p align="center">
  <b>ASTROHEALTH AI</b><br/>
  <i>Intelligent monitoring for the future of human space exploration.</i>
</p>
