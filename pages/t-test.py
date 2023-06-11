import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t, ttest_1samp

st.title('T Distribution')

data = st.text_area("Enter the data (comma-separated):")
data_list = [float(x.strip()) for x in data.split(',') if x.strip()]

df = pd.DataFrame(data_list, columns=['data'])

with st.expander("View data"):
    st.dataframe(df)

with st.expander("View statistics"):
    st.dataframe(df.describe())

alpha = st.number_input("Enter the significance level (alpha):", value=0.05)
alpha_t = t.ppf(1 - alpha / 2, len(df) - 1)

null_mean = st.number_input("Enter the null hypothesis mean:")

if len(df) > 1:
    t_score, p_value = ttest_1samp(df['data'], null_mean)

    clicked = st.button('Do the t test !!')

    if clicked:
        if abs(t_score) > alpha_t:
            st.write('Reject H0')
        else:
            st.write('Cannot reject H0')

        st.write('t-score:', t_score)
        st.write('Critical t-value:', alpha_t)

        fig, ax = plt.subplots()
        ax.hist(df['data'], bins='auto', density=True, alpha=0.7)
        ax.set_xlabel('Data')
        ax.set_ylabel('Density')
        ax.set_title('Histogram')
        st.pyplot(fig)

        x = np.linspace(df['data'].min(), df['data'].max(), 100)
        pdf = t.pdf(x, df=len(df) - 1, loc=df['data'].mean(), scale=df['data'].std())
        fig, ax = plt.subplots()
        ax.plot(x, pdf, 'r-', lw=2)
        ax.set_xlabel('Data')
        ax.set_ylabel('Probability Density')
        ax.set_title('Probability Density Function (PDF)')
        st.pyplot(fig)

        cdf = t.cdf(x, df=len(df) - 1, loc=df['data'].mean(), scale=df['data'].std())
        fig, ax = plt.subplots()
        ax.plot(x, cdf, 'b-', lw=2)
        ax.set_xlabel('Data')
        ax.set_ylabel('Cumulative Probability')
        ax.set_title('Cumulative Distribution Function (CDF)')
        st.pyplot(fig)

else:
    st.write("Error: Insufficient data points, unable to perform t-test.")