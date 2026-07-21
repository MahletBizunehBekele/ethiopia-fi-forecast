# Ethiopia Financial Inclusion Forecasting

## Project Overview

This project analyzes financial inclusion trends in Ethiopia by combining historical observations, policy events, and impact relationships. It explores the data, enriches the dataset, models event impacts, generates forecasts for financial inclusion indicators, and presents the results through a simple Streamlit dashboard.

---

## Repository Structure

```
ethiopia-fi-forecast/
│
├── data/
│   ├── raw/                # Original datasets
│   └── processed/          # Enriched datasets
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 03_event_impact_modeling.ipynb
│   └── 04_forecasting.ipynb
│
├── dashboard/
│   └── app.py              # Streamlit dashboard
│
├── src/
│   └── data_loader.py      # Data loading utilities
│
├── data_enrichment_log.md
├── requirements.txt
└── README.md
```

---

## Project Tasks

### Task 1 – Data Exploration and Enrichment
- Loaded and explored the unified financial inclusion dataset.
- Documented the dataset schema.
- Added enriched observations following the required schema.
- Recorded enrichment details in `data_enrichment_log.md`.

### Task 2 – Exploratory Data Analysis
- Explored record types, pillars, confidence levels, and source types.
- Visualized financial inclusion indicators.
- Examined account ownership and mobile money trends.
- Documented key insights and dataset limitations.

### Task 3 – Event Impact Modeling
- Explored relationships between events and indicators.
- Built an event-indicator association matrix.
- Documented methodology and impact assumptions.

### Task 4 – Forecasting
- Generated simple forecasts for account ownership (2025–2027).
- Included baseline and scenario-based projections.
- Discussed forecast uncertainty and interpretation.

### Task 5 – Dashboard
- Developed a Streamlit dashboard.
- Displayed summary metrics and visualizations.
- Included historical trends and forecast results.

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## Author

Mahlet 