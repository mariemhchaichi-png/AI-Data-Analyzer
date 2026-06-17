import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# Configuration
# -------------------------

st.set_page_config(
    page_title="AI Data Analyzer",
    page_icon="📊",
    layout="wide"
)


# -------------------------
# Title
# -------------------------

st.title("📊 AI Data Analyzer")

st.write(
    "Upload your CSV dataset and explore your data 🚀"
)


# -------------------------
# Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)


if uploaded_file is not None:


    df = pd.read_csv(uploaded_file)


    st.success(
        "Dataset uploaded successfully!"
    )


    

    st.header("Dataset Preview")

    st.dataframe(
        df.head()
    )


    # -------------------------
    # Dataset information
    # -------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Rows",
            df.shape[0]
        )


    with col2:

        st.metric(
            "Columns",
            df.shape[1]
        )



    # -------------------------
    # Columns
    # -------------------------

    st.header("📋 Columns")

    st.write(
        df.columns.tolist()
    )



    # -------------------------
    # Statistics
    # -------------------------

    st.header("📊 Statistics")

    st.dataframe(
        df.describe()
    )



    # -------------------------
    # Missing values
    # -------------------------

    st.header("🔍 Missing Values")


    missing = df.isnull().sum().reset_index()

    missing.columns = [
        "Column",
        "Missing Values"
    ]


    st.dataframe(
        missing
    )



    # -------------------------
    # Histogram
    # -------------------------

    st.header("📈 Histogram")


    numeric_columns = df.select_dtypes(
        include="number"
    ).columns


    selected_column = st.selectbox(
        "Choose numeric column",
        numeric_columns
    )


    fig, ax = plt.subplots()


    ax.hist(
        df[selected_column].dropna(),
        bins=20
    )


    ax.set_title(
        f"Distribution of {selected_column}"
    )


    ax.set_xlabel(
        selected_column
    )


    ax.set_ylabel(
        "Frequency"
    )


    st.pyplot(fig)



    # -------------------------
    # Bar Chart
    # -------------------------

    st.header("📊 Bar Chart")


    column = st.selectbox(
        "Choose column",
        df.columns
    )


    chart_data = df[column].value_counts()


    st.bar_chart(
        chart_data
    )



    # -------------------------
    # Correlation Heatmap
    # -------------------------

    st.header("Correlation Heatmap")


    numeric_df = df.select_dtypes(
        include="number"
    )


    if len(numeric_df.columns) > 1:


        fig, ax = plt.subplots()


        correlation = numeric_df.corr()


        image = ax.imshow(
            correlation
        )


        ax.set_xticks(
            range(len(correlation.columns))
        )

        ax.set_yticks(
            range(len(correlation.columns))
        )


        ax.set_xticklabels(
            correlation.columns,
            rotation=45
        )


        ax.set_yticklabels(
            correlation.columns
        )


        st.pyplot(fig)


    else:

        st.info(
            "Not enough numeric columns for correlation"
        )



    # -------------------------
    # Download Report
    # -------------------------

    st.header("Download Report")


    report = f"""
AI Data Analyzer Report

Rows:
{df.shape[0]}

Columns:
{df.shape[1]}

Column names:
{list(df.columns)}

Missing values:

{missing.to_string()}


Statistics:

{df.describe().to_string()}
"""


    st.download_button(
        label="Download Report",
        data=report,
        file_name="analysis_report.txt",
        mime="text/plain"
    )