import json
import os

# Tiedostonimi, johon opiskelijoiden tiedot tallennetaan
TIEDOSTO = "opintosuoritusote.json"

# Kurssi-luokka kuvaa yksittäistä kurssia
class Kurssi:
    def __init__(self, nimi, osp, arvosana):
        self.nimi = nimi
        self.osp = osp
        self.arvosana = arvosana

    # Muuntaa kurssin sanakirjaksi JSON-tallennusta varten
    def to_dict(self):
        return {
            "nimi": self.nimi,
            "osp": self.osp,
            "arvosana": self.arvosana
        }

# Opiskelija-luokka sisältää YTO- ja ammatilliset kurssit
class Opiskelija:
    def __init__(self, nimi):
        self.nimi = nimi
        self.yto = []              # Lista YTO-kursseista
        self.ammatilliset = []    # Lista ammatillisista kursseista

    # Lisää kurssi oikeaan kategoriaan (YTO tai ammatillinen)
    def lisaa_kurssi(self, kurssi, tyyppi):
        lista = self.yto if tyyppi == "yto" else self.ammatilliset
        # Tarkistetaan, ettei samaa kurssia lisätä kahdesti (nimi vertailu pienillä kirjaimilla)
        if any(k.nimi.lower() == kurssi.nimi.lower() for k in lista):
            print("kurssi on jo lisätty.")
            return False
        lista.append(kurssi)
        print("Kurssi lisätty.")
        return True
    
    # Poistaa kurssin nimen ja tyypin perusteella
    def poista_kurssi(self, nimi, tyyppi):
        lista = self.yto if tyyppi == "yto" else self.ammatilliset
        for k in lista:
            if k.nimi.lower() == nimi.lower():
                lista.remove(k)
                print("Kurssi poistettu.")
                return True
        print("Kurssia ei löytynyt.")
        return False
    
    # Laskee keskiarvot YTO-kursseista, ammatillisista ja kaikista yhteensä
    def laske_keskiarvo(self):
        def keskiarvo(lista):
            if not lista:
                return 0
            return round(sum(k.arvosana for k in lista) / len(lista), 2)
        
        yto_ka = keskiarvo(self.yto)
        amm_ka = keskiarvo(self.ammatilliset)
        kaikki = self.yto + self.ammatilliset
        yhteensa_ka = keskiarvo(kaikki)

        return {
            "yto": yto_ka,
            "ammatillinen": amm_ka,
            "kaikki": yhteensa_ka
        }

    # Muuntaa opiskelijan tiedot sanakirjaksi JSON-tallennusta varten
    def to_dict(self):
        return {
            "yto": [k.to_dict() for k in self.yto],
            "ammatillinen": [k.to_dict() for k in self.ammatilliset]
        }
    
# Sovelluksen pääluokka, joka sisältää valikon ja tiedostokäsittelyn
class OpintosuoritusoteSovellus:
    def __init__(self):
        self.opiskelijat = self.lataa_tiedot()
    
    # Lataa tallennetut opiskelijat ja heidän kurssit tiedostosta
    def lataa_tiedot(self):
        # Jos tiedostoa ei ole olemassa, palautetaan tyhjä sanakirja
        if not os.path.exists(TIEDOSTO):
            return {}

        # Avataan tiedosto lukemista varten
        with open(TIEDOSTO, "r", encoding="utf-8") as tiedosto:
            data = json.load(tiedosto)  # Ladataan JSON-muodossa oleva sisältö Pythonin sanakirjaksi

        opiskelijat = {}  # Tänne kerätään kaikki opiskelijaoliot

        # Käydään läpi jokainen opiskelija ja hänen kurssit
        for nimi, tiedot in data.items():
            op = Opiskelija(nimi)  # Luodaan uusi Opiskelija-olio nimen perusteella

            # Käydään läpi opiskelijan YTO-kurssit ja luodaan Kurssi-oliot niistä
            for k in tiedot.get("yto", []):
                op.yto.append(Kurssi(k["nimi"], k["osp"], k["arvosana"]))

            # Sama ammatillisille kursseille
            for k in tiedot.get("ammatillinen", []):
                op.ammatilliset.append(Kurssi(k["nimi"], k["osp"], k["arvosana"]))

            # Tallennetaan opiskelija sanakirjaan nimen perusteella
            opiskelijat[nimi] = op

        # Palautetaan kaikki opiskelijat
        return opiskelijat
    
    # Tallentaa opiskelijatiedot JSON-tiedostoon
    def tallenna_tiedot(self):
        data = {nimi: op.to_dict() for nimi, op in self.opiskelijat.items()}
        with open(TIEDOSTO, "w", encoding="utf-8") as tiedosto:
            json.dump(data, tiedosto, ensure_ascii=False, indent=2)

    # Sovelluksen päävalikko
    def valikko(self):
        while True:
            print("\n--- Opintosuoritusote ---")
            print()
            print("1. Lisää uusi opiskelija tai kurssi")
            print("2. Näytä opiskelijan tiedot")
            print("3. Poista opiskelija")
            print("4. Poista kurssi")
            print("5. Poistu")
            valinta = input("Valitse toiminto (1–5): ")

            if valinta == "1":
                self.lisaa_kurssi()        # Toteutetaan seuraavaksi
            elif valinta == "2":
                self.nayta_kurssit()       # Toteutetaan myöhemmin
            elif valinta == "3":
                self.poista_opiskelija()
            elif valinta == "4":
                self.poista_kurssi()       # Toteutetaan myöhemmin
            elif valinta == "5":
                self.tallenna_tiedot()     # Tallennetaan tiedot ennen poistumista
                print("Ohjelma suljetaan.")
                break
            else:
                print("Virheellinen valinta.")

    # Lisää uusi kurssi opiskelijalle
    def lisaa_kurssi(self):
        nimi = input("Anna opiskelijan nimi: ").strip()

        # Haetaan olemassa oleva opiskelija tai luodaan uusi
        if nimi in self.opiskelijat:
            opiskelija = self.opiskelijat[nimi]
        else:
            opiskelija = Opiskelija(nimi)
            self.opiskelijat[nimi] = opiskelija
            print("Uusi opiskelija lisätty.")

        # Valitaan kurssityyppi
        while True:
            tyyppi = input("Onko kurssi YTO vai ammatillinen? (yto/ammatillinen): ").strip().lower()
            if tyyppi in ["yto", "ammatillinen"]:
                break
            print("Virheellinen tyyppi. Kirjoita 'yto' tai 'ammatillinen'.")

        #Kysytään kurssin nimi
        kurssin_nimi = input("Anna kurssin nimi: ").strip()

        #Kysytään OSP-määrä ja varmistetaa, että se on kokonaisluku
        try:
            osp = int(input("Anna OSP-määrä: "))
            if osp <= 0:
                print("OSP:n täytyy olla positiivinen luku.")
                return
        except ValueError:
            print("OSP:n täytyy olla kokonaisluku.")
            return
        
        # Kysytään arvosana ja varmistetaan, että se on 1–5
        try:
            arvosana = int(input("Anna arvosana (1–5): "))
            if arvosana < 1 or arvosana > 5:
                print("Arvosanan täytyy olla välillä 1–5.")
                return
        except ValueError:
            print("Arvosanan täytyy olla kokonaisluku.")
            return

        # Luodaan uusi kurssi-olio
        uusi_kurssi = Kurssi(kurssin_nimi, osp, arvosana)

        # Lisätään kurssi opiskelijalle, jos ei ole jo olemassa
        if opiskelija.lisaa_kurssi(uusi_kurssi, tyyppi):
            self.tallenna_tiedot()  # TALLENNETAAN HETI
    
    # Näyttää opiskelijan kurssit ja keskiarvot
    def nayta_kurssit(self):
                # Listataan opiskelijat numeroilla
        if not self.opiskelijat:
            print("Ei opiskelijoita.")
            return

        print("\nValitse opiskelija:")
        nimilista = list(self.opiskelijat.keys())
        for i, nimi in enumerate(nimilista, 1):
            print(f"{i}. {nimi}")

        # Kysytään valinta ja tarkistetaan se
        try:
            valinta = int(input("Anna valinnan numero: "))
            if valinta < 1 or valinta > len(nimilista):
                print("Virheellinen valinta.")
                return
        except ValueError:
            print("Syötteen täytyy olla numero.")
            return

        # Haetaan valittu opiskelija
        valittu_nimi = nimilista[valinta - 1]
        opiskelija = self.opiskelijat[valittu_nimi]

        print(f"\nOpiskelijan {nimi} kurssit:")

        # Tulostetaan YTO-kurssit siistissä taulukkomuodossa
        if opiskelija.yto:
            print("\nYTO-kurssit:")
            print(f"{'Nro':<4} | {'Kurssin nimi':<65} | {'OSP':^5} | {'Arvosana':^8} |")
            print("-" * 93)
            for i, k in enumerate(opiskelija.yto, 1):
                print(f"{i:<4} | {k.nimi:<65} | {k.osp:^5} | {k.arvosana:^8} |")
        else:
            print("\nEi YTO-kursseja.")

        # Tulostetaan ammatilliset kurssit siistissä taulukkomuodossa
        if opiskelija.ammatilliset:
            print("\nAmmatilliset kurssit:")
            print(f"{'Nro':<4} | {'Kurssin nimi':<65} | {'OSP':^5} | {'Arvosana':^8} |")
            print("-" * 93)
            for i, k in enumerate(opiskelija.ammatilliset, 1):
                print(f"{i:<4} | {k.nimi:<65} | {k.osp:^5} | {k.arvosana:^8} |")
        else:
            print("\nEi ammatillisia kursseja.")

         #  Näytetään kurssien määrät ja lasketaan kurssien määrät & OSP-yhteissummat
        yto_lkm = len(opiskelija.yto)
        amm_lkm = len(opiskelija.ammatilliset)
        yhteensa_lkm = yto_lkm + amm_lkm

        yto_osp = sum(k.osp for k in opiskelija.yto)
        amm_osp = sum(k.osp for k in opiskelija.ammatilliset)
        yhteensa_osp = yto_osp + amm_osp

        print("\nKurssien määrät:")
        print(f"- YTO-kursseja: {yto_lkm} (yhteensä {yto_osp} osp)")
        print(f"- Ammatillisia kursseja: {amm_lkm} (yhteensä {amm_osp} osp)")
        print(f"- Kaikki kurssit yhteensä: {yhteensa_lkm} (yhteensä {yhteensa_osp} osp)")      

        # Lasketaan ja näytetään keskiarvot
        ka = opiskelija.laske_keskiarvo()
        print("\nKeskiarvot:")
        print(f"- YTO-kurssit: {ka['yto']}")
        print(f"- Ammatilliset kurssit: {ka['ammatillinen']}")
        print(f"- Kaikki kurssit yhteensä: {ka['kaikki']}")

    # Poistaa kurssin opiskelijalta
    def poista_kurssi(self):
        nimi = input("Anna opiskelijan nimi: ").strip()

        # Tarkistetaan löytyykö opiskelija
        if nimi not in self.opiskelijat:
            print("Opiskelijaa ei löytynyt.")
            return

        opiskelija = self.opiskelijat[nimi]

        # Kysytään kurssityyppi
        while True:
            tyyppi = input("Minkä tyyppinen kurssi poistetaan? (yto/ammatillinen): ").strip().lower()
            if tyyppi in ["yto", "ammatillinen"]:
                break
            print("Virheellinen tyyppi. Kirjoita 'yto' tai 'ammatillinen'.")

        # Näytetään valitun tyypin kurssit
        kurssilista = opiskelija.yto if tyyppi == "yto" else opiskelija.ammatilliset

        if not kurssilista:
            print("Ei kursseja tässä kategoriassa.")
            return

        print("\nOpiskelijan kurssit:")
        for k in kurssilista:
            print(f"- {k.nimi} ({k.osp} osp), arvosana: {k.arvosana}")

        # Kysytään poistettavan kurssin nimi
        kurssin_nimi = input("Anna poistettavan kurssin nimi: ").strip()

        # Yritetään poistaa kurssi
        if opiskelija.poista_kurssi(kurssin_nimi, tyyppi):
            self.tallenna_tiedot()  # TALLENNETAAN HETI

    # Poistaa koko opiskelijan ja hänen kurssinsa
    def poista_opiskelija(self):
        nimi = input("Anna poistettavan opiskelijan nimi: ").strip()

        if nimi not in self.opiskelijat:
            print("Opiskelijaa ei löytynyt.")
            return

        vahvista = input(f"Haluatko varmasti poistaa opiskelijan '{nimi}'? (k/e): ").strip().lower()
        if vahvista != "k":
            print("Poisto peruttu.")
            return

        del self.opiskelijat[nimi]
        self.tallenna_tiedot()
        print(f"Opiskelija '{nimi}' ja hänen kurssinsa poistettu.")


# Ohjelman käynnistys
if __name__ == "__main__":
    sovellus = OpintosuoritusoteSovellus()
    sovellus.valikko()