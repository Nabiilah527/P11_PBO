from abc import ABC, abstractmethod

class Mahasiswa:
    def __init__(self, nama, sks, prasyarat_lengkap):
        self.nama = nama
        self.sks = sks
        self.prasyarat_lengkap = prasyarat_lengkap

# --- IMPLEMENTASI SOLID ---

# 1. Kontrak Abstraksi (DIP) 
class IValidationRule(ABC):
    """Kontrak untuk semua aturan validasi mahasiswa."""
    @abstractmethod
    def validate(self, mhs: Mahasiswa) -> bool:
        """Method abstrak untuk memvalidasi data mahasiswa."""
        pass

# 2. Implementasi SRP 
class SKSValidator(IValidationRule):
    """Aturan untuk memvalidasi batas maksimal SKS."""
    def validate(self, mhs: Mahasiswa) -> bool:
        """Memeriksa apakah jumlah SKS tidak melebihi batas 24 SKS.

        Args:
            reg (Registrasi): Objek data registrasi.

        Returns:
            bool: True jika valid, False jika melanggar.
        """
        if mhs.sks <= 24:
            return True
        print(f"Log: SKS {mhs.sks} melampaui batas.")
        return False

class PrerequisiteValidator(IValidationRule):
    def validate(self, mhs: Mahasiswa) -> bool:
        if mhs.prasyarat_lengkap:
            return True
        print("Log: Prasyarat belum lengkap.")
        return False

# 3. Koordinator yang fleksibel (OCP & Dependency Injection) 
class RegistrationService:
    """Service untuk mengelola alur registrasi mahasiswa menggunakan prinsip SOLID."""
    def __init__(self, rules: list):
        self.rules = rules 

    def run(self, mhs: Mahasiswa):
        print(f"--- Memproses Registrasi: {mhs.nama} ---")
        success = True
        for rule in self.rules:
            if not rule.validate(mhs):
                success = False
        
        if success:
            print("Status: Registrasi Diterima!")
        else:
            print("Status: Registrasi Ditolak!")

# Simulasi Eksekusi
if __name__ == "__main__":
    mhs_budi = Mahasiswa("Budi", 20, True)
    
    aturan = [SKSValidator(), PrerequisiteValidator()]
    
    app = RegistrationService(aturan)
    app.run(mhs_budi)