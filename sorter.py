import os
import shutil
from data_struckt import Fails, Failsisteme

KATEGORIJAS = {
    "dokumentu": [".pdf", ".doc", ".docx", ".txt",],
    "attelu": [".jpg", ".jpeg", ".png", ".gif"],
    "video": [".mp4", ".avi", ".mov"],
    "audio": [".mp3", ".wav"],
    "programmu": [".exe", ".msi"],
    "saspiestie": [".zip", ".rar", ".7z"],
    "matlab faili": [".m", ".mat"],
    "python faili": [".py", ".ipynb"],
    "web lapas": [".html", ".css", ".js"],

}

def noskaidrot_kategoriju(fails_nosaukums):
    _, ext = os.path.splitext(fails_nosaukums.lower())
    for kategorija, paplasinajumi in KATEGORIJAS.items():
        if ext in paplasinajumi:
            return kategorija
    return "cits"

def sakartot_mapes(cels: str):
    sistema = Failsisteme()

    for nosaukums in os.listdir(cels):
        pilns_cels = os.path.join(cels, nosaukums)
        if os.path.isfile(pilns_cels):
            kategorija = noskaidrot_kategoriju(nosaukums)
            fails = Fails(nosaukums, pilns_cels, kategorija)
            sistema.pievienot(fails)

            kategorijas_mape = os.path.join(cels, kategorija)
            os.makedirs(kategorijas_mape, exist_ok=True)
            jauns_cels = os.path.join(kategorijas_mape, nosaukums)
            shutil.move(pilns_cels, jauns_cels)

    return sistema

if __name__ == "__main__":
    direktorija = input("Ievadi ceļu uz mapi, kuru sakārtot: ")
    if not os.path.isdir(direktorija):
        print("Norādītā mape neeksistē.")
    else:
        struktura = sakartot_mapes(direktorija)
        print("\nSakārtoti faili pēc kategorijām:")
        struktura.paradit_kopsavilkumu()
