import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from statsmodels.stats.weightstats import ztest

st.title('Z Distribution')

data = st.text_area("Enter the data (comma-separated):")
data_list = [float(x.strip()) for x in data.split(',') if x.strip()]

df = pd.DataFrame(data_list, columns=['data'])

with st.expander("View data"):
    st.dataframe(df)

with st.expander("View statistics"):
    st.dataframe(df.describe())

alpha = st.number_input("Enter the significance level (alpha):", value=0.05)
alpha_z = norm().ppf(1 - alpha / 2)

null_mean = st.number_input("Enter the null hypothesis mean:")

if len(df) > 1:  
    if df['data'].var() != 0:  
        z_score, p_value = ztest(df['data'], value=null_mean, alternative='two-sided')

        clicked = st.button('Do the Z test !!')

        if clicked:
            if abs(z_score) > alpha_z:
                st.write('Reject H0')
            else:
                st.write('Cannot reject H0')

            st.write('Z-score:', z_score)
            st.write('Critical Z-value:', alpha_z)

            fig, ax = plt.subplots()
            ax.hist(df['data'], bins='auto', density=True, alpha=0.7)
            ax.set_xlabel('Data')
            ax.set_ylabel('Density')
            ax.set_title('Histogram')
            st.pyplot(fig)

            x = np.linspace(df['data'].min(), df['data'].max(), 100)
            pdf = norm.pdf(x, loc=df['data'].mean(), scale=df['data'].std())
            fig, ax = plt.subplots()
            ax.plot(x, pdf, 'r-', lw=2)
            ax.set_xlabel('Data')
            ax.set_ylabel('Probability Density')
            ax.set_title('Probability Density Function (PDF)')
            st.pyplot(fig)

            cdf = norm.cdf(x, loc=df['data'].mean(), scale=df['data'].std())
            fig, ax = plt.subplots()
            ax.plot(x, cdf, 'b-', lw=2)
            ax.set_xlabel('Data')
            ax.set_ylabel('Cumulative Probability')
            ax.set_title('Cumulative Distribution Function (CDF)')
            st.pyplot(fig)

    else:
        st.write("Error: Variance of data is zero, unable to perform Z-test.")
else:
    st.write("Error: Insufficient data points, unable to perform Z-test.")