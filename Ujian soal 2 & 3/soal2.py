# Soal 2 - Infografis ASEAN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlalchemy
import seaborn as sns


mydb = sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://zaky9:september@1@localhost:3306/world'
)
query = 'select Negara_ASEAN, Populasi_Negara, GNP, SurfaceArea from asean'
df = pd.read_sql(query, mydb)
nama = df['Negara_ASEAN'].values
populasi = df['Populasi_Negara'].values
GNP = df['GNP'].values
area = df['SurfaceArea'].values
# print(area)


# Soal 2.1: Populasi Negara ASEAN
# Bar Chart
plt.figure('Populasi Negara Asean') 
plt.style.use('seaborn-whitegrid')
plt.bar(nama, populasi, width = 0.5, color=['red', 'Green', 'yellow', 'purple', 'pink' ,'violet', 'brown', 'orange','blue','grey'])
plt.title('Populasi Negara ASEAN', fontsize=20)
plt.xlabel("Negara", fontsize=15)
plt.xticks(nama, rotation= 30)
plt.ylabel("Populasi (x100 jiwa)", fontsize=15)
plt.grid(zorder=0)

for i, j in enumerate(populasi):
    plt.text(i-.3, j, str(j), color='black')
# plt.show()


# Soal ke 2.2: Persentase Penduduk ASEAN
#Pie chart
plt.figure('Persentase Penduduk Asean') 
plt.pie(populasi, labels=nama, shadow= False, 
    autopct='%1.1f%%') 
plt.axis('equal')  
plt.title('Persentase Penduduk ASEAN')
# plt.show()


# Soal ke 2.3: Gross National Product ASEAN
plt.figure('Pendapatan Bruto Nasional Asean') 
plt.style.use('seaborn-whitegrid')
plt.bar(nama, GNP,width=0.5,color=['red', 'Green', 'yellow', 'purple', 'pink' ,'violet', 'brown', 'orange','blue','grey'], zorder=3 )
plt.title('Pendapatan Bruto Nasional ASEAN', fontsize=20)
plt.xlabel("Negara", fontsize=15)
plt.xticks(nama, rotation= 30)
plt.ylabel("Gross National Products", fontsize=15)
plt.grid(zorder=0)

for i, j in enumerate(GNP):
    plt.text(i-.25, j, str(j), color='black')
# plt.show()


# Soal ke 2.4:Persentase Luas Daratan ASEAN
plt.figure('Persentase Luas Daratan Asean') 
plt.pie(area, labels=nama, shadow= False, 
    autopct='%1.1f%%')

plt.axis('equal')  
plt.title('Persentase Luas Daratan ASEAN')

plt.show()


