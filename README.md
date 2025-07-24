# ₿ Generator Alamat Bitcoin Manual (Edukasi Saja!) ⚠️

Sebuah proyek Python yang mendemistifikasi proses pembuatan alamat Bitcoin P2PKH (Pay-to-Public Key Hash) dan kunci privat WIF (Wallet Import Format) secara langkah demi langkah. Ini adalah implementasi *manual* yang berfokus pada pemahaman konsep dasar kriptografi Bitcoin, BUKAN untuk penggunaan nyata!

---

## 🔗 Tujuan Projek Ini

* **Memahami Mekanisme Bitcoin**: Mengungkap lapisan demi lapisan bagaimana alamat Bitcoin P2PKH dihasilkan dari kunci privat.
* **Eksplorasi Kriptografi**: Menjelajahi penggunaan SHA256, RIPEMD160, dan kurva elips SECP256k1 dalam konteks Bitcoin.
* **Implementasi Protokol**: Membangun kembali bagian dari protokol Bitcoin secara manual untuk tujuan edukasi.
* **Peringatan Keamanan**: Menyoroti kompleksitas dan bahaya dalam mengimplementasikan kriptografi tingkat rendah tanpa keahlian khusus.

---

## 📦 Isi Kotak Proyek Ini

* **Generator Kunci Pasangan**: Fungsi untuk membuat kunci privat (acak) dan mendapatkan kunci publik terkompresi.
* **Hashing Ganda**: Implementasi SHA256 dan RIPEMD160 untuk proses hashing kunci publik.
* **Base58 Encoding**: Fungsi dasar untuk mengonversi data biner ke format Base58. (Catatan: Ini bukan Base58Check lengkap).
* **Perhitungan Checksum**: Metode untuk menambahkan checksum guna validasi alamat dan WIF.
* **Pembentukan Alamat & WIF**: Menggabungkan semua komponen untuk menghasilkan alamat Bitcoin P2PKH dan kunci privat WIF.

---

## ✨ Fitur-Fitur Utama

* **Pembuatan Kunci Privat**: Menghasilkan kunci privat acak (256-bit).
* **Kunci Publik Terkompresi**: Mendapatkan kunci publik dalam format terkompresi sesuai standar Bitcoin.
* **Hashing Standar Bitcoin**: Menerapkan hashing `SHA256` diikuti `RIPEMD160` pada kunci publik.
* **Version Byte**: Menambahkan *version byte* yang tepat untuk alamat Bitcoin Mainnet (`0x00`) dan kunci privat WIF (`0x80`).
* **Checksum Ganda SHA256**: Menghitung *checksum* untuk integritas data.
* **Base58 Encoding**: Mengodekan data biner akhir ke format Base58.
* **Output Lengkap**: Menampilkan Kunci Privat (Hex & WIF) dan Alamat Bitcoin (P2PKH).

---

## ⚠️ PERINGATAN KRITIS: HANYA UNTUK EDUKASI! ⚠️

**Kode ini adalah implementasi manual dan sederhana. JANGAN PERNAH MENGGUNAKAN KODE INI UNTUK MENGHASILKAN KUNCI ATAU ALAMAT BITCOIN ASLI YANG AKAN ANDA GUNAKAN DENGAN DANA NYATA.**

* **Keamanan**: Implementasi manual ini sangat rentan terhadap kesalahan manusia, *bug*, dan kerentanan keamanan yang dapat menyebabkan kehilangan dana permanen.
* **Kompleksitas**: Standar Bitcoin sangat kompleks. Ada banyak detail kecil yang harus diikuti dengan tepat untuk memastikan keamanan dan kompatibilitas.
* **Risiko**: Kesalahan kecil sekalipun (misalnya, salah *byte*, *checksum* yang tidak tepat) akan membuat alamat atau kunci tidak valid atau tidak dapat diakses.

**SELALU gunakan perpustakaan kriptografi yang telah teruji dan diaudit oleh para ahli jika Anda berinteraksi dengan mata uang kripto asli.**

---

## 🛠️ Apa Yang Kamu Butuhkan

### Persyaratan Software

* **Python 3.x**
* **Perpustakaan `ecdsa`**: Anda dapat menginstalnya menggunakan pip:
    ```bash
    pip install ecdsa
    ```

---

## 🚀 Langkah-Langkah Penggunaan

Ikuti langkah-langkah mudah ini untuk menjalankan dan memahami generator alamat Bitcoin manual ini:

### Langkah 1: Siapkan Lingkungan

1.  **Pastikan Python Terinstal**: Unduh dan instal Python 3.x jika Anda belum memilikinya dari [python.org](https://www.python.org/downloads/).
2.  **Instal Perpustakaan `ecdsa`**: Buka terminal atau Command Prompt Anda dan jalankan perintah ini:
    ```bash
    pip install ecdsa
    ```
3.  **Simpan Kode**: Simpan kode yang diberikan ke dalam sebuah file, misalnya `bitcoin_address_generator.py`.

### Langkah 2: Jalankan Aplikasi

Setelah semua persyaratan terpenuhi dan kode tersimpan, jalankan skrip dari terminal Anda:

```bash
python bitcoin_address_generator.py
```

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE). Bebas untuk digunakan, dimodifikasi, dan disebarluaskan untuk keperluan apa pun.

---

## 👋 Tertarik untuk Kolaborasi?

Kami sangat terbuka untuk kontribusi dan ide-ide baru! Jika Anda menemukan bug, memiliki saran fitur, atau ingin berkontribusi dalam bentuk kode, silakan:

* Buka **Issues** untuk melaporkan masalah atau mengusulkan ide.
* Buat **Pull Request** jika Anda sudah memiliki kode yang siap untuk digabungkan.

Mari bersama-sama ciptakan alat-alat yang lebih bermanfaat!

