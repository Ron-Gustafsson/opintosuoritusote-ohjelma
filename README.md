# Study Record Management System (Python CLI Program)

This is a command-line based program written in Python that manages student course information and calculates statistics related to study performance.

---

## 🔧 Program Functions

- Add a student and their courses (YTO or Vocational)
- Prevent saving the same course twice
- Display selected student's:
  - Course lists
  - Number of courses and total OSP credits
  - Average grades
- Delete individual courses
- Delete a student with all their data
- Automatically save and load data from the opintosuoritusote.json file
---

## 🖥️ Usage

Run the program from the command line:

python opintosuoritusote.py

It opens a menu-based interface:

--- Study Transcript ---

1. Add a new student or course  
2. View student information  
3. Delete a student  
4. Delete a course  
5. Exit

---

## 💾 Data Structure (JSON)
Example of one student:
```json
"Ron Gustafsson": {
  "yto": [
    {
      "nimi": "Native Language: For Polytechnic Studies",
      "osp": 1,
      "arvosana": 5
    }
  ],
  "ammatillinen": [
    {
      "nimi": "Programming Basics",
      "osp": 5,
      "arvosana": 5
    }
  ]
}
```
---

## 🚀 Future Development Ideas
- Graphical user interface (Tkinter)
- Course editing
- CSV or PDF export option

---

## 📄 License
This project is published openly for educational and training purposes.
You are free to use, modify, and share it.

Ron Gustafsson, May 22, 2025

---

## Sama suomeksi...

# Opintosuoritusote (Python CLI-ohjelma)

Tämä on Pythonilla tehty komentorivipohjainen ohjelma, joka hallitsee opiskelijoiden kurssitietoja ja laskee opintosuorituksiin liittyviä tilastoja.

---

## 🔧 Ohjelman toiminnot

- Lisää opiskelija ja hänen kurssinsa (YTO tai ammatillinen)
- Estää saman kurssin tallentamisen kahdesti
- Näyttää valitun opiskelijan:
  - Kurssilistat
  - Kurssien määrät ja OSP-yhteismäärät
  - Keskiarvot
- Poistaa yksittäisiä kursseja
- Poistaa opiskelijan kaikkine tietoineen
- Tallentaa ja lataa tiedot `opintosuoritusote.json`-tiedostosta automaattisesti

---

## 🖥️ Käyttö

Aja ohjelma komentorivillä:

python opintosuoritusote.py

Se avaa valikkopohjaisen käyttöliittymän:

--- Opintosuoritusote ---

1. Lisää uusi opiskelija tai kurssi
2. Näytä opiskelijan tiedot
3. Poista opiskelija
4. Poista kurssi
5. Poistu

---

## 💾 Tietojen rakenne (JSON)
Esimerkki yhdestä opiskelijasta:
```json
"Ron Gustafsson": {
  "yto": [
    {
      "nimi": "Äidinkieli: AMK-opintoihin",
      "osp": 1,
      "arvosana": 5
    }
  ],
  "ammatillinen": [
    {
      "nimi": "Ohjelmoinnin perusteet",
      "osp": 5,
      "arvosana": 5
    }
  ]
}
```
---

## 🚀 Tulevat kehitysideat
- Graafinen käyttöliittymä (Tkinter)
- Kurssien muokkaus
- CSV- tai PDF-vientimahdollisuus

---

## 📄 Lisenssi
Tämä projekti on julkaistu avoimena opetus- ja harjoittelutarkoituksessa.
Voit vapaasti käyttää, muokata ja jakaa.

Ron Gustafsson, 22.5.2025

---
