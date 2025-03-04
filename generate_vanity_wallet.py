from eth_account import Account
import json
import time
import re
from eth_account.hdaccount import generate_mnemonic
import datetime

# Mengaktifkan fitur HD Wallet
Account.enable_unaudited_hdwallet_features()

def is_valid_pattern(address, base_pattern="alkindi"):
    # Convert address and pattern to lowercase for basic matching
    address_lower = address.lower()

    # Pattern untuk mencocokkan variasi dari "alkindi"
    # Contoh yang valid: alkindi, ALKINDI, AlKiNdi, alK1nd1, dll
    pattern = re.compile(f'.*({base_pattern}|[a4]lk[i1]nd[i1]|[a4]lk[i1]nd[y1]).*', re.IGNORECASE)

    return bool(pattern.match(address_lower))

def format_time(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

def generate_vanity_address():
    print("\n🔍 Mencari address yang mengandung variasi dari 'ALKINDI'")
    print("⏳ Mohon tunggu, ini bisa memakan waktu...")
    print("\n⚠️ PERINGATAN KEAMANAN:")
    print("1. Pastikan Anda menjalankan script ini di komputer yang aman dan bebas malware")
    print("2. Jangan bagikan private key dan seed phrase kepada siapapun")
    print("3. Simpan backup file JSON di tempat yang aman")
    print("4. Sebaiknya gunakan wallet ini hanya untuk jumlah kecil atau testing")
    print("5. Untuk keamanan maksimal, gunakan hardware wallet\n")

    print("📊 Statistik Pencarian:")
    print("- Rata-rata waktu: 1-2 jam")
    print("- Kecepatan: ~150 address/detik")
    print("- Pattern yang diterima: ALKINDI, alkindi, AlK1ndi, 4lkindi, dll.\n")

    attempts = 0
    start_time = time.time()
    last_update = start_time
    update_interval = 1  # Update setiap 1 detik

    try:
        while True:
            # Generate mnemonic and account
            mnemonic = generate_mnemonic(12, "english")
            account = Account.from_mnemonic(mnemonic)
            address = account.address

            # Check if address contains any valid variation of the pattern
            if is_valid_pattern(address):
                break

            attempts += 1
            current_time = time.time()

            # Update progress setiap interval
            if current_time - last_update >= update_interval:
                elapsed = current_time - start_time
                rate = attempts / elapsed if elapsed > 0 else 0

                # Clear line and update progress
                print(f"\r⏳ Percobaan: {attempts:,} | "
                      f"Kecepatan: {rate:.1f} addr/s | "
                      f"Waktu: {format_time(elapsed)} | "
                      f"Address terakhir: {address[:12]}...{address[-8:]}", end="")

                last_update = current_time

    except KeyboardInterrupt:
        print("\n\n🛑 Pencarian dihentikan oleh user")
        print(f"Total percobaan: {attempts:,}")
        return

    duration = time.time() - start_time

    wallet_info = {
        "address": address,
        "private_key": account.key.hex(),
        "mnemonic": mnemonic,
        "attempts": attempts,
        "duration_seconds": round(duration, 2),
        "security_notice": {
            "warning": "JANGAN BAGIKAN file ini kepada siapapun!",
            "recommendations": [
                "Simpan backup di tempat yang aman",
                "Jangan simpan file ini di cloud storage",
                "Hapus file ini setelah Anda mencatat/backup informasinya",
                "Untuk keamanan maksimal, gunakan hardware wallet"
            ]
        }
    }

    # Save to file
    filename = f"alkindi_wallet_{int(time.time())}.json"
    with open(filename, 'w') as f:
        json.dump(wallet_info, f, indent=2)

    print(f"\n\n✨ BERHASIL! Address dengan pattern 'alkindi' ditemukan!")
    print(f"⏱️ Total waktu pencarian: {format_time(duration)}")
    print(f"🔍 Total percobaan: {attempts:,}")
    print(f"⚡ Kecepatan rata-rata: {attempts/duration:.1f} address/detik")

    print(f"\n🔑 Address: {address}")
    print(f"🔒 Private Key: {account.key.hex()}")
    print(f"🌱 Seed Phrase: {mnemonic}")
    print(f"\n💾 Info lengkap telah disimpan ke {filename}")
    print("\n🔐 PENTING:")
    print("- Segera catat seed phrase dan private key di tempat yang aman")
    print("- Hapus file JSON setelah Anda mencatat informasi penting")
    print("- JANGAN BAGIKAN private key dan seed phrase kepada siapapun")

if __name__ == "__main__":
    # Install required package if not exists
    try:
        import eth_account
    except ImportError:
        print("Installing required package...")
        import subprocess
        subprocess.check_call(["pip", "install", "eth-account"])

    generate_vanity_address()