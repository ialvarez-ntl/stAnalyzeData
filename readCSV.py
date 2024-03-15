import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def TractarCSVVodafone(strPath, strPathDesti, df):
    strFecha = strPath.split('_')[2][0:8]
    strFecha = datetime.strptime(strFecha, "%Y%m%d")

    df.columns = df.columns.str.strip()

    df_agrupat = df.groupby(['ADDRESSTO']).size().reset_index(name='CONTA').sort_values(by='CONTA', ascending=False)
    df_agrupat['ADDRESSTO'] = df_agrupat['ADDRESSTO'].astype(str)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_ylabel('Destinataris')
    ax.set_xlabel('Número de trucades')
    ax.set_title('Trucades del dia ' + strFecha.strftime("%d/%m/%Y"))
    plt.barh(df_agrupat['ADDRESSTO'], df_agrupat['CONTA'])
    for i, v in enumerate(df_agrupat['CONTA']):
        ax.text(v + 1.1, i - .25, str(v),
                color='blue', fontweight='bold')
    return fig