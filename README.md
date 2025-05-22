# Opintosuoritusote (Python CLI-ohjelma)

Tämä on Pythonilla tehty komentorivipohjainen ohjelma, joka hallitsee opiskelijoiden kurssitietoja ja laskee opintosuorituksiin liittyviä tilastoja.

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

## 🖥️ Käyttö

Aja ohjelma komentorivillä:

```bash
python opintosuoritusote.py

Se avaa valikkopohjaisen käyttöliittymän:

--- Opintosuoritusote ---

1. Lisää uusi opiskelija tai kurssi
2. Näytä opiskelijan tiedot
3. Poista opiskelija
4. Poista kurssi
5. Poistu

💾 Tietojen rakenne (JSON)
Esimerkki yhdestä opiskelijasta:

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

🚀 Tulevat kehitysideat
- Graafinen käyttöliittymä (Tkinter)
- Kurssien muokkaus
- CSV- tai PDF-vientimahdollisuus

📄 Lisenssi
Tämä projekti on julkaistu avoimena opetus- ja harjoittelutarkoituksessa. Voit vapaasti käyttää, muokata ja jakaa.

Ron Gustafsson 22.5.2025

![Opintosuoritusote esimerkkikuva](ohjelman_toimintaa.png)
