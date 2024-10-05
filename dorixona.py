class dorixona:
    def __init__(self, dori_nomi, narx, ishlab_chiqarilgan_joyi, muddat):
        self.dori_nomi = dori_nomi
        self.narx = narx
        self.ishlab_chiqarilgan_joyi = ishlab_chiqarilgan_joyi
        self.muddat = muddat
    
    def info(self):
        print(f"Nomi: {self.dori_nomi}, Narxi: {self.narx} so'm, Ishlab chiqarilgan joyi: {self.ishlab_chiqarilgan_joyi}, Muddati: {self.muddat}")

tomoq_ogrigi_uchun = [
    {
        "nomi": "Ingalip sprey",
        "muddati": "2025-12",
        "narxi": 12000,
        "ishlab_chiqarilgan_joyi": "Rossiya"
    },
    {
        "nomi": "Gultse kukun",
        "muddati": "2024-09",
        "narxi": 20500,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    },
    {
        "nomi": "Bisepptol tabletkalar",
        "muddati": "2024-11",
        "narxi": 6000,
        "ishlab_chiqarilgan_joyi": "Polsha"
    },
    {
        "nomi": "Iitsin eritma",
        "muddati": "2026-03",
        "narxi": 36000,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    },
    {
        "nomi": "Sadjisept pastilkalar",
        "muddati": "2025-05",
        "narxi": 19000,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    }
]

bosh_ogrigi_uchun = [
    {
        "nomi": "Pentalgin",
        "muddati": "2024-12",
        "narxi": 33000,
        "ishlab_chiqarilgan_joyi": "Uzbekistan"
    },
    {
        "nomi": "Sitramon",
        "muddati": "2025-01",
        "narxi": 5000,
        "ishlab_chiqarilgan_joyi": "Gruziya"
    },
    {
        "nomi": "Brufen",
        "muddati": "2026-06",
        "narxi": 62000,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    },
    {
        "nomi": "Analgin",
        "muddati": "2025-12",
        "narxi": 2800,
        "ishlab_chiqarilgan_joyi": "Uzbekistan"
    },
    {
        "nomi": "Tempalgin",
        "muddati": "2024-10",
        "narxi":24000,
        "ishlab_chiqarilgan_joyi": "Rossiya"
    }
]

isitma_uchun= [
    {
        "nomi": "Nurofen",
        "muddati": "2024-09",
        "narxi": 40000,
        "ishlab_chiqarilgan_joyi": "AQSh"
    },
    {
        "nomi": "Parasetamol",
        "muddati": "2025-03",
        "narxi": 3200,
        "ishlab_chiqarilgan_joyi": "Uzbekistan"
    },
    {
        "nomi": "Bolnol",
        "muddati": "2026-01",
        "narxi": 5200,
        "ishlab_chiqarilgan_joyi": "Uzbekistan"
    },
    {
        "nomi": "Sefekon",
        "muddati": "2023-11",
        "narxi": 130000,
        "ishlab_chiqarilgan_joyi": "Buyuk Britaniya"
    },
    {
        "nomi": "Ibuklin",
        "muddati": "2025-05",
        "narxi": 89000,
        "ishlab_chiqarilgan_joyi": "AQSh"
    }
]

bogim_ogrigi_uchun = [
    {
        "nomi": "Fastungel",
        "muddati": "2024-10",
        "narxi": 90000,
        "ishlab_chiqarilgan_joyi": "Shveytsariya"
    },
    {
        "nomi": "Inforin",
        "muddati": "2025-06",
        "narxi": 66000,
        "ishlab_chiqarilgan_joyi": "Xitoy"
    },
    {
        "nomi": "Dolgitgel",
        "muddati": "2026-02",
        "narxi": 100000,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    },
    {
        "nomi": "Sertofengel",
        "muddati": "2024-12",
        "narxi": 55000,
        "ishlab_chiqarilgan_joyi": "Italiya"
    },
    {
        "nomi": "Dikloseyfgel",
        "muddati": "2025-08",
        "narxi": 55400,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    }
]

umumiy = [
    {
        "nomi": "Paracetamol",
        "muddati": "2025-12",
        "narxi": 12000,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    },
    {
        "nomi": "Ibuprofen",
        "muddati": "2025-09",
        "narxi": 8000,
        "ishlab_chiqarilgan_joyi": "Uzbekistan"
    },
    {
        "nomi": "Amoksitsilin",
        "muddati": "2026-03",
        "narxi": 6000,
        "ishlab_chiqarilgan_joyi": "Xitoy"
    },
    {
        "nomi": "Fastungel",
        "muddati": "2024-10",
        "narxi": 90000,
        "ishlab_chiqarilgan_joyi": "Shveytsariya"
    },
    {
        "nomi": "Tamsulosin",
        "muddati": "2025-04",
        "narxi": 17000,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    },
    {
        "nomi": "Etoricoxib",
        "muddati": "2026-02",
        "narxi": 95000,
        "ishlab_chiqarilgan_joyi": "Buyuk Britaniya"
    },
    {
        "nomi": "Azelastin",
        "muddati": "2025-11",
        "narxi": 45000,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    },
    {
        "nomi": "Clonazepam",
        "muddati": "2025-03",
        "narxi": 28000,
        "ishlab_chiqarilgan_joyi": "Fransiya"
    },
    {
        "nomi": "Fluoksetin",
        "muddati": "2024-10",
        "narxi": 22000,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    },
    {
        "nomi": "Metoprolol",
        "muddati": "2024-12",
        "narxi": 18000,
        "ishlab_chiqarilgan_joyi": "Rossiya"
    },
    {
        "nomi": "Simvastatin",
        "muddati": "2025-06",
        "narxi": 36000,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    },
    {
        "nomi": "Cetirizine",
        "muddati": "2025-01",
        "narxi": 15000,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    },
    {
        "nomi": "Montelukast",
        "muddati": "2024-09",
        "narxi": 30000,
        "ishlab_chiqarilgan_joyi": "Hindiston"
    },
    {
        "nomi": "Dexamethasone",
        "muddati": "2025-05",
        "narxi": 5000,
        "ishlab_chiqarilgan_joyi": "Xitoy"
    },
    {
        "nomi": "Furosemide",
        "muddati": "2024-11",
        "narxi": 9000,
        "ishlab_chiqarilgan_joyi": "Germaniya"
    },
    {
        "nomi": "Omeprazole",
        "muddati": "2026-01",
        "narxi": 12000,
        "ishlab_chiqarilgan_joyi": "Rossiya"
    }
]

def dori_qidiruv(dori_royxati, dori_nomi):
    for dori in dori_royxati:
        if dori["nomi"].lower() == dori_nomi.lower():
            d = dorixona(dori["nomi"], dori["narxi"], dori["ishlab_chiqarilgan_joyi"], dori["muddati"])
            d.info()
            return True
    return False

def dori_royxatini_chiqar(dori_royxati):
    print("Bizda bor dorilar:")
    for dori in dori_royxati:
        print(f"- {dori['nomi']}")

while True:
    print("isitma uchun\nbosh ogrigi uchun\nbogim ogrigi uchun\ntomoq ogrigi uchun\numumiy")
    tanlov = input("Qanday dori kerak: ").lower()

    if tanlov == "isitma uchun":
        dori_royxatini_chiqar(isitma_uchun)
        dori_nomi = input("Dori nomini kiriting: ").capitalize()
        topildi = dori_qidiruv(isitma_uchun, dori_nomi)
    elif tanlov == "bosh ogrigi uchun":
        dori_royxatini_chiqar(bosh_ogrigi_uchun)
        dori_nomi = input("Dori nomini kiriting: ").capitalize()
        topildi = dori_qidiruv(bosh_ogrigi_uchun, dori_nomi)
    elif tanlov == "bogim ogrigi uchun":
        dori_royxatini_chiqar(bogim_ogrigi_uchun)
        dori_nomi = input("Dori nomini kiriting: ").capitalize()
        topildi = dori_qidiruv(bogim_ogrigi_uchun, dori_nomi)
    elif tanlov == "tomoq ogrigi uchun":
        dori_royxatini_chiqar(tomoq_ogrigi_uchun)
        dori_nomi = input("Dori nomini kiriting: ").capitalize()
        topildi = dori_qidiruv(tomoq_ogrigi_uchun, dori_nomi)
    elif tanlov == "umumiy":
        dori_royxatini_chiqar(umumiy)
        dori_nomi = input("Dori nomini kiriting: ").capitalize()
        topildi = dori_qidiruv(umumiy, dori_nomi)
    else:
        print("Noto'g'ri tanlov!")
        continue

    if not topildi:
    
        print("Afsus, bunday dori mavjud emas.")

    yana = input("Yana dori kerakmi? (ha/yo'q): ").lower()
    if yana != "ha":
        break