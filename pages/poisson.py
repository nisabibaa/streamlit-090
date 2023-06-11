import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.title('Poisson Distribution')

lmbda = st.slider('Parameter Lambda (λ)', min_value=0.1, max_value=10.0, value=1.0, step=0.1)

sample = np.random.poisson(lmbda, size=1000)

st.subheader('Histogram')
fig, ax = plt.subplots()
ax.hist(sample, bins='auto', density=True, alpha=0.7)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title(f'Distribusi Poisson (λ={lmbda})')
st.pyplot(fig)

st.subheader('Probability Density Function (PDF)')
x = np.arange(poisson.ppf(0.001, lmbda), poisson.ppf(0.999, lmbda))
pmf = poisson.pmf(x, lmbda)

fig, ax = plt.subplots()
ax.plot(x, pmf, 'ro', ms=8)
ax.vlines(x, 0, pmf, colors='r', lw=5)
ax.set_xlabel('Nilai')
ax.set_ylabel('Probability Mass')
ax.set_title(f'Distribusi Poisson PMF (λ={lmbda})')
st.pyplot(fig)

st.subheader('Cumulative Distribution Function (CDF)')
cdf = poisson.cdf(x, lmbda)

fig, ax = plt.subplots()
ax.plot(x, cdf, 'b-', lw=2, label='CDF')
ax.set_xlabel('Nilai')
ax.set_ylabel('Cumulative Probability')
ax.set_title(f'Distribusi Poisson CDF (λ={lmbda})')
st.pyplot(fig)