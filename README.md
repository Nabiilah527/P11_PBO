# Tugas Praktikum PBO - Refactoring SOLID Principle

Repositori ini dibuat untuk memenuhi tugas mata kuliah Pemrograman Berorientasi Objek (Pertemuan 11).

## Identifikasi Pelanggaran Prinsip Desain (Code Smell)

Pada kode sebelum refactoring (`registrasi_sebelum.py`), ditemukan beberapa pelanggaran prinsip desain:

1. **Single Responsibility Principle (SRP)**: Kelas `ValidatorManager` memiliki lebih dari satu alasan untuk berubah karena menangani logika validasi SKS sekaligus validasi prasyarat dalam satu metode tunggal.
2. **Open/Closed Principle (OCP)**: Kode bersifat kaku. Jika terdapat aturan validasi baru (misalnya validasi keuangan), kita harus memodifikasi kelas yang sudah ada, bukan menambahkannya melalui ekstensi.
3. **Dependency Inversion Principle (DIP)**: Logika bisnis bergantung langsung pada implementasi konkrit yang kaku (hardcoded), bukan pada sebuah abstraksi atau kontrak.

## Hasil Refactoring

Setelah proses refactoring (`registrasi_sesudah.py`), struktur kode telah diperbaiki dengan:
- **Abstraksi**: Menggunakan `Abstract Base Class` (ABC) sebagai kontrak untuk semua aturan validasi.
- **Modularitas**: Memecah tanggung jawab ke kelas-kelas kecil (`SKSValidator`, `PrerequisiteValidator`) yang masing-masing hanya memiliki satu tanggung jawab (SRP).
- **Dependency Injection**: Menggunakan *constructor injection* pada `RegistrationService` sehingga kelas tersebut bergantung pada abstraksi, bukan implementasi konkrit.
