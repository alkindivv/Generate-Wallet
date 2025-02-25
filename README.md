# Generate Ethereum Wallet

Script sederhana untuk generate multiple Ethereum wallet secara otomatis dengan Node.js dan ethers.js.

## Fitur

- Generate multiple Ethereum wallet sekaligus
- Menyimpan informasi wallet dalam format JSON
- Informasi yang disimpan untuk setiap wallet:
  - Alamat wallet (address)
  - Private key
  - Seed phrase (mnemonic)
- Output disimpan ke file JSON dengan timestamp

## Persyaratan

- Node.js (versi 12 atau lebih baru)
- NPM (Node Package Manager)

## Instalasi

1. Clone repository ini:

```bash
git clone [URL_REPOSITORY_ANDA]
cd generate-wallet
```

2. Install dependensi yang diperlukan:

```bash
npm install
```

## Cara Penggunaan

1. Jalankan script dengan perintah:

```bash
node generateWallet.js
```

2. Masukkan jumlah wallet yang ingin di-generate ketika diminta

3. Script akan menghasilkan file JSON dengan format nama `wallets_[timestamp].json` yang berisi semua informasi wallet

## Format Output

File JSON yang dihasilkan akan memiliki format seperti ini:

```json
[
  {
    "index": 1,
    "address": "0x...",
    "privateKey": "0x...",
    "mnemonic": "word1 word2 ... word12"
  },
  ...
]
```

## Peringatan Keamanan

⚠️ **PENTING:**

- Jangan pernah membagikan private key atau mnemonic phrase Anda kepada siapapun
- Simpan backup dari file JSON yang dihasilkan di tempat yang aman
- Pastikan komputer Anda bebas dari malware sebelum generate wallet
- Script ini sebaiknya dijalankan di lingkungan yang aman dan terisolasi

## Dependensi

- [ethers.js](https://docs.ethers.org/v5/) - Library untuk berinteraksi dengan Ethereum
- [readline-sync](https://www.npmjs.com/package/readline-sync) - Library untuk input terminal

## Lisensi

MIT License

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau issue jika Anda memiliki saran perbaikan.
