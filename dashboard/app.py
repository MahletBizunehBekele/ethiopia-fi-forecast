import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# -------------------------
# Configuration
# -------------------------

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)


BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------
# Load data
# -------------------------

enriched = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "ethiopia_fi_enriched.csv"
)


unified = pd.read_csv(
    BASE_DIR /
    "data" /
    "raw" /
    "ethiopia_fi_unified_data.csv"
)


forecast_path = (
    BASE_DIR /
    "data" /
    "processed" /
    "account_ownership_forecast.csv"
)


if forecast_path.exists():
    forecast = pd.read_csv(forecast_path)



# Convert dates

enriched["observation_date"] = pd.to_datetime(
    enriched["observation_date"],
    errors="coerce"
)


unified["observation_date"] = pd.to_datetime(
    unified["observation_date"],
    errors="coerce"
)


# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Dashboard Filters")

selected_categories = st.sidebar.multiselect(
    "Select Category",
    enriched["category"].dropna().unique(),
    default=enriched["category"].dropna().unique()
)


if selected_categories:
    enriched = enriched[
        enriched["category"].isin(selected_categories)
    ]
# -------------------------
# Header
# -------------------------

st.title(
    "🇪🇹 Ethiopia Financial Inclusion Dashboard"
)


st.markdown(
"""
Interactive dashboard integrating enriched indicators,
event impact analysis, and financial inclusion projections.
"""
)



# -------------------------
# KPI cards
# -------------------------

st.header("Overview")


c1,c2,c3,c4 = st.columns(4)


with c1:
    st.metric(
        "Total Records",
        len(enriched)
    )


with c2:
    st.metric(
        "Indicators",
        enriched["indicator"].nunique()
    )


with c3:
    st.metric(
        "Events",
        len(
            unified[
                unified.record_type=="event"
            ]
        )
    )


with c4:
    regions = enriched["region"].dropna().nunique()

    st.metric(
        "Regions Covered",
        regions if regions > 0 else "N/A"
    )


# -------------------------
# Indicator Explorer
# -------------------------

st.header(
    "Indicator Trends"
)


indicator = st.selectbox(
    "Choose indicator",
    enriched["indicator"].dropna().unique()
)


trend = enriched[
    enriched["indicator"]==indicator
]


trend = trend.sort_values(
    "observation_date"
)



fig = px.line(
    trend,
    x="observation_date",
    y="value_numeric",
    markers=True,
    title=f"{indicator} over time"
)


st.plotly_chart(
    fig,
    use_container_width=True
)

st.info(
"""
This interactive view shows historical changes in selected
financial inclusion indicators over time. Users can explore
different indicators to identify long-term trends.
"""
)

# -------------------------
# Event Impact Analysis
# -------------------------

st.header(
    "Event Impact Analysis"
)


events = enriched[
    enriched["record_type"]=="event"
]


impact = events[
    [
        "indicator",
        "impact_direction",
        "impact_magnitude",
        "impact_estimate",
        "lag_months",
        "evidence_basis"
    ]
]


st.dataframe(
    impact,
    use_container_width=True
)



if len(events)>0:

    fig = px.bar(
        events,
        x="impact_direction",
        y="impact_estimate",
        color="impact_magnitude",
        title="Estimated Event Impact"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
    """
    Event impacts are analyzed using linked indicators,
    impact direction, estimated magnitude, and expected lag.
    This helps evaluate how major events may influence
    financial inclusion outcomes.
    """
    )

# -------------------------
# Forecast Section
# -------------------------

st.header(
    "Account Ownership Forecast"
)


if forecast_path.exists():

    historical = enriched[
        enriched["indicator_code"]
        ==
        "ACC_OWNERSHIP"
    ]


    historical = (
        historical
        .groupby("observation_date")
        ["value_numeric"]
        .mean()
        .reset_index()
    )


    forecast_plot = forecast.copy()


    forecast_plot["Date"] = pd.to_datetime(
        forecast_plot["Year"],
        format="%Y"
    )


    fig = px.line(
        historical,
        x="observation_date",
        y="value_numeric",
        markers=True,
        title="Historical + Forecast"
    )


    fig.add_scatter(
        x=forecast_plot["Date"],
        y=forecast_plot["Forecast"],
        mode="lines+markers",
        name="Forecast"
    )


    fig.add_scatter(
        x=forecast_plot["Date"],
        y=forecast_plot["Optimistic"],
        mode="lines+markers",
        name="Optimistic Scenario"
    )


    fig.add_scatter(
        x=forecast_plot["Date"],
        y=forecast_plot["Pessimistic"],
        mode="lines+markers",
        name="Pessimistic Scenario"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.info(
    """
    The forecast section extends historical account ownership
    trends into future years and compares baseline projections
    with optimistic and pessimistic scenarios.
    """
    )

else:

    st.warning(
        "Forecast file not found. Run forecasting notebook first."
    )



# -------------------------
# Scenario Simulator
# -------------------------

st.header(
    "Scenario Simulation"
)


growth = st.slider(
    "Adjust forecast growth (%)",
    -20,
    30,
    0
)


if forecast_path.exists():

    scenario = forecast.copy()


    scenario["Adjusted Forecast"] = (
        scenario["Forecast"]
        *
        (1 + growth/100)
    )


    fig = px.line(
        scenario,
        x="Year",
        y=[
            "Forecast",
            "Adjusted Forecast"
        ],
        markers=True,
        title="Baseline vs User Scenario"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )