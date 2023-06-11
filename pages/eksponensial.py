import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

st.title('Eksponensial Distribution')

lmbda = st.slider('Parameter Lambda (λ)', min_value=0.1, max_value=10.0, value=1.0, step=0.1)

sample = np.random.exponential(scale=1/lmbda, size=1000)

st.subheader('Histogram')
fig, ax = plt.subplots()
ax.hist(sample, bins='auto', density=True, alpha=0.7)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title(f'Distribusi Eksponensial (λ={lmbda})')
st.pyplot(fig)

st.subheader('Probability Density Function (PDF)')
x = np.linspace(expon.ppf(0.001, scale=1/lmbda), expon.ppf(0.999, scale=1/lmbda), 100)
pdf = expon.pdf(x, scale=1/lmbda)

fig, ax = plt.subplots()
ax.plot(x, pdf, 'r-', lw=2, label='PDF')
ax.set_xlabel('Nilai')
ax.set_ylabel('Probability Density')
ax.set_title(f'Distribusi Eksponensial PDF (λ={lmbda})')
st.pyplot(fig)

st.subheader('Cumulative Distribution Function (CDF)')
cdf = expon.cdf(x, scale=1/lmbda)

fig, ax = plt.subplots()
ax.plot(x, cdf, 'b-', lw=2, label='CDF')
ax.set_xlabel('Nilai')
ax.set_ylabel('Cumulative Probability')
ax.set_title(f'Distribusi Eksponensial CDF (λ={lmbda})')
st.pyplot(fig)