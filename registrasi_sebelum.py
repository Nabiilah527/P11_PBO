# === KODE BURUK (SEBELUM REFACTORING) ===

class ValidatorManager:
    def validate_registration(self, nama, sks, prasyarat_lengkap):
        print(f"Memulai validasi untuk {nama}...")

        if sks > 24:
            print("Gagal: SKS tidak boleh lebih dari 24!")
            return False
        
        if not prasyarat_lengkap:
            print("Gagal: Mata kuliah prasyarat belum terpenuhi!")
            return False
        
        print("Registrasi Berhasil!")
        return True

if __name__ == "__main__":
    validator = ValidatorManager()
    validator.validate_registration("Budi", 26, False)