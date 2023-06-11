import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

st.title('Binomial Distribution')

n = st.slider('Jumlah Percobaan (n)', min_value=1, max_value=100, value=10)
p = st.slider('Probabilitas Keberhasilan (p)', min_value=0.1, max_value=1.0, value=0.5, step=0.1)

sample = np.random.binomial(n, p, size=1000)

st.subheader('Histogram')
fig, ax = plt.subplots()
ax.hist(sample, bins=np.arange(n+2)-0.5, density=True, alpha=0.7)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title(f'Distribusi Binomial (n={n}, p={p})')
st.pyplot(fig)

st.subheader('Probability Density Function (PDF)')
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

fig, ax = plt.subplots()
ax.plot(x, pmf, 'ro', ms=8)
ax.vlines(x, 0, pmf, colors='r', lw=5)
ax.set_xlabel('Nilai')
ax.set_ylabel('Probability Mass')
ax.set_title(f'Distribusi Binomial PMF (n={n}, p={p})')
st.pyplot(fig)

st.subheader('Cumulative Distribution Function (CDF)')
cdf = binom.cdf(x, n, p)

fig, ax = plt.subplots()
ax.plot(x, cdf, 'b-', lw=2, label='CDF')
ax.set_xlabel('Nilai')
ax.set_ylabel('Cumulative Probability')
ax.set_title(f'Distribusi Binomial CDF (n={n}, p={p})')
st.pyplot(fig)