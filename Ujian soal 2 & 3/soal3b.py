# Soal 3.2 - Harga Historis Saham Provider Telco Indonesia
# ot harga penutupan (close) harian selama bulan April 2019.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excl = pd.read_csv('EXCL.JK.csv', index_col=['Date'], parse_dates=['Date'])

# Bulan April
# EXCL
excl = excl.loc['2019-04']
excl = excl.reset_index()

# Mengisi data kosong
r = pd.date_range(start=excl['Date'].min(), end=excl['Date'].max())
excl = excl.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')
# FREN
fren = pd.read_csv('FREN.JK.csv', index_col=['Date'], parse_dates=['Date'])
fren = fren.loc['2019-04']
fren = fren.reset_index()
fren = fren.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')
# ISAT
isat = pd.read_csv('ISAT.JK.csv', index_col=['Date'], parse_dates=['Date'])
isat = isat.loc['2019-04']
isat = isat.reset_index()
isat = isat.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')
# TLKM
tlkm = pd.read_csv('TLKM.JK.csv', index_col=['Date'], parse_dates=['Date'])
tlkm = tlkm.loc['2019-04']
tlkm = tlkm.reset_index()
tlkm = tlkm.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')

plt.style.use('seaborn-whitegrid')
plt.plot(excl.loc['2019-04'].index, excl.loc['2019-04']['Close'])
plt.plot(fren.loc['2019-04'].index, fren.loc['2019-04']['Close'])
plt.plot(isat.loc['2019-04'].index, isat.loc['2019-04']['Close'])
plt.plot(tlkm.loc['2019-04'].index, tlkm.loc['2019-04']['Close'])
# plt.show()

plt.title('Harga Historis Saham Provider Telco Indonesia (April 2019)', fontsize=20)
labels = excl['2019-04'].index
plt.xticks(ticks=labels, labels=labels.date, rotation=50)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')

legends = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(legends, mode='expand', ncol=5)

plt.show()
