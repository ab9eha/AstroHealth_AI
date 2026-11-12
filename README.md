# 🛰️ AstroHealth AI
### Intelligent Astronaut Health Monitoring & Mission Control System

An AI-powered health-monitoring dashboard designed to help astronauts explore physiological telemetry, identify unusual patterns, and review health indicators during space missions.

**Built for the NASA Space Apps Challenge 2026**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)
![Machine Learning](https://img.shields.io/badge/AI-Isolation%20Forest-8A63D2)
![Status](https://img.shields.io/badge/Status-Prototype-35A67A)

---

## 🌌 Project Overview

Long-duration space missions expose astronauts to demanding environmental conditions, including microgravity, isolation, confinement, and radiation. Monitoring physiological changes and identifying unusual health patterns are important parts of supporting astronaut well-being.

**AstroHealth AI** is an interactive mission-control platform that brings physiological monitoring, machine-learning-based anomaly detection, and analytical visualizations into one interface.

The prototype demonstrates how an intelligent monitoring system could help astronauts and mission personnel review health observations and identify readings that may require further attention.

## 🎯 Problem We Address

Astronauts on extended missions need accessible ways to monitor health indicators and recognize unusual changes. A system that combines organized health data, visual analytics, and automated pattern detection could support more informed monitoring and follow-up.

AstroHealth AI explores this concept through a modular software prototype.

## ✨ Key Features

### 1. Mission Overview
- Mission-control dashboard with astronaut profile.
- Physiological telemetry summary cards.
- Interactive heart-rate, blood-oxygen, temperature, and respiration charts.
- Monitoring status overview.

### 2. Physiological Health Monitoring
- Seven monitored indicators:
  - Heart rate
  - Blood oxygen saturation
  - Body temperature
  - Respiration rate
  - Systolic blood pressure
  - Diastolic blood pressure
  - Activity level
- Historical trend exploration.
- Configured reference-range comparisons.

### 3. AI Intelligence
- Unsupervised anomaly detection using Isolation Forest.
- Identification of statistically unusual observations.
- Anomaly scores and visual comparisons.
- Flagged-observation review.

### 4. Alert Command
- Configured reference-range deviation alerts.
- Recommended verification actions.
- Persistent alert history using SQLite.
- Downloadable alert records.

### 5. Analytics Laboratory
- Physiological correlation heatmap.
- Statistical distribution analysis.
- Descriptive statistics.
- Experimental linear trend projections.

### 6. Data Command
- CSV dataset upload and validation.
- Downloadable telemetry data.
- Mission report generation.
- Demonstration dataset reset and regeneration.

## 🧠 AI & Technical Methodology

AstroHealth AI uses an Isolation Forest model for unsupervised anomaly detection.

The model examines physiological observations and identifies patterns that are statistically unusual relative to the dataset.

The prototype's workflow:

1. Generate or import physiological telemetry.
2. Validate timestamps and numerical measurements.
3. Process the observations for machine-learning analysis.
4. Apply Isolation Forest anomaly detection.
5. Calculate anomaly scores and flag unusual observations.
6. Present results through interactive charts and monitoring panels.
7. Display configured alerts and recommended verification actions.

The experimental trend projection uses a simple linear regression fit to recent observations. It is intended for demonstration and is not a validated medical forecasting method.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive dashboard |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and anomaly detection |
| Plotly | Interactive data visualization |
| SQLite | Persistent alert storage |

## 🏗️ Application Architecture

```text
                 ASTROHEALTH AI
                       |
             Physiological Telemetry
                       |
              Data Validation Layer
                       |
              Health Analysis Layer
                       |
          Machine Learning Detection
                       |
             Alert & Recommendation
                       |
              Analytics Dashboard
                       |
             Mission Control Interface
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AstroHealth-AI.git
cd AstroHealth-AI
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

### 5. Launch the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## 📂 Project Structure

```text
AstroHealthAI/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
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

## 📊 Data & Demonstration

The current application generates synthetic physiological telemetry for demonstration and testing. Users can also import a CSV file containing the required columns:

`timestamp, heart_rate, spo2, temperature, respiration, systolic, diastolic, activity`

The synthetic observations are not actual astronaut medical records or NASA mission telemetry.

## 🔭 Future Development

Potential future extensions include:

- Integration with validated spaceflight health datasets and relevant open research resources.
- Offline-first operation for environments with limited connectivity.
- More advanced personalized baseline analysis.
- Improved anomaly explanations and alert prioritization.
- Additional environmental and behavioral health monitoring.
- Validation with domain experts and appropriate medical standards.

## ⚠️ Important Disclaimer

AstroHealth AI is an educational and research prototype. It uses synthetic demonstration data by default. Its anomaly detection, configured reference ranges, health indicator score, and experimental projections are not clinically validated.

The application is not a medical device, does not diagnose medical conditions, and must not replace professional medical assessment or established mission medical procedures.

## 🏆 Challenge

Created in response to the NASA Space Apps Challenge 2026 challenge:

**Create Health Monitoring Software for Astronauts on Space Missions**

Official challenge: https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/

## 👩‍💻 Developer

**Abeeha Zeeshan**

Project concept, software development, dashboard implementation, machine-learning integration, and documentation.

---

*Exploring how intelligent software can support human health monitoring beyond Earth.*