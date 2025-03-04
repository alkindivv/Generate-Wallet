# Ethereum Wallet Generator

Kumpulan script untuk generate dan mengelola Ethereum wallet.

## Fitur

- Generate wallet Ethereum (alamat, private key, seed phrase)
- Generate vanity address dengan pola tertentu
- Generate random amount untuk daftar alamat
- Menyimpan data wallet dalam format JSON

## Persyaratan

### Untuk Script Python

```bash
pip install -r requirements.txt
```

### Untuk Script Node.js

```bash
npm install
```

## Penggunaan

### Generate Wallet (Node.js)

```bash
npm start
# atau
node generateWallet.js
```

### Generate Vanity Address (Python)

```bash
python3 generate_vanity_wallet.py
```

### Generate Random Amounts (Python)

```bash
python3 generate_random_amounts.py
```

## Keamanan

- Simpan private key dan seed phrase dengan aman
- Jangan bagikan informasi wallet kepada siapapun
- Gunakan komputer yang aman saat menjalankan script
- Backup data wallet secara offline

## Catatan

- Script vanity address membutuhkan waktu untuk menemukan alamat yang sesuai
- CPU usage bisa tinggi saat mencari vanity address
- Data wallet disimpan dalam format JSON dengan timestamp

## Dependensi

- [ethers.js](https://docs.ethers.org/v5/) - Library untuk berinteraksi dengan Ethereum
- [readline-sync](https://www.npmjs.com/package/readline-sync) - Library untuk input terminal

## Lisensi

MIT License

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau issue jika Anda memiliki saran perbaikan.
