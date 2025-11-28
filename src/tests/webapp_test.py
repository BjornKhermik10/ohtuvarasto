"""Yksikkötestit web-sovellukselle."""

import unittest
from webapp.app import create_app
from webapp.models import db, Varasto, Tuote


class TestWebApp(unittest.TestCase):
    """Testiluokka web-sovelluksen toiminnallisuudelle."""

    def setUp(self):
        """Luodaan testisovellus ja tietokanta."""
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
        })
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Poistetaan tietokanta testin jälkeen."""
        with self.app.app_context():
            db.drop_all()

    def test_etusivu_nakyy(self):
        """Etusivu latautuu onnistuneesti."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Varastot'.encode(), response.data)

    def test_luo_varasto(self):
        """Uuden varaston luonti onnistuu."""
        response = self.client.post('/varasto/uusi', data={
            'nimi': 'Testivarasto'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Testivarasto'.encode(), response.data)

    def test_luo_varasto_tyhjalla_nimella_ei_luo(self):
        """Varastoa ei luoda tyhjällä nimellä."""
        self.client.post('/varasto/uusi', data={'nimi': ''})
        with self.app.app_context():
            varastot = Varasto.query.all()
            self.assertEqual(len(varastot), 0)

    def test_nayta_varasto(self):
        """Varaston näyttäminen onnistuu."""
        with self.app.app_context():
            varasto = Varasto(nimi='Testivarasto')
            db.session.add(varasto)
            db.session.commit()
            varasto_id = varasto.id
        response = self.client.get(f'/varasto/{varasto_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Testivarasto'.encode(), response.data)

    def test_muokkaa_varaston_nimea(self):
        """Varaston nimen muokkaus onnistuu."""
        with self.app.app_context():
            varasto = Varasto(nimi='Vanha nimi')
            db.session.add(varasto)
            db.session.commit()
            varasto_id = varasto.id
        response = self.client.post(
            f'/varasto/{varasto_id}/muokkaa',
            data={'nimi': 'Uusi nimi'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Uusi nimi'.encode(), response.data)

    def test_poista_varasto(self):
        """Varaston poisto onnistuu."""
        with self.app.app_context():
            varasto = Varasto(nimi='Poistettava')
            db.session.add(varasto)
            db.session.commit()
            varasto_id = varasto.id
        response = self.client.post(
            f'/varasto/{varasto_id}/poista',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            varasto = db.session.get(Varasto, varasto_id)
            self.assertIsNone(varasto)

    def test_lisaa_tuote_varastoon(self):
        """Tuotteen lisäys varastoon onnistuu."""
        with self.app.app_context():
            varasto = Varasto(nimi='Testivarasto')
            db.session.add(varasto)
            db.session.commit()
            varasto_id = varasto.id
        response = self.client.post(
            f'/varasto/{varasto_id}/tuote/uusi',
            data={'nimi': 'Testituote', 'maara': '10'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Testituote'.encode(), response.data)

    def test_poista_tuote(self):
        """Tuotteen poisto onnistuu."""
        with self.app.app_context():
            varasto = Varasto(nimi='Testivarasto')
            db.session.add(varasto)
            db.session.commit()
            tuote = Tuote(nimi='Poistettava', maara=5, varasto_id=varasto.id)
            db.session.add(tuote)
            db.session.commit()
            tuote_id = tuote.id
        response = self.client.post(
            f'/tuote/{tuote_id}/poista',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            tuote = db.session.get(Tuote, tuote_id)
            self.assertIsNone(tuote)

    def test_muokkaa_tuotteen_maaraa(self):
        """Tuotteen määrän muokkaus onnistuu."""
        with self.app.app_context():
            varasto = Varasto(nimi='Testivarasto')
            db.session.add(varasto)
            db.session.commit()
            tuote = Tuote(nimi='Testituote', maara=5, varasto_id=varasto.id)
            db.session.add(tuote)
            db.session.commit()
            tuote_id = tuote.id
        response = self.client.post(
            f'/tuote/{tuote_id}/muokkaa',
            data={'maara': '20'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            tuote = db.session.get(Tuote, tuote_id)
            self.assertEqual(tuote.maara, 20)

    def test_varasto_ei_loydy_404(self):
        """Palauttaa 404 kun varastoa ei löydy."""
        response = self.client.get('/varasto/9999')
        self.assertEqual(response.status_code, 404)

    def test_tuote_ei_loydy_404(self):
        """Palauttaa 404 kun tuotetta ei löydy."""
        response = self.client.post('/tuote/9999/poista')
        self.assertEqual(response.status_code, 404)
