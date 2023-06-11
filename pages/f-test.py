import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f

st.title('F Distribution')

data1 = st.text_area("Enter data for Group 1 (comma-separated):")
data1_list = [float(x.strip()) for x in data1.split(',') if x.strip()]

data2 = st.text_area("Enter data for Group 2 (comma-separated):")
data2_list = [float(x.strip()) for x in data2.split(',') if x.strip()]

df1 = pd.DataFrame(data1_list, columns=['Group 1'])
df2 = pd.DataFrame(data2_list, columns=['Group 2'])

with st.expander("View Group 1 data"):
    st.dataframe(df1)

with st.expander("View Group 2 data"):
    st.dataframe(df2)

with st.expander("View statistics"):
    st.write("Group 1 statistics:")
    st.dataframe(df1.describe())
    st.write("Group 2 statistics:")
    st.dataframe(df2.describe())

alpha = st.number_input("Enter the significance level (alpha):", value=0.05)
alpha_f = f.ppf(1 - alpha, len(df1) - 1, len(df2) - 1)

clicked = st.button('Do the F test !!')

if clicked:
    if df1['Group 1'].var() != 0 and df2['Group 2'].var() != 0:
        f_value = np.var(df1['Group 1']) / np.var(df2['Group 2'])
        p_value = f.sf(f_value, len(df1) - 1, len(df2) - 1)

        if f_value > alpha_f:
            st.write('Reject H0')
        else:
            st.write('Cannot reject H0')

        st.write('F-value:', f_value)
        st.write('Critical F-value:', alpha_f)

        fig, ax = plt.subplots()
        ax.boxplot([df1['Group 1'], df2['Group 2']], labels=['Group 1', 'Group 2'])
        ax.set_ylabel('Data')
        ax.set_title('Boxplot')
        st.pyplot(fig)

    else:
        st.write("Error: Variance of one or both groups is zero, unable to perform F-test.")
else:
    st.write("Click the button to perform the F-test.")