import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

st.title("Data Explorer")

st.header("Upload your data file")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)

    st.header("Data Preview")
    st.write(data.head())

    st.header("Descriptive Statistics")
    st.write(data.describe())

    st.header("Data Information")
    buffer = StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.header("Histogram")
    columns = data.columns.tolist()
    selected_column = st.selectbox("Select a column to plot histogram", columns)

    if selected_column:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[selected_column], kde=True, bins=30)
        plt.title(f'Histogram of {selected_column}')
        plt.xlabel(selected_column)
        plt.ylabel('Frequency')
        st.pyplot(plt)

    st.header("Correlation Matrix")
    corr = data.corr()
    st.write(corr)

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Matrix Heatmap")
    st.pyplot(plt)

    st.header("Scatter Plot")
    dependent_var = st.selectbox("Select the dependent variable", columns)
    independent_var = st.selectbox("Select the independent variable", columns)

    if dependent_var and independent_var:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x=independent_var, y=dependent_var)
        plt.title(f'Scatter plot between {dependent_var} and {independent_var}')
        plt.xlabel(independent_var)
        plt.ylabel(dependent_var)
        st.pyplot(plt)