"""Varasto-luokka varaston tilan hallintaan."""


class Varasto:
    """Luokka, joka kuvaa varastoa tilavuuden ja saldon avulla."""

    def __init__(self, tilavuus: float, alku_saldo: float = 0.0):
        """Alustaa varaston tilavuuden ja alkuperäisen saldon.

        Virheellinen tilavuus asetetaan nollaksi. 
        Liian suuri saldo rajoitetaan tilavuuden mukaiseksi.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = tilavuus

    def paljonko_mahtuu(self) -> float:
        """Palauttaa tilan, joka on vielä käytettävissä varastossa."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara: float) -> None:
        """Lisää varastoon annettu määrä, negatiiviset määrät ohitetaan."""
        if maara < 0:
            return

        if maara <= self.paljonko_mahtuu():
            self.saldo += maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara: float) -> float:
        """Ottaa varastosta annettua määrää. Palauttaa otetun määrän.

        Jos määrä on negatiivinen, palauttaa 0. Jos varasto ei riitä, 
        palauttaa kaiken jäljellä olevan saldon.
        """
        if maara < 0:
            return 0.0

        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo -= maara
        return maara

    def __str__(self) -> str:
        """Palauttaa varaston saldon ja jäljellä olevan tilan."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
