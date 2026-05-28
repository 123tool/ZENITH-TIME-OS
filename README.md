## ZENITH TIME OS TERMINAL

## Deskripsi
**ZENITH TIME OS** adalah *enterprise-grade terminal time management suite*. Aplikasi ini dirancang untuk memberikan kendali waktu yang presisi langsung melalui antarmuka terminal. Dengan fitur *adaptive UI* yang responsif terhadap ukuran layar, aplikasi ini berjalan sempurna baik di desktop (Linux/Windows/macOS) maupun perangkat mobile melalui Termux.

## Fitur
- **Adaptive Terminal UI:** Tampilan yang menyesuaikan otomatis dengan lebar terminal Anda.
- **Cross-Platform:** Mendukung ekosistem Linux (Xubuntu, dll), Windows, macOS, dan Termux.
- **Background Scheduler:** Sistem alarm berbasis *threading* yang tidak mengganggu alur kerja utama.
- **Persistence Data:** Menyimpan log stopwatch dan jadwal alarm secara aman di SQLite.
- **High-Visibility Clock:** Jam digital ASCII yang estetik dan mudah dibaca.
- **Lightweight & Modular:** Arsitektur kode yang bersih (clean code) untuk performa maksimal.

## Cara Install

## 1. Persiapan
Pastikan Python 3.8 atau versi terbaru sudah terinstal di sistem Anda.

## 2. Clone Repository
```bash
git clone https://github.com/123tool/ZENITH-TIME-OS.git
cd ZENITH-TIME-OS
```
## 3. Install Dependensi
​Gunakan pip untuk menginstal library yang diperlukan :
```
pip install -r requirements.txt
```
## 4. Run
​Jalankan aplikasi melalui terminal dengan perintah :
```
python3 main.py
```
*Catatan untuk pengguna Linux/Xubuntu :* `Jika keyboard listener tidak terdeteksi, pastikan memiliki akses grup input atau jalankan dengan sudo python3 main.py.`

## Troubleshooting
- ​Audio Alarm Tidak Bunyi : Sistem menggunakan beep standar terminal. Pastikan volume sistem Anda tidak dalam kondisi mute.
- ​UI Berantakan : Jika ukuran layar terminal terlalu kecil, beberapa elemen mungkin terpotong. Disarankan untuk menggunakan terminal dengan lebar minimal 80 karakter.
- ​Termux : Pastikan telah mengizinkan akses penyimpanan jika ingin menyimpan database secara permanen.
