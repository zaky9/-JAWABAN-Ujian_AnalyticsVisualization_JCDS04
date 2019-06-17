# Soal 3.1 - Harga Historis Saham Provider Telco Indonesia
# ata plot harga penutupan (close) harian seluruh data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excl = pd.read_csv('EXCL.JK.csv', index_col=False, parse_dates=['Date'])
fren = pd.read_csv('FREN.JK.csv', index_col=False, parse_dates=['Date'])
isat = pd.read_csv('ISAT.JK.csv', index_col=False, parse_dates=['Date'])
tlkm = pd.read_csv('TLKM.JK.csv', index_col=False, parse_dates=['Date'])

plt.style.use('seaborn-whitegrid')
plt.plot(excl['Date'], excl['Close'])
plt.plot(fren['Date'], fren['Close'])
plt.plot(isat['Date'], isat['Close'])
plt.plot(tlkm['Date'], tlkm['Close'])
# plt.show()

plt.title('Harga Historis Saham Provider Telco Indonesia', fontsize=20)
plt.xticks(rotation=50)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')

legends = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(legends, mode='expand', ncol=5)

plt.show()