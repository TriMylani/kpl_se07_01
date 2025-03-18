from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis Kelamin harusnya adalah PRIA atau WANITA")
    patients.append({"name": name, "gender": gender.name})  
    # gender.name = menampilkan PRIA/WANITA; gender.value = menampilkan angka; gender = menampilkan JenisKelamin.PRIA/WANITA

add_patient("Andi", JenisKelamin.PRIA)
add_patient("Siti", JenisKelamin.WANITA)

for patient in patients:
    print(f"{patient['name']} adalah {patient['gender']}")