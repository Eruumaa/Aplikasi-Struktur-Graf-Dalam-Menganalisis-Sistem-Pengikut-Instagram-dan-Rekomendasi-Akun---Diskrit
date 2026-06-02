# Aplikasi Struktur Graf Dalam Menganalisis Sistem Pengikut dan Rekomendasi Akun Pada Jaringan Sosial Instagram 📊🕸️

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![NetworkX](https://img.shields.io/badge/library-NetworkX-brightgreen)
![Pandas](https://img.shields.io/badge/library-Pandas-yellow)
![Status](https://img.shields.io/badge/status-Completed-success)
![Academic](https://img.shields.io/badge/Project-Universitas%20Syiah%20Kuala-red)

Repositori ini berisi implementasi kode dalam bahasa Python untuk menganalisis topologi jaringan sosial sistem pengikut (*followers*) Instagram menggunakan Teori Graf. Proyek ini juga mengimplementasikan sistem rekomendasi akun murni menggunakan algoritma diskrit (*Jaccard Similarity*) tanpa *Machine Learning*.

Proyek ini disusun sebagai Tugas Akhir mata kuliah **Matematika Diskrit (SINF1002)**, Program Studi Informatika, Fakultas Matematika dan Ilmu Pengetahuan Alam, Universitas Syiah Kuala (USK).

## 👥 Tim Peneliti (Kelompok 7)
* **Muhammad Aqil Mubarak** (250810701100003)
* **Shofy Suhaila Putri** (250810701100007)
* **Faiz Asra** (250810701100062)
* **Virzi Mayhand Syahputra** (250810701100077)
* **Fauzana Izzati** (250810710110009)

---

## 🎯 Fitur Utama
1. **Konstruksi Graf Raksasa:** Memproses *dataset* berisi 70.410 simpul (akun) dan 1.031.349 sisi (relasi *following*) ke dalam struktur *Directed Graph*.
2. **Analisis Sentralitas (*Centrality*):** 
   * *Degree Centrality* (Mencari *hubs* / akun paling populer).
   * *Betweenness Centrality* (Menggunakan teknik aproksimasi $k=100$ untuk mencari akun "jembatan").
   * *Closeness Centrality* (Mencari akun dengan kecepatan sebar informasi tertinggi).
3. **Deteksi Komunitas (Sirkel):** Menerapkan metode **Louvain Algorithm** untuk mempartisi jaringan ke dalam komunitas-komunitas yang memiliki interaksi padat.
4. **Sistem Rekomendasi Akun:** Menggunakan **Jaccard Similarity Coefficient** berdasarkan *Common Out-Neighbors* untuk memprediksi probabilitas ketertarikan antar-akun.
5. **Visualisasi Sub-Graf:** Me-render sampel 200 akun paling berpengaruh lengkap dengan pewarnaan berdasarkan komunitas menggunakan *Matplotlib* dan *Seaborn*.

---

## 📂 Struktur Repositori

Pastikan struktur folder Anda seperti ini sebelum menjalankan program:

```text
📁 Aplikasi-Struktur-Graf/
│
├── 📁 data/
│   ├── Network for IC LT.txt       # Edge list (u, v) relasi following
│   └── Instagram User Stats.csv    # Metadata statistik pengguna
│
├── main.py                         # Skrip utama komputasi dan visualisasi
└── README.md                       # Dokumentasi repositori ini
