import os # <--- Pastikan ini ada di bagian paling atas
import hashlib
import binascii
from ecdsa import SigningKey, SECP256k1 # pip install ecdsa

# 1. Base58 Encoding (Implementasi Sederhana - PERHATIKAN INI BUKAN Base58Check LENGKAP)
# Base58Check memerlukan perhitungan checksum, yang sudah dilakukan sebelumnya.
# Fungsi ini hanya mengonversi byte ke Base58.
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(data):
    # Mengonversi byte ke integer
    num = int.from_bytes(data, 'big') # Python 3.2+

    # Menghitung nol di awal
    leading_zeros = 0
    for byte in data:
        if byte == 0:
            leading_zeros += 1
        else:
            break

    output = ""
    while num > 0:
        num, remainder = divmod(num, 58)
        output = ALPHABET[remainder] + output

    return ALPHABET[0] * leading_zeros + output

# 2. Hashing SHA256 & RIPEMD160
def hash160(public_key_bytes):
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    return ripemd160_hash

# 3. Fungsi Utama untuk Membuat Alamat Bitcoin
def generate_bitcoin_address_manual():
    # A. Membuat Kunci Privat (256-bit angka acak)
    private_key_bytes = os.urandom(32)
    private_key_hex = binascii.hexlify(private_key_bytes).decode('utf-8')

    # B. Mendapatkan Kunci Publik (compressed) dari Kunci Privat (membutuhkan ecdsa)
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    vk = sk.get_verifying_key()

    # Public Key Compressed
    x_coord = vk.pubkey.point.x().to_bytes(32, 'big')
    # Y koordinat menentukan prefix (0x02 jika genap, 0x03 jika ganjil)
    prefix_byte = b'\x02' if vk.pubkey.point.y() % 2 == 0 else b'\x03'
    public_key_compressed_bytes = prefix_byte + x_coord

    # C. Hashing Kunci Publik (SHA256 lalu RIPEMD160)
    public_key_hash160 = hash160(public_key_compressed_bytes)

    # D. Menambahkan Version Byte (0x00 untuk Bitcoin Mainnet P2PKH)
    version_byte = b'\x00'
    versioned_payload = version_byte + public_key_hash160

    # E. Menghitung Checksum (Double SHA256 dari payload berversi)
    first_sha256 = hashlib.sha256(versioned_payload).digest()
    second_sha256 = hashlib.sha256(first_sha256).digest()
    checksum = second_sha256[:4] # Ambil 4 byte pertama

    # F. Menggabungkan Payload dan Checksum
    final_payload_for_base58 = versioned_payload + checksum

    # G. Mengodekan ke Base58Check
    bitcoin_address = base58_encode(final_payload_for_base58)

    # Mengkonversi private key bytes ke WIF (Wallet Import Format)
    # Ini juga melibatkan version byte (0x80 untuk mainnet) dan checksum Base58Check.
    # Ini adalah langkah yang sedikit berbeda dari alamat, tapi penting untuk kunci privat.
    wif_version_byte = b'\x80'
    private_key_wif_payload = wif_version_byte + private_key_bytes

    # Jika menggunakan compressed public key, tambahkan 0x01 byte di akhir private key
    private_key_wif_payload += b'\x01' # Indikasi bahwa ini adalah kunci untuk compressed public key

    wif_first_sha256 = hashlib.sha256(private_key_wif_payload).digest()
    wif_second_sha256 = hashlib.sha256(wif_first_sha256).digest()
    wif_checksum = wif_second_sha256[:4]

    private_key_wif_final = private_key_wif_payload + wif_checksum
    private_key_wif = base58_encode(private_key_wif_final)


    print(f"Kunci Privat Hex: {private_key_hex}")
    print(f"Kunci Privat (WIF): {private_key_wif}")
    print(f"Alamat Bitcoin (P2PKH): {bitcoin_address}")
    print("\n--- PERINGATAN KRITIS ---")
    print("Implementasi manual ini sangat kompleks dan rentan kesalahan.")
    print("JANGAN gunakan ini untuk Bitcoin asli. Hanya untuk tujuan edukasi.")
    print("Kesalahan kecil dapat menyebabkan kehilangan dana permanen.")

if __name__ == "__main__":
    generate_bitcoin_address_manual()
