# Event-Ticket-System
Capstone Module 1 Python CRUD

## List of Function
### Enter as Admin or Buyer
Pada sistem ini dapat memilih akun admin atau pembeli, kedua jenis akun memiliki opsi menu tersendiri

pada akun admin, User cukup memasukkan password admin

untuk akun pembeli, User dapat me-register akun untuk log-in pada sistem
register akan meminta
1. Nama
2. Password
3. Initial Balance
akun yang diregister tidak boleh menggunakan nama user yang sudah ada

### Menu Option
Untuk Admin:
1. Show Event Schedule --> Memperlihatkan seluruh data event
2. Add Event --> Menambahkan data event
3. Change Event Data --> Mengubah data event
4. Delete Event --> Menghapus event
5. Show Ticket --> Memperlihatkan seluruh tiket dari seluruh user pembeli
6. Logout Account --> Keluar dari akun untuk memilih akun lain
7. Exit System --> Mematikan sistem

Untuk Pembeli:
1. Show Event Schedule --> Memperlihatkan seluruh data event
2. Buy Event Ticket --> Membeli tiket event
3. Check Ticket --> Melihat tiket yang sudah dibeli dan fungsi lainnya (tertera di bawah)
4. Print Ticket --> Menampilkan print tiket yang sudah valid
5. Check Account --> Memperlihatkan data akun (nama & balance) serta untuk Top Up Balance
6. Logout Account --> Keluar dari akun untuk memilih akun lain
7. Exit System --> Mematikan sistem

### Event Ticket Code
Tiap event memiliki kode tersendiri yang unik dan tiap tiket juga memiliki kode unik tersendiri sehingga tidak ada 2 tiket yang sama

## Event and Ticket Status
Status pada Event dibagi menjadi 3 yaitu:
1. Avalailable
2. Unavailable
3. Sold Out

Opsi 1 tiket event dapat dibeli
Opsi 2 tidat dapat dibeli meski masih ada sisa jumlah kursi
Opsi 3 kursi pada event sudah terbeli semua

Status pada Tiket dibagi menjadi 4 yaitu:
1. In Cart
2. Pending Payment
3. Cancelled
4. Valid

Opsi 1 Tiket baru dipilih dan belum dibeli
Opsi 2 Tiket sudah dibeli tapi belum dibayar
  Biaya akhir tiket merupakan biaya tiket tertera pada event ditambah biaya admin sebesar 10%
Opsi 3 tiket dibatalkan
  Diberikan opsi untuk mendelete data tiket untuk tiket cancelled
Opsi 4 Tiket sudah dibayar dan valid untuk digunakan

## Check Ticket
Fungsi ini memilih tiket yang dimiliki oleh pembeli untuk melihat serta mengubah status ticket

1. In Cart:
  1. Opsi untuk mengubah ke Pending Payment
  2. Opsi untuk mengubah ke Cancelled
  3. Cukup melihat saja
2. Pending Payment:
  1. Opsi untuk mengubah ke Valid
  2. Opsi untuk mengubah ke Cancelled
  3. Cukup melihat saja
3. Cancelled:
  1. Notif tiket tidak dapat digunakan
  2. Opsi untuk menghapus data ticket
4. Valid:
   Notif tiket sudah dapat diprint untuk digunakan pada event

