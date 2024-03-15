import sys
import streamlit as st
import pandas as pd
import readCSV

st.set_page_config(page_title='Analisi trucades SAC', page_icon = '', layout = 'wide', initial_sidebar_state = 'auto')
st.image('./NTL_logo.jpg', width=200)
col1, col2 = st.columns([2,1])

col1.markdown("# Analisis trucades SAC")
col1.markdown("## Llista de trucades a la centraleta del SAC")

dades = col2.file_uploader(":phone: :blue[Carrega el(s) fitxer(s) de trucades:] "
                           , type=["csv"]
                           , accept_multiple_files=True
                           , help='Missatge')

if dades is not None:
    for dada in dades:
        df = pd.read_csv(dada)
        plot = readCSV.TractarCSVVodafone(dada.name, '', df)
        st.pyplot(plot)

