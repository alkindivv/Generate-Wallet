const { ethers } = require("ethers");
const readlineSync = require("readline-sync");
const fs = require("fs");

async function generateWallets() {
  // Meminta input jumlah wallet yang akan digenerate
  const jumlahWallet = parseInt(
    readlineSync.question("Masukkan jumlah wallet yang ingin digenerate: ")
  );

  if (isNaN(jumlahWallet) || jumlahWallet <= 0) {
    console.log("Mohon masukkan angka yang valid dan lebih besar dari 0");
    return;
  }

  const wallets = [];

  console.log(`\nMemulai generate ${jumlahWallet} wallet...\n`);

  for (let i = 0; i < jumlahWallet; i++) {
    // Generate wallet baru
    const wallet = ethers.Wallet.createRandom();

    // Menyimpan informasi wallet
    const walletInfo = {
      index: i + 1,
      address: wallet.address,
      privateKey: wallet.privateKey,
      mnemonic: wallet.mnemonic.phrase,
    };

    wallets.push(walletInfo);

    console.log(`Wallet #${i + 1} berhasil digenerate`);
  }

  // Menyimpan ke file JSON
  const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
  const fileName = `wallets_${timestamp}.json`;

  fs.writeFileSync(fileName, JSON.stringify(wallets, null, 2));
  console.log(`\nBerhasil generate ${jumlahWallet} wallet!`);
  console.log(`Data wallet telah disimpan ke file: ${fileName}`);
}

// Menjalankan fungsi
generateWallets().catch(console.error);
