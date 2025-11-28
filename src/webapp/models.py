"""Tietokantamallit varastonhallintaan."""

# pylint: disable=too-few-public-methods

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Varasto(db.Model):
    """Varasto-tietokantamalli."""

    __tablename__ = 'varasto'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(100), nullable=False)
    tuotteet = db.relationship(
        'Tuote',
        backref='varasto',
        lazy=True,
        cascade='all, delete-orphan'
    )


class Tuote(db.Model):
    """Tuote-tietokantamalli."""

    __tablename__ = 'tuote'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(100), nullable=False)
    maara = db.Column(db.Integer, nullable=False, default=0)
    varasto_id = db.Column(
        db.Integer,
        db.ForeignKey('varasto.id'),
        nullable=False
    )
