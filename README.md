```markdown
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

```

> **⚠️ Catatan Dataset:** Karena keterbatasan ukuran file di GitHub, Anda harus mengunduh *dataset* `im_instagram_70k` secara mandiri melalui [Kaggle](https://www.google.com/search?q=https://www.kaggle.com/datasets/krisnarp/instagram-network-dataset) dan meletakkannya di dalam folder `data/`.

---

## 🚀 Cara Instalasi dan Penggunaan

**1. Clone Repositori**
Buka terminal/CMD Anda dan jalankan perintah berikut:

```bash
git clone [https://github.com/Eruumaa/Aplikasi-Struktur-Graf-Dalam-Menganalisis-Sistem-Pengikut-Instagram-dan-Rekomendasi-Akun---Diskrit.git](https://github.com/Eruumaa/Aplikasi-Struktur-Graf-Dalam-Menganalisis-Sistem-Pengikut-Instagram-dan-Rekomendasi-Akun---Diskrit.git)
cd Aplikasi-Struktur-Graf-Dalam-Menganalisis-Sistem-Pengikut-Instagram-dan-Rekomendasi-Akun---Diskrit

```

**2. Instalasi Dependensi (Libraries)**
Pastikan Anda sudah menginstal Python (minimal versi 3.8). Instal semua pustaka yang dibutuhkan dengan perintah:

```bash
pip install pandas networkx python-louvain matplotlib seaborn

```

**3. Jalankan Program**
Eksekusi file Python utama:

```bash
python main.py

```

*(Catatan: Proses kalkulasi Betweenness Centrality mungkin memakan waktu 10-30 detik tergantung spesifikasi CPU Anda. Harap tunggu hingga output muncul di terminal).*

---

## 📈 Output yang Dihasilkan

Ketika program dijalankan, sistem akan mencetak secara otomatis di terminal:

* Ringkasan graf (Jumlah Simpul dan Sisi).
* Tabel Top 5 Akun untuk *In-Degree*, *Betweenness*, dan *Closeness Centrality*.
* Jumlah komunitas makro yang terdeteksi.
* Kepadatan Jaringan (*Network Density*) dan Rata-rata Panjang Lintasan (*Average Path Length*).
* Top 5 Hasil Rekomendasi Akun untuk di-*follow* oleh entitas target.

Setelah output terminal selesai, sebuah jendela (*window*) **Matplotlib** akan terbuka secara otomatis menampilkan **Visualisasi Sub-Graf** dengan pewarnaan simpul berdasarkan sirkel komunitasnya.

---

## 🎓 Apresiasi dan Referensi

Penelitian dan kode ini dikembangkan murni untuk keperluan akademis. Kami mengucapkan terima kasih kepada Bapak Nazaruddin, S.Si., M.Eng.Sc., selaku Dosen Pengampu mata kuliah Struktur Diskrit USK.

Metode evaluasi dalam kode ini merujuk pada buku *Discrete Mathematics and Its Applications* dan referensi standar IEEE terkini mengenai *Social Network Analysis*.

```
