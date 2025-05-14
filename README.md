# Failu Sakārtošanas Automatizācijas Projekts

Šis projekts ir paredzēts ikdienas failu sakārtošanas automatizēšanai, izmantojot Python. Programmatūra pārskata norādīto direktoriju un pārvieto failus uz kategoriju mapēm, balstoties uz to paplašinājumu (piemēram, dokumenti, attēli, video, audio u.c.).

## Projekta uzdevums

Automatizēt darbvirsmas vai lejupielāžu mapes saturu, pārskatot tajā esošos failus un pārvietojot tos uz atbilstošām kategoriju mapēm, tādējādi uzlabojot lietotāja darba vidi un failu pārskatāmību.

## Struktūra

Projekts sastāv no diviem Python failiem:

- `data_struckt.py` – definē datu struktūras `Fails` un `Failsisteme`
- `sorter.py` – galvenais izpildes fails, kas sakārto failus pēc paplašinājuma

## Datu struktūras

### Fails

![Fails klase](https://github.com/user-attachments/assets/07f096f4-40f0-4608-99b2-0b85a35fa71d)

Apraksta vienu failu ar tā nosaukumu, pilno ceļu un kategoriju.

### Failsisteme

![Failsisteme klase](https://github.com/user-attachments/assets/521b400b-b719-4bfb-b741-b04b832074de)

Glabā visus failus sadalītus kategorijās un piedāvā iespēju izvadīt kopsavilkumu.

## Sakārtošanas skripts

### Galvenās funkcijas:

- `noskaidrot_kategoriju(fails_nosaukums)` — nosaka faila kategoriju pēc paplašinājuma.
- `sakartot_mapes(cels)` — izveido `Failsisteme`, iziet cauri visiem failiem un pārvieto tos uz kategoriju mapēm.

### Papildu kategorijas:

Skripts atbalsta arī specializētus failu tipus:

- **matlab faili**: `.m`, `.mat`
- **python faili**: `.py`, `.ipynb`
- **web lapas**: `.html`, `.css`, `.js`

## Izmantotās bibliotēkas

### Sistēmas bibliotēkas

- `os` — darbam ar failu ceļiem un mapēm
- `shutil` — failu pārvietošanai uz citu mapi

### Strukturēšana un tipēšana

- `dataclasses` — klasēm, kas glabā tikai datus (`Fails`, `Failsisteme`)
- `typing` — tipiem: `List`, `Dict`

## Lietošana

1. Klonē vai lejupielādē projektu.
2. Atver komandrindu un palaid `sorter.py`:
   ```bash
   python sorter.py
3.Norādi ceļu uz mapi, kuru vēlies sakārtot.
4.Faili tiks pārvietoti uz kategoriju mapēm.
5.Pēc izpildes tiks izvadīts kopsavilkums.

## Piemers:
![image](https://github.com/user-attachments/assets/08076fed-85c5-4433-8f4d-54f06c26913c)

## Iespējamie uzlabojumi:
- Eksports uz .csv
- Iespēja dzēst tukšās mapes
- Lietotāja saskarne ar tkinter
- Automatizēta palaišana ar uzdevumu plānotāju (cron vai Task Scheduler)

