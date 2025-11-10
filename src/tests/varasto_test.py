"""Yksikkötestit Varasto-luokalle."""


import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testiluokka Varasto-luokan toiminnallisuudelle."""

    def setUp(self):
        """Luodaan testivarasto ennen jokaista testiä."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Konstruktori luo varaston, jonka saldo on nolla."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Uudella varastolla on oikea tilavuus."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Lisäys kasvattaa varaston saldoa oikein."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Lisäys pienentää vapaata tilaa oikein."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Ottaminen palauttaa oikean määrän varastosta."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Ottaminen lisää varastossa vapaata tilaa."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        """Negatiivinen tilavuus nollataan konstruktorissa."""
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alku_saldo_nollataan(self):
        """Negatiivinen alku_saldo nollataan konstruktorissa."""
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alku_saldo_ei_voi_ylittaa_tilavuutta(self):
        """Alku_saldo ei voi ylittää tilavuutta."""
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_negatiivinen_ei_muuta_saldoa(self):
        """Negatiivinen lisäys ei muuta saldoa."""
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        """Lisäys, joka ylittää tilavuuden, täyttää varaston."""
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_negatiivisella_palauttaa_nolla(self):
        """Negatiivinen ottaminen palauttaa nolla."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_enemman_kuin_saldo_tyhjentaa_varaston(self):
        """Ottaminen suurempi kuin saldo tyhjentää varaston oikein."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikean_merkkijonon(self):
        """__str__ palauttaa oikean merkkijonon."""
        self.varasto.lisaa_varastoon(5)
        odotettu = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(self.varasto), odotettu)
