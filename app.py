import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Title
st.title("📊 AI Data Analyzer")

st.write("Upload your dataset and analyze it 🚀")


# Upload CSV
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    # Read dataset
    df = pd.read_csv(uploaded_file)


    st.success("Dataset uploaded successfully!")


    # Preview
    st.subheader("👀 Preview")
    st.dataframe(df.head())


    # Shape
    st.subheader("📏 Dataset Shape")
    st.write(df.shape)


    # Columns
    st.subheader("📋 Columns")
    st.write(df.columns.tolist())


    # Statistics
    st.subheader("📊 Statistics")
    st.dataframe(df.describe())


    # Missing values
    st.subheader("🔍 Missing Values")
    missing = df.isnull().sum().reset_index()

    missing.columns = ["Column", "Missing Values"]

    st.dataframe(missing)



    # Histogram
    st.subheader("📈 Histogram")


    numeric_columns = df.select_dtypes(
        include="number"
    ).columns


    selected_column = st.selectbox(
        "Choose a numeric column",
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