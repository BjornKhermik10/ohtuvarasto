"""Testiohjelma Varasto-luokan toiminnalle."""

from varasto import Varasto


def tulosta_varasto(varasto: Varasto, nimi: str) -> None:
    """Tulostaa varaston tilan ja siihen liittyvät tiedot."""
    print(f"{nimi}: {varasto}")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def testaa_mehu_varasto(mehua: Varasto) -> None:
    """Testaa mehuvaraston lisäys- ja otto-operaatiot."""
    print("Mehu setterit:")
    mehua.lisaa_varastoon(50.7)
    tulosta_varasto(mehua, "Mehuvarasto")
    mehua.ota_varastosta(3.14)
    tulosta_varasto(mehua, "Mehuvarasto")
    mehua.lisaa_varastoon(-666.0)
    tulosta_varasto(mehua, "Mehuvarasto")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    tulosta_varasto(mehua, "Mehuvarasto")


def testaa_olut_varasto(olutta: Varasto) -> None:
    """Testaa olutvaraston lisäys- ja otto-operaatiot."""
    print("Olut getterit:")
    tulosta_varasto(olutta, "Olutvarasto")
    olutta.lisaa_varastoon(1000.0)
    tulosta_varasto(olutta, "Olutvarasto")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    tulosta_varasto(olutta, "Olutvarasto")


def testaa_virhetilanteet() -> None:
    """Testaa virheelliset syötteet Varasto-luokalle."""
    huono = Varasto(-100.0)
    print(huono)
    huono = Varasto(100.0, -50.7)
    print(huono)


def main() -> None:
    """Pääohjelma, joka testaa Varasto-luokan toimintaa."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulosta_varasto(mehua, "Mehuvarasto")
    tulosta_varasto(olutta, "Olutvarasto")

    testaa_mehu_varasto(mehua)
    testaa_olut_varasto(olutta)
    testaa_virhetilanteet()


if __name__ == "__main__":
    main()
