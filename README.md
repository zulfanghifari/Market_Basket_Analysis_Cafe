# Market Basket Analysis dengan Algoritma Apriori

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://marketbasketanalysiscafe.streamlit.app/)

Aplikasi web interaktif untuk analisis keranjang belanja (Market Basket Analysis) menggunakan algoritma Apriori. Aplikasi ini membantu mengidentifikasi pola pembelian produk dan memberikan rekomendasi produk berdasarkan asosiasi antar item.

## 🌐 Live Demo

**Coba aplikasi langsung:** [https://marketbasketanalysiscafe.streamlit.app/](https://marketbasketanalysiscafe.streamlit.app/)

## 📋 Deskripsi

Aplikasi ini menganalisis data transaksi penjualan untuk menemukan produk-produk yang sering dibeli bersamaan. Dengan menggunakan algoritma Apriori, aplikasi dapat:
- Menemukan pola pembelian pelanggan
- Memberikan rekomendasi produk
- Membantu strategi cross-selling dan bundle promotion
- Optimasi penempatan produk dan manajemen inventori

## 🚀 Fitur Utama

- **Filter Interaktif**: Pilih item, periode waktu, hari, dan bulan
- **Analisis Apriori**: Algoritma Apriori untuk menemukan asosiasi antar produk
- **Hasil Rekomendasi**: Rekomendasi produk berdasarkan item yang dipilih
- **Penjelasan Metrik**: Penjelasan lengkap untuk Support, Confidence, dan Lift
- **Rekomendasi Bisnis**: Saran praktis untuk implementasi hasil analisis
- **Detail Statistik**: Lihat top 5 rekomendasi dengan metrik lengkap

## 📦 Teknologi yang Digunakan

- **Python 3.7+**
- **Streamlit**: Framework untuk web aplikasi
- **Pandas**: Manipulasi dan analisis data
- **NumPy**: Komputasi numerik
- **MLxtend**: Implementasi algoritma Apriori dan Association Rules

## 🔧 Instalasi

### 1. Clone atau Download Repository

```bash
git clone <repository-url>
cd market-basket-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Atau install secara manual:

```bash
pip install streamlit pandas numpy mlxtend
```

### 3. Persiapkan Data

Pastikan file `bread basket.csv` berada di folder yang sama dengan `app.py`. File CSV harus memiliki struktur kolom berikut:
- `Transaction`: ID transaksi
- `Item`: Nama produk
- `date_time`: Waktu transaksi
- `period_day`: Periode waktu (morning, afternoon, evening, night)
- `weekday_weekend`: Tipe hari (weekday/weekend)

## 🎯 Cara Menjalankan

### Opsi 1: Gunakan Aplikasi Online (Recommended)

Langsung akses aplikasi yang sudah live di:
**[https://marketbasketanalysiscafe.streamlit.app/](https://marketbasketanalysiscafe.streamlit.app/)**

### Opsi 2: Jalankan Secara Lokal

Jalankan aplikasi dengan perintah:

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`

## 📊 Cara Menggunakan

1. **Pilih Item**: Gunakan dropdown untuk memilih produk yang ingin dianalisis
2. **Atur Filter** (opsional):
   - Period Day: Pilih waktu dalam sehari
   - Weekday/Weekend: Pilih tipe hari
   - Month: Gunakan slider untuk memilih bulan
   - Day: Gunakan slider untuk memilih hari dalam seminggu
3. **Lihat Hasil**: Aplikasi akan menampilkan rekomendasi produk yang sering dibeli bersamaan
4. **Eksplorasi Detail**: Klik "Lihat Detail Metrik" untuk melihat statistik lengkap
5. **Baca Penjelasan**: Scroll ke bawah untuk memahami metrik dan rekomendasi bisnis

## 📈 Interpretasi Metrik

### Support
Persentase transaksi yang mengandung kombinasi item tertentu.
- **Tinggi**: Item sering dibeli bersama
- **Rendah**: Item jarang dibeli bersama

### Confidence
Probabilitas item B dibeli ketika item A dibeli.
- **Tinggi (>50%)**: Hubungan kuat
- **Sedang (30-50%)**: Hubungan moderat
- **Rendah (<30%)**: Hubungan lemah

### Lift
Kekuatan hubungan dibandingkan pembelian acak.
- **Lift > 1**: Item saling berkaitan positif
- **Lift = 1**: Tidak ada hubungan
- **Lift < 1**: Item berkaitan negatif

## 📝 Contoh Dataset

```csv
Transaction,Item,date_time,period_day,weekday_weekend
1,Bread,30-10-2016 09:58,morning,weekend
2,Scandinavian,30-10-2016 10:05,morning,weekend
3,Hot chocolate,30-10-2016 10:07,morning,weekend
3,Jam,30-10-2016 10:07,morning,weekend
```

## ⚙️ Konfigurasi

Anda dapat menyesuaikan parameter algoritma Apriori di dalam kode:

```python
# Minimum support (default: 0.01 atau 1%)
min_support = 0.01

# Minimum lift threshold (default: 1)
min_threshold = 1
```

## 🔍 Troubleshooting

### File tidak ditemukan
**Masalah**: `FileNotFoundError: File 'bread basket.csv' tidak ditemukan`

**Solusi**: Pastikan file CSV berada di folder yang sama dengan `app.py` atau sesuaikan path di kode:
```python
df = pd.read_csv("path/ke/file/bread basket.csv")
```

### Error saat import mlxtend
**Masalah**: `ModuleNotFoundError: No module named 'mlxtend'`

**Solusi**: Install mlxtend
```bash
pip install mlxtend
```

### Tidak ada rekomendasi
**Masalah**: Aplikasi menampilkan "Tidak ada rekomendasi yang ditemukan"

**Solusi**: 
- Pilih item yang lebih populer (coffee, bread, tea)
- Turunkan nilai `min_support` di kode

## 💡 Pengembangan Lebih Lanjut

Beberapa ide untuk pengembangan aplikasi:

- [ ] Upload file CSV langsung dari aplikasi
- [ ] Visualisasi grafik network asosiasi
- [ ] Export hasil analisis ke Excel/PDF
- [ ] Filter berdasarkan periode waktu dan hari
- [ ] Dashboard analytics dengan multiple visualisasi
- [ ] Integrasi dengan database real-time
- [ ] A/B testing untuk strategi rekomendasi

## 👥 Kontributor

- **Muhammad Zulfan Alghifari**

## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan portfolio.

## 🙏 Acknowledgments

- Dataset: Bread Basket transactions
- MLxtend library untuk implementasi Apriori
- Streamlit untuk framework aplikasi web

## 📧 Kontak

Jika ada pertanyaan atau saran, silakan hubungi:
- Email: zulfanghifari29@gmail.com
- LinkedIn: https://www.linkedin.com/in/zulfanghifari/
- GitHub: [GitHub Profile]

---

**Happy Analyzing! 🎉**
