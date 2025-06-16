import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data yang sudah diproses
df = pd.read_csv('processed_vgsales.csv')

# Judul aplikasi Streamlit
st.title('Dashboard Penjualan Video Game')

# Menampilkan beberapa baris data
st.write('Data Penjualan Video Game:')
st.dataframe(df.head())

# Menampilkan statistik deskriptif
st.write('Statistik Deskriptif:')
st.write(df.describe())

# 1. Genre apa yang memiliki penjualan global rata-rata tertinggi?
st.subheader('1. Genre dengan Penjualan Global Rata-rata Tertinggi')

# Menghitung rata-rata penjualan global berdasarkan genre
genre_sales_avg = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False)

# Menampilkan hasil analisis genre dengan penjualan global tertinggi
st.write(genre_sales_avg)

# Visualisasi Penjualan Global berdasarkan Genre
plt.figure(figsize=(10, 6))
genre_sales_avg.plot(kind='bar', color='skyblue')
plt.title('Rata-rata Penjualan Global berdasarkan Genre')
plt.xlabel('Genre')
plt.ylabel('Rata-rata Penjualan Global (juta)')
st.pyplot(plt)

# 2. Apakah terdapat perbedaan signifikan dalam penjualan global berdasarkan platform yang digunakan?
st.subheader('2. Perbedaan Penjualan Global Berdasarkan Platform')

# Menghitung penjualan global berdasarkan platform
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)

# Menampilkan hasil analisis penjualan global berdasarkan platform
st.write(platform_sales)

# Visualisasi Penjualan Global berdasarkan Platform
plt.figure(figsize=(12, 6))
platform_sales.plot(kind='bar', color='orange')
plt.title('Total Penjualan Global Berdasarkan Platform')
plt.xlabel('Platform')
plt.ylabel('Total Penjualan Global (juta)')
st.pyplot(plt)

# 3. Bagaimana tren penjualan video game dari tahun ke tahun?
st.subheader('3. Tren Penjualan Video Game dari Tahun ke Tahun')

# Menghitung penjualan global berdasarkan tahun
yearly_sales = df.groupby('Year')['Global_Sales'].sum()

# Menampilkan tren penjualan video game dari tahun ke tahun
st.write(yearly_sales)

# Visualisasi Tren Penjualan Global
plt.figure(figsize=(10, 6))
yearly_sales.plot(kind='line', marker='o', color='green')
plt.title('Tren Penjualan Global Video Game dari Tahun ke Tahun')
plt.xlabel('Tahun')
plt.ylabel('Total Penjualan Global (juta)')
st.pyplot(plt)

# 4. Apakah ada hubungan antara genre video game dan penjualan global?
st.subheader('4. Hubungan antara Genre dan Penjualan Global')

# Visualisasi hubungan antara genre dan penjualan global
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Genre', y='Global_Sales', palette='viridis')
plt.title('Hubungan antara Genre dan Penjualan Global')
plt.xlabel('Genre')
plt.ylabel('Penjualan Global (juta)')
plt.xticks(rotation=45)
st.pyplot(plt)

# 5. Platform mana yang paling banyak menghasilkan penjualan di setiap wilayah (NA, EU, JP)?
st.subheader('5. Platform dengan Penjualan Tertinggi di Setiap Wilayah')

# Menghitung penjualan berdasarkan wilayah (NA, EU, JP) dan platform
platform_na_sales = df.groupby('Platform')['NA_Sales'].sum().sort_values(ascending=False)
platform_eu_sales = df.groupby('Platform')['EU_Sales'].sum().sort_values(ascending=False)
platform_jp_sales = df.groupby('Platform')['JP_Sales'].sum().sort_values(ascending=False)

# Menampilkan hasil analisis platform dengan penjualan tertinggi di setiap wilayah
st.write('Penjualan Platform di Amerika Utara (NA):')
st.write(platform_na_sales)

st.write('Penjualan Platform di Eropa (EU):')
st.write(platform_eu_sales)

st.write('Penjualan Platform di Jepang (JP):')
st.write(platform_jp_sales)

# Visualisasi Platform dengan Penjualan Tertinggi di Setiap Wilayah
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

platform_na_sales.plot(kind='bar', color='red', ax=axs[0])
axs[0].set_title('Penjualan Platform di Amerika Utara (NA)')
axs[0].set_xlabel('Platform')
axs[0].set_ylabel('Penjualan NA (juta)')

platform_eu_sales.plot(kind='bar', color='blue', ax=axs[1])
axs[1].set_title('Penjualan Platform di Eropa (EU)')
axs[1].set_xlabel('Platform')
axs[1].set_ylabel('Penjualan EU (juta)')

platform_jp_sales.plot(kind='bar', color='purple', ax=axs[2])
axs[2].set_title('Penjualan Platform di Jepang (JP)')
axs[2].set_xlabel('Platform')
axs[2].set_ylabel('Penjualan JP (juta)')

st.pyplot(fig)

