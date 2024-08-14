# Skrip Daily Assisterr.ai

Skrip ini mengotomatiskan klaim poin harian Assisterr.ai menggunakan token otentikasi yang disediakan. Skrip ini mendukung beberapa akun dan menampilkan detail akun dalam format yang menarik dan berwarna.

## Fitur

- Mengklaim poin harian secara otomatis dari Assisterr.ai.
- Mendukung banyak akun

## Persyaratan

Sebelum menjalankan skrip, pastikan Anda telah menginstal yang berikut:

- **Python 3.x**
- **pip** (pengelola paket Python)

### Paket Python

Instal paket Python yang diperlukan dengan perintah berikut:

```bash
pip install requests termcolor
```

## Cara Penggunaan

1. **Clone repositori ini**:

   ```bash
   git clone https://github.com/Semutireng22/assister.git
   cd assister
   ```

2. **Siapkan file `auth.txt`**:

   - Buat file bernama `auth.txt` di direktori yang sama dengan skrip.
   - Tambahkan token otentikasi Anda, satu token per baris. Setiap token mewakili akun yang berbeda.

   Contoh isi `auth.txt`:

   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ8...
   ```

3. **Jalankan skrip**:

   ```bash
   python3 main.py
   ```

   Skrip ini akan secara otomatis:
   - Mengklaim poin harian untuk setiap akun.
   - Mengambil dan menampilkan detail akun dalam format yang menarik.

## Cara Mengambil Token Otentikasi

Untuk mengambil `auth` dari cookies di browser:

1. **Buka Developer Tools**:
   - Tekan `F12` atau `Ctrl + Shift + I` di Windows/Linux, atau `Cmd + Option + I` di macOS.
   - Buka tab **Console**.

2. **Jalankan skrip berikut di console**:

   ```javascript
   let cookies = document.cookie.split('; ');
   let refreshToken = cookies.find(cookie => cookie.startsWith('refreshToken=')).split('=')[1];
   prompt('UGD AIRDROP:', refreshToken);
   ```

   - Sebuah prompt akan muncul dengan `auth`. Salin token tersebut dan tempelkan ke file `auth.txt`.

## Catatan

- Pastikan Anda memperbarui file `auth.txt` dengan token yang valid secara berkala agar otomasi tetap berfungsi.
- Skrip akan berhenti selama 24 jam setelah setiap kali dijalankan, menunggu untuk mengklaim poin harian berikutnya. Jika ingin bekerja selama 24 jam maka jalankan di dalam screen

## Lisensi

Proyek ini dilisensikan di bawah Lisensi Apache - lihat file [LICENSE](LICENSE) untuk detailnya.
