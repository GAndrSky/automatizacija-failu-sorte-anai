Failu Sakārtošanas Automatizācijas Projekts
Šis projekts ir paredzēts ikdienas failu sakārtošanas automatizēšanai, izmantojot Python. Programmatūra pārskata norādīto direktoriju un pārvieto failus uz kategoriju mapēm, balstoties uz to paplašinājumu (piemēram, dokumenti, attēli, video, audio u.c.).

Projekta uzdevums
Automatizēt darbvirsmas vai lejupielāžu mapes saturu, pārskatot tajā esošos failus un pārvietojot tos uz atbilstošām kategoriju mapēm, tādējādi uzlabojot lietotāja darba vidi un failu pārskatāmību.

Datu struktūras
Fails
class Fails:
    nosaukums: str
    cels: str
    kategorija: str
Failsisteme
class Failsisteme:
    kategorijas: Dict[str, List[Fails]]
    def pievienot(self, fails: Fails): ...
    def paradit_kopsavilkumu(self): ...
Izmantotās Python bibliotēkas
os — darbam ar failu sistēmu

shutil — failu pārvietošanai

dataclasses — strukturēto objektu definēšanai

Lietošana
Klonē vai lejupielādē projektu.

Palaid skriptu scraper.py (kas ir sakārtošanas skripts).

Norādi ceļu uz sakārtojamo mapi (piemēram, C:\Users\Lietotajs\Downloads).

Programma pārvietos failus uz kategorijām atbilstošām mapēm.

Pēc izpildes tiek izvadīts kopsavilkums par paveikto:

DOKUMENTU: 3 faili
  - fails1.pdf
  - fails2.docx
  - teksts.txt
ATTĒLU: 2 faili
  - bilde.jpg
  - zime.png
Kategorijas
Faili tiek sadalīti šādās kategorijās:

dokumentu: .pdf, .docx, .txt utt.

attelu: .jpg, .png, .gif utt.

video: .mp4, .avi utt.

audio: .mp3, .wav utt.

saspiestie: .zip, .rar utt.

programmu: .exe, .msi utt.

cits: ja nav sakritības ar kategorijām

Iespējamie uzlabojumi
Eksports uz .csv

Iespēja dzēst tukšās mapes pēc sakārtošanas

Lietotāja saskarne ar tkinter

Automātiska izpilde ar Windows uzdevumu plānotāju vai cron Linux vidē