import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

st.title('Chi-Square Distribution')

df = st.slider('Degree of Freedom (df)', min_value=1, max_value=30, value=10)

sample = np.random.chisquare(df, size=1000)

st.subheader('Histogram')
fig, ax = plt.subplots()
ax.hist(sample, bins='auto', density=True, alpha=0.7)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title(f'Distribusi Chi-Square (df={df})')
st.pyplot(fig)

st.subheader('Probability Density Function (PDF)')
x = np.linspace(chi2.ppf(0.001, df), chi2.ppf(0.999, df), 100)
pdf = chi2.pdf(x, df)

fig, ax = plt.subplots()
ax.plot(x, pdf, 'r-', lw=2, label='PDF')
ax.set_xlabel('Nilai')
ax.set_ylabel('Probability Density')
ax.set_title(f'Distribusi Chi-Square PDF (df={df})')
st.pyplot(fig)

st.subheader('Cumulative Distribution Function (CDF)')
cdf = chi2.cdf(x, df)

fig, ax = plt.subplots()
ax.plot(x, cdf, 'b-', lw=2, label='CDF')
ax.set_xlabel('Nilai')
ax.set_ylabel('Cumulative Probability')
ax.set_title(f'Distribusi Chi-Square CDF (df={df})')
st.pyplot(fig)